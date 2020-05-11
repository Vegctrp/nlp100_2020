from stemming.porter2 import stem
import spacy
import re
from collections import Counter
from sklearn.linear_model import LogisticRegression
import pickle

nlp = spacy.load("en")

def get_data():
    test = []
    train = []
    valid = []
    with open("./test.txt") as intxt:
        line = intxt.readline()
        while line:
            test.append(tuple(line.strip("\n").split("\t")))
            line = intxt.readline()
    with open("./train.txt") as intxt:
        line = intxt.readline()
        while line:
            train.append(tuple(line.strip("\n").split("\t")))
            line = intxt.readline()
    with open("./valid.txt") as intxt:
        line = intxt.readline()
        while line:
            valid.append(tuple(line.strip("\n").split("\t")))
            line = intxt.readline()
    return train, test, valid

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

if __name__ == '__main__':
    train, test, valid = get_data()
    train_stemmed = data2stemmed(train)
    test_stemmed = data2stemmed(test)
    valid_stemmed = data2stemmed(valid)

    feature = get_feature_stems(train_stemmed)
    train_t, train_x = make_count_mat(train_stemmed, feature)
    test_t, test_x = make_count_mat(test_stemmed, feature)
    valid_t, valid_x = make_count_mat(valid_stemmed, feature)

    #write_features("./train.feature.txt", train_t, train_x, feature)
    #write_features("./test.feature.txt", test_t, test_x, feature)
    #write_features("./valid.feature.txt", valid_t, valid_x, feature)

    lr = LogisticRegression(max_iter=1000)
    print(lr.fit(train_x, train_t))
    print(lr.score(train_x, train_t))
    print(lr.score(test_x, test_t))

    with open("52lr.pickle", "wb") as pickleout:
        pickle.dump(lr, pickleout)
    
    with open("52data.pickle", "wb") as pickleout:
        pickle.dump([feature, train_t, train_x, test_t, test_x, valid_t, valid_x], pickleout)