#built in functions

#startswith 3 parameters
s1="watsapp"
print(s1.startswith('w',1)) #start and end  #checks if 'w' is the starting letter
print(s1.startswith('w',0,5)) 

#endwith
print(s1.endswith('p',1,5))

print(s1.startswith('wa')) 
print(s1.startswith('ppas',-1,-5)) 

print(s1[-1:-5:-1])
