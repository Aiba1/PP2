# checking access to file

import os

filename = input()

print(os.access(filename, os.F_OK)) 
print(os.access(filename, os.R_OK)) 
print(os.access(filename, os.W_OK)) 
print(os.access(filename, os.X_OK)) 