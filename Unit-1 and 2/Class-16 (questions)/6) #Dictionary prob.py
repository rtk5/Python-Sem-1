
#input="good book good sleep read book"
#output={'good':2,'book':2,'sleep':1,'read':1}

n="good book good sleep read book"
n1=n.split()
d={}
for word in n1:
    if word not in d:
        d[word]=0
    d[word]=d[word]+1
print(d)

#output={'good',:4,'sleep':5,'read':4}

