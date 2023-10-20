#WAP to print number divisible by 3 and 5 
#using for loop and user specified range
start=int(input('Enter start-'))
stop=int(input('Enter stop-'))
for i in range(start,stop):
    if(i%15==0):
        print(i)