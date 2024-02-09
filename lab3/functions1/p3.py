def solve(numheads,numlegs):
    for i in range(100):
        for j in range(100):
            if i+j==numheads and 4*i + 2*j==numlegs:
                print(i,j)
solve(35,94)            