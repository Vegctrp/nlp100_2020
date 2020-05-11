from stemming.porter2 import stem
import spacy
import re
from collections import Counter
from sklearn.linear_model import LogisticRegression
import pickle
import random
import numpy as np
import statistics

nlp = spacy.load("en")

def get_feat_from_sentence(string):
    sl = nlp.make_doc(string)
    string = [stem(i.lemma_.lower()) for i in sl]
    return string

def data2stemmed(data):
    return [(label, get_feat_from_sentence(string)) for label,string in data]

def get_feature_stems(stemmed):
    counter = Counter([tok for _,toks in stemmed for tok in toks])
    #for i in counter.most_common():
    #    print(i)
    return [stem for stem,num in counter.most_common() if 2<num<1000]

def make_count_mat(stemmed, feature):
    tl = [label for label,_ in stemmed]
    xl = [make_count_vec(steml, feature) for _,steml in stemmed]
    return tl, xl

def make_count_vec(steml, feature):
    cd = Counter(steml)
    return [cd[stem] if stem in cd else 0 for stem in feature]

def write_features(filename, tl, xl, feature):
    assert len(tl)==len(xl)
    with open(filename, "w") as out:
        print(",".join(feature), file=out)
        for t,x in zip(tl,xl):
            print(t+","+",".join([str(int(i)) for i in x]), file=out)

def predict_from_midashi(midashi, lr, feature):
    midashi_stemmed = get_feat_from_sentence(midashi)
    midashi_vec = make_count_vec(midashi_stemmed, feature)
    res = lr.predict_proba([midashi_vec])[0]
    return res,res.argmax(),res.max()

def accuracy(lr, xl, tl):
    res = lr.predict(xl)
    return (res==tl).mean()

def make_confusion_matrix(lr, xl, tl):
    label_dic = {"b":0, "e":1, "m":2, "t":3}
    mat = np.zeros((4,4),dtype=int)
    res = lr.predict(xl)
    for gold_label, system_label in zip(tl, res):
        mat[label_dic[system_label]][label_dic[gold_label]] += 1
    return mat

def macro_score(mat):
    scores_part = [macro_score_part(mat, target) for target in range(4)]
    recall = statistics.mean([i[0] for i in scores_part])
    precision = statistics.mean([i[1] for i in scores_part])
    f1_score = 2*recall*precision / (recall+precision)
    return recall, precision, f1_score

def macro_score_part(mat, target):
    msum = np.sum(mat)
    TP = mat[target][target]
    FP = sum(mat[target]) - TP
    FN = sum(mat[:,target]) - TP
    TN = msum - TP - FP - FN
    recall = TP/(TP+FN)
    precision = TP/(TP+FP)
    return recall, precision, msum, TP, FP, FN, TN

def micro_score(mat):
    print(mat)
    msum = np.sum(mat)
    TP = sum([mat[i][i] for i in range(4)])
    FP = msum - TP
    score = TP/(TP+FP)
    return score

def print_scores(mat):
    print(mat)
    scores = [micro_score(mat)] + list(macro_score(mat))
    print("macro_precision", scores[2])
    print("macro_recall", scores[1])
    print("macro_f1", scores[3])
    print("micro", scores[0])

if __name__ == '__main__':
    with open("52lr.pickle","rb") as reg:
        lr = pickle.load(reg)
    with open("52data.pickle","rb") as reg:
        feature, train_t, train_x, test_t, test_x, valid_t, valid_x = pickle.load(reg)
    
    category = {"b":"business", "e":"entertainment", "m":"health", "t":"science and technology"}

    for i,label in enumerate(["b", "e", "m", "t"]):
        print(category[label])
        indexl = lr.coef_[i].argsort()
        for j,index in enumerate(indexl[:-21:-1]):
            print(j,feature[index],lr.coef_[i][index])
        
        for j,index in enumerate(indexl[:20]):
            print(j,feature[index],lr.coef_[i][index])