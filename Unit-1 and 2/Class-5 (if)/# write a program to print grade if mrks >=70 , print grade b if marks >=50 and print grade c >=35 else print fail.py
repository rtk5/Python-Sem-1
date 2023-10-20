# write a program to print grade if mrks >=70 , print grade b if marks >=50 and print grade c >=35 else print fail

num=int(input('Enter your marks-'))
if num>=80:
    print('grade A')
else num >= 50:
    print('grade B')
    if num>=30:
        print('grade c')
    else :
         print ('fail')

