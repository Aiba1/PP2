n = int(input())

gnr = (i for i in range(n+1) if i % 2 == 0)

b =[]

for x in gnr:
    b.append(x)

print(b)
    