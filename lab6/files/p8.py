import os
x=r"C:\Users\Aibar\Desktop\pp2\practice\lab6\files\test\del"
print("existense:",os.path.exists(x))
print("readability:",os.access(x,os.R_OK))
print("writibility:",os.access(x,os.W_OK))
print("executibilty:",os.access(x,os.X_OK))
os.rmdir(x)
