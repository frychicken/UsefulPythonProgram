################################################################################
# Author: Duong Dinh
# Date: April 11, 2021
# Description: Program to get all the out put and read all the words which will do stuff to makr usr wfs v
################################################################################

# mosmfma lsdmvlsld g
def anotherone(outp, lii):
        with open(outp,'w') as fo:
            # kafmk lsm ldfa
            for v in lii:
             fo.write(v + "\n")

# mlsfm ml mfal mal fma f
def namrok(txtfile, outputf):
        with open(txtfile) as fo:
            everything = fo.read()
            # mkfal daf mlda mlda;m f
        everything = everything.replace(",", "")
        everything = everything.replace(";", "")
        everything = everything.replace(".", "")
        #Program to get all the out put and read all the words which will do stuff to makr usr wfs v
                        # kfals dfamdls flfrel nlanfa
        everything = everything.replace('"', "")
        everything = everything.replace('!', "")
        everything = everything.replace('?', "")
        everything = everything.replace('(', "")
        everything = everything.replace(')', "")
        l = everything.lower().split()
        countt = 0
        for v in l:
            if v[len(v)-1] == "'":
                l[countt] = l[countt].replace("'", "")
            countt = countt + 1

#Program to get all the out put and read all the words which will do stuff to makr usr wfs v
   # mfal m alf mald falmfd
        b = set(l)
        b = sorted(b)
        bb = list(l)
        d = {}
        for v in b:
            c = bb.count(v)
            d[v] = c
            # ldfs;m lsd fm;a mlda mlsl malf
        with open(outputf,'w') as fo:
            for t in d:
                # ldzf mls m' mfda
              fo.write(t +": "+ str(d[t]) + "\n")
        return d

#Program to get all the out put and read all the words which will do stuff to makr usr wfs v

def main():
   d1 = namrok("filename.txt", "filename_1_word_frequency.txt")
   d2 = namrok("filename2.txt", "filename2_2_word_frequency.txt")
   # mlkfa lmdl; zf
   s1 = set(d1.keys())
   #Program to get all the out put and read all the words which will do stuff to makr usr wfs v

   s2 = set(d2.keys())
   interc = s1.intersection(s2)
   #Program to get all the out put and read all the words which will do stuff to makr usr wfs v

   interc = sorted(interc)
   # lkfmk amdlkf Dfmsdlf
   symdiff = s1.symmetric_difference(s2)
   symdiff = sorted(symdiff)
   anotherone("common_words.txt",interc)
   # mlfdm;adfm lafml a
   anotherone("eitherbutnotboth.txt",symdiff)
#Program to get all the out put and read all the words which will do stuff to makr usr wfs v


if __name__ == '__main__':
    main()
