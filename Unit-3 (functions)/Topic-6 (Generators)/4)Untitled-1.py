
def my_generator():
    for i in range(int(input("ENTER:"))):
        yield i

gen=my_generator()
for j in gen:
    print(j)