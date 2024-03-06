import os

x=input("path:")
if os.path.exists(x):
    print(os.listdir(x))