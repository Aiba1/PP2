def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

numbers = [23, 56, 17, 29, 31, 40, 47, 53]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)
