class Morph:
    def __init__(self,surf_line,base=None,pos=None,pos1=None):
        if base is not None:
            self.surface=surf_line
            self.base=base
            self.pos=pos
            self.pos1=pos1
        else:
            self.surface = surf_line.split("\t")[0]
            self.base = surf_line.split("\t")[1].split(",")[6]
            self.pos = surf_line.split("\t")[1].split(",")[0]
            self.pos1 = surf_line.split("\t")[1].split(",")[1]

    def print_morph(self):
        print("{} {} {} {}".format(self.surface,self.base,self.pos,self.pos1))

def make_novellist():
    novel_list = []
    with open("../data/neko.txt.cabocha", "r") as intxt:
        fulltxt = intxt.read()
        for sentence in fulltxt.split("EOS"):
            if sentence != "\n":
                sentence_list = []
                for morph in sentence.split("\n"):
                    if morph!="" and morph[0]!="*":
                        sentence_list.append(Morph(morph))
                novel_list.append(sentence_list)
    return novel_list

if __name__ == '__main__':
    nl = make_novellist()
    for ml in nl[2]:
        ml.print_morph()