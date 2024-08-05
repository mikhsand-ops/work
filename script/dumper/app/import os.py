import os

# get current working directory
cwd = os.getcwd()

#get files in directory
files = os.listdir(cwd) 

print(type(files))