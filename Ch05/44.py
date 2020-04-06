import pydot

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

class Chunk:
    def __init__(self, line=None):
        if line is None:
            self.morphs=[]
            self.dst=-1
            self.srcs=[]
        else:
            self.morphs = []
            self.dst = int(line.split(" ")[1][:-1])
            self.srcs = []
    def add_morph(self,morph):
        self.morphs.append(morph)
    def add_dst(self,dst):
        self.dst=dst
    def add_src(self,src):
        self.srcs.append(src)
    def print_chunk(self):
        print("Chunk : \n\tmorphs : ")
        for morph in self.morphs:
            print("\t\t",end="")
            morph.print_morph()
        print("\tdst : {}".format(self.dst))
        print("\tsrcs : { ",end="")
        for src in self.srcs:
            print(str(src)+" ",end="")
        print("}")
    def chunk_string(self):
        return "".join([morph.surface for morph in self.morphs])
    def chunk_string_without_sign(self):
        return "".join([morph.surface if morph.pos!="記号" else "" for morph in self.morphs])
    def include_verb(self):
        for morph in self.morphs:
            if morph.pos=="動詞":
                return True
        return False
    def include_noun(self):
        for morph in self.morphs:
            if morph.pos=="名詞":
                return True
        return False

def make_novellist():
    novel_list = []
    with open("../data/neko.txt.cabocha", "r") as intxt:
        fulltxt = intxt.read()
        for sentence in fulltxt.split("EOS"):
            if sentence != "\n":
                sentence_list = []
                chunks = sentence.split("* ")
                for chunk in chunks[1:]:
                    cs = chunk.split("\n")
                    c = Chunk(cs[0])
                    for morph in cs[1:-1]:
                        c.add_morph(Morph(morph))
                    sentence_list.append(c)
                
                for i,chunk in enumerate(sentence_list):
                    if chunk.dst != -1:
                        sentence_list[chunk.dst].add_src(i)
                novel_list.append(sentence_list)
    return novel_list

if __name__ == '__main__':
    nl = make_novellist()
    sentence_num = 3
    graph = []
    for chunk in nl[sentence_num]:
        src_string = chunk.chunk_string_without_sign()
        if chunk.dst == -1:
            dst_string = ""
        else:
            dst_string = nl[sentence_num][chunk.dst].chunk_string_without_sign()
        if src_string !="" and dst_string !="":
            graph.append((src_string, dst_string))
    
    print(graph)
    g=pydot.graph_from_edges(graph,directed=True)
    g.write_png("44result.png")