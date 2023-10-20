#write a program to print alphabets of string on each line using 'for' loop
n=input('Enter string-')
l=len(n)
for i in range(l):
    print(n[i],ord(n[i]))
