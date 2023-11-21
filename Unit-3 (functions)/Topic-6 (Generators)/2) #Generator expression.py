#Generator Expression
generator_exp=(i**2 for i in range(5) if i%2==0)
for i in generator_exp:
    print(i)