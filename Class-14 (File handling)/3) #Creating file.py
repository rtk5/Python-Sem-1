#Creating file
fp=open('write.txt','w')    #creates new file if no file present    # 'w' - write type file
                            #writes over existing file if file present
#To enter text
fp.write('have a nice day')
print(',How are you?',file=fp)

#to read text from write.txt create a new file(Reading file) 