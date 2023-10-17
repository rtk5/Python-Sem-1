#Printing

fp=open("/home/rithvikmatta/Python/Class-14/File1.txt")       #works directly in terminal
e=fp.readlines()
#print(e)   #output= ['do not\n', 'trouble\n', 'the trouble\n', '  till\n', 'trouble\n', '\n', 'troubles you']

for ele in e:
    print(ele,end="")       #prints properly

fp.close()