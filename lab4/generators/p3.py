n=int(input())
gen = (i for i in range(n) if i%3==0 and i%4==0 )

for x in gen:
    print(x)