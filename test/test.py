def readWords():
    ordlist = []
    with open("./ord.txt",'r',encoding = 'utf-8') as f:
        ordlist = f.read().split()
        f.close()
    return ordlist

def lookfor(word):
    if (len(word) != 4): return -1
    if (word[0] == word[3] 
    and word[1] == word[2]): return 1
    return -1

ord = readWords()

abba = []
for o in ord:
    if (lookfor(o) == 1): 
        abba.append(o)

print(abba)
