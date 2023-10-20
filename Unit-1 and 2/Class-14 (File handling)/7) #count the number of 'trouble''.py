#count the number of 'trouble' words in file

#from File1
fp=open("/home/rithvikmatta/Python/Class-14/File1.txt",'r')       #works directly in terminal
e=fp.readlines()
count=0
fp.close
for lines in e:
    count+=lines.count('trouble')
print(count)
