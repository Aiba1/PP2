n=int(input())
gen=(i for i in range(n,-1,-1))
for x in gen:
    print(x,end=' ')