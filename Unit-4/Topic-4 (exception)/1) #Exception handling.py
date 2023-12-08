#Exception handling
try:
    a=int(input("Enter one number-"))
    b=int(input("Enter other number-"))
    c=a/b
except ZeroDivisionError:
    print("Invalid division")
else:
    print(c)
finally:
    print("Thank you")

print()

def f1():
    try:
        a=int(input("Enter one number-"))
        b=int(input("Enter other number-"))
        c=a/b
    except ZeroDivisionError:
        #print("Invalid division")
        return 0
    finally:
        print("Executed")
print(f1())


