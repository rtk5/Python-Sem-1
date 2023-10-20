# write a program to print grade if mrks >=70 , print grade b if marks >=50 and print grade c >=35 else print fail

mrks=int(input('Enter your marks-'))
if mrks>=80:
    print('grade A')
elif mrks >= 50:
    print('grade B')
elif mrks >=35:
    print('grade C')
else:
    print ('fail')
