from stemming.porter2 import stem
import spacy
import re
from collections import Counter
from sklearn.linear_model import LogisticRegression
import pickle
import random

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

if __name__ == '__main__':
    with open("52lr.pickle","rb") as reg:
        lr = pickle.load(reg)
    with open("52data.pickle","rb") as reg:
        feature, train_t, train_x, test_t, test_x, valid_t, valid_x = pickle.load(reg)
    
    print("train :",accuracy(lr, train_x, train_t))
    print("test : ",accuracy(lr, test_x, test_t))