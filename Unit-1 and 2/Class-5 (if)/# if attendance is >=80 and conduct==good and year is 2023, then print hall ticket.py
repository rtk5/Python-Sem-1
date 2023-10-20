# if attendance is >=80 and conduct==good and year is 2023, then print hall ticket

attendance=int(input('Enter attendance-'))
conduct=input('Enter conduct-')                  #string value
year=int(input("Enter year-"))
               
if attendance>=80 and conduct == 'good' and year==2023:
    print('issue hall ticket')
else:
    print("Don't issue hall ticket")