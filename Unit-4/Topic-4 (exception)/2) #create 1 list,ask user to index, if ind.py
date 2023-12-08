#create 1 list,ask user to index, if index is 5, shows exception
try:
    s=input("ENter list-").split(",")
    l=[]
    for i in range (len(s)):
        l.append(i)
        if l[i]==5:
            raise ValueError
except ValueError:
        print("This is unacceptable")
else:
    print("SUre, go for it")        
