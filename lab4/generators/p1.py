n = int(input())
gen = (i ** 2 for i in range(n+1))

for x in gen:
    print(x, end=" ")