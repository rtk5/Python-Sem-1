try:
    a=int(input("enter number btw 5 to 9-"))
    if (a<5 or a>9):
        raise ValueError
except ValueError:
    print("Entered value must be btw 5 and 9!!!!!!!!!")
finally:
    print("Thank you")

print()

