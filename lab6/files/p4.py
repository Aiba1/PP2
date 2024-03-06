import os

x = r"C:\Users\Aibar\Desktop\pp2\practice\lab6\files\test\a.txt"
file = open(x)
num=0
for line in file:
    num+=1

print(num)