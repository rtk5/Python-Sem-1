#write a function that output the length of words in string
#input="welcome python"   output= 7 6

def count(s):
    w=s.split()
    for word in w:
        print(len(word),end=" ")
count('welcome python')
