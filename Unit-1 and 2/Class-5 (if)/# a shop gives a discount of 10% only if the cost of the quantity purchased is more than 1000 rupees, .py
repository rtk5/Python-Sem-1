# a shop gives a discount of 10% only if the cost of the quantity purchased is more than 1000 rupees, 
#one unit costs 100 rupees, print total cost for the user, take the quantity as user input

quantity=int(input('Enter quantity-'))
cost=quantity*100
if cost>=1000:
    print ('cost is',quantity*90)
else:
    print('cost is',cost)