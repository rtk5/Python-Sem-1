#Given a list, print the elements of the list in seperate line

s1=input("Enter values-").split()

for i in range(len(s1)):
    s1[i]=int(s1[i])  #changing string to integer
print(s1)

#use space in terminal ie 24 35 56