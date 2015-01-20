__author__ = 'uermel'

import re

infilename = input("Path to VectorNTI primer archive:")
outfilename = input("Output path:")


infile = open(infilename, mode='r', encoding="ISO-8859-1")
outfile = open(outfilename, mode='w')

raw = infile.readlines()
infile.close()

final = list()
good = [["", ""]]*len(raw)

for i in range(len(raw)):
    line = raw[i]
    if re.search("12\|", line) :
        good[i][0] = line[3:len(line)-1]
        good[i][1] = raw[i+2][3:len(raw[i+2])-1]
        final.append(good[i][0]+","+good[i][1]+"\n")

outfile.writelines(final)
outfile.close()

print("All Done! Result saved at:"+outfilename)

