try:
    a=int(input("Enter one number-"))
    b=int(input("Enter other number-"))
    c=a/b
    if b==0:
        raise NameError
    else:
        c=a/b
        print(c)
except Exception as e:
    print(e.__class__.__name__)
    print(e)
else:
    print("in else")
finally:
    print("Thank you")

print()
