try:
    a=int(input("Enter one number-"))
    b=int(input("Enter other number-"))
    c=a/b
except ZeroDivisionError:
    print("Invalid division")
except ValueError:                      #except block should be at the end
    print("Entered value is string")
else:
    print(c)
finally:
    print("Thank you")

print()

try:
    a=int(input("Enter one number-"))
    b=int(input("Enter other number-"))
    c=a/b
except (ZeroDivisionError,ValueError):
    print("Invalid division")
else:
    print(c)
finally:
    print("Thank you")

print()

try:
    a=int(input("Enter one number-"))
    b=int(input("Enter other number-"))
    c=a/b
except Exception:
    print("Invalid division")
else:
    print(c)
finally:
    print("Thank you")

print()
