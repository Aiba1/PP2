def palin(str):
    Is = True
    for i in range(len(str)//2):
        if str[i]==str[len(str)-i-1]:
            Is=True
        else:
            Is=False
            break
    if Is:
        return True
    else:
        return False
print(palin("madam"))
