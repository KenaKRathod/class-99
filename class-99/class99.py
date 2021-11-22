import os
import shutil
path = 'C:/Users/Lenovo/Desktop/python_work'
print("before moving files:")
print(os.listdir(path))
source = "C:/Users/Lenovo/Desktop/python_work/fri.txt"
destination = "C:/Users/Lenovo/Desktop/python_work/fri(copy).txt"
dest = shutil.move(source,destination)



