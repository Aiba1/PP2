import os
path=r'C:\Users\Aibar\Desktop\pp2\practice\lab6\files\test\\'

m = ["a","b","c","d","e","f","g","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for j in range(26):
    file=open(f"{path}{m[j]}.txt","w")
    file.close()