def set_2(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
print(set_2([5,48,5,63,6,48,56]))
