def prime(lst):
    for x in lst:
        if x <= 1:
            continue
        is_prime = True
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                is_prime = False
                break  
        if is_prime:
            print(x)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
prime(x)
