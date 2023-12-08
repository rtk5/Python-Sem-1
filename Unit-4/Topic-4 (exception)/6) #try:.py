try:
    j=2/0
except ZeroDivisionError as z:
    print("You are in except",z)
except Exception as e:
    print("Exception is",e)
    
