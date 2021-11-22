import os
import shutil
path = 'C:/Users/Lenovo/Desktop/python_work'
print("before moving files:")
print(os.listdir(path))
source = "C:/Users/Lenovo/Desktop/python_work/a.txt"
destination = "C:/Users/Lenovo/Desktop/python_work/a(copy).txt"
dest = shutil.copy(source,destination)
print("after copying files:")
print(os.listdir(path))