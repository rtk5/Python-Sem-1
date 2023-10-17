#Append
fp=open('data.txt','a')     #if i run it twice, text in data.txt    printed twice
#fp=open('data.txt','w')     #since it overwrites on data.txt    printed only once

print('appended data',file=fp)
fp=open('data.txt','r')
d=fp.read()
print(d)