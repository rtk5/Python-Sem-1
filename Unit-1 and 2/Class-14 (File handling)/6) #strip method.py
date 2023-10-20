#strip method
fp=open('data.txt','r')
d=fp.readline()
print('line1',d)
print(d.strip())        #removes white spaces in the start of the line

