def reverse_string(a):
    arr = []
    x = a.split()
    for i in range(len(x)-1, -1, -1):
        arr.append(x[i])
    print(arr)

reverse_string("are you ready")
