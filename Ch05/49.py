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
    def get_first_verb(self):
        for morph in self.morphs:
            if morph.pos=="動詞":
                return morph.base
        return ""
    def get_last_pparticle(self):
        for morph in self.morphs[::-1]:
            if morph.pos=="助詞":
                return morph.base
        return ""

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

def chunk_replace_noun(chunk, string):
    ans = []
    fl = 1
    for morph in chunk.morphs:
        if morph.pos == "記号":
            continue
        elif morph.pos =="名詞" and fl:
            ans.append(string)
            fl = 0
        elif morph.pos =="名詞":
            continue
        else:
            ans.append(morph.surface)
    return "".join(ans)


if __name__ == '__main__':
    nl = make_novellist()
    for sl in nl:
        path_dict = {}
        for chunk_num,chunk in enumerate(sl):
            if chunk.include_noun():
                path = [chunk_num]
                now = chunk.dst
                while now != -1:
                    path.append(now)
                    now = sl[now].dst
                path_dict[chunk_num] = path

        for srcx in path_dict:
            for srcy in path_dict:
                if srcx < srcy:
                    pathx = path_dict[srcx]
                    pathy = path_dict[srcy]
                    if srcy in pathx:
                        print(chunk_replace_noun(sl[srcx],"X"), end="")
                        now = pathx[1]
                        while now != srcy:
                            print(" -> " + sl[now].chunk_string_without_sign(), end="")
                            now = sl[now].dst
                        print(" -> Y")
                    else:
                        length = 0
                        while pathx[-length-1:] == pathy[-length-1:]:
                            length+=1
                        path_same = path_dict[srcx][-length:]
                        pathx = pathx[:len(pathx)-length]
                        pathy = pathy[:len(pathy)-length]
                        print(chunk_replace_noun(sl[srcx],"X"), end="")
                        for i in pathx[1:]:
                            print(" -> " + sl[i].chunk_string_without_sign(), end="")
                        print(" | ", end="")
                        print(chunk_replace_noun(sl[srcy],"Y"), end="")
                        for i in pathy[1:]:
                            print(" -> " + sl[i].chunk_string_without_sign(), end="")
                        print(" | ", end="")
                        print(sl[path_same[0]].chunk_string_without_sign(), end="")
                        for i in path_same[1:]:
                            print(" -> " + sl[i].chunk_string_without_sign(), end="")
                        print()
        print("#######")