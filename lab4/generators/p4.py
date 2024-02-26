def squares(a,b):
    for x in range(a,b+1):
        yield x**2

gen = squares(4,77)

for x in gen:
    print (x, end=" ")
