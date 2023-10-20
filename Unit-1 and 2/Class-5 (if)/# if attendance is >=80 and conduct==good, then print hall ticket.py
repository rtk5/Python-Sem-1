# if attendance is >=80 and conduct==good, then print hall ticket

attendance=int(input('Enter attendance-'))
conduct=input('Enter conduct-')                  #string value
if attendance>=80 and conduct == 'good':
    print('issue hall ticket')
else:
    print("Don't issue hall ticket")