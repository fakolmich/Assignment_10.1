import os
import time

directory = input("Enter your directory name")
filename = input("Enter your file name")
parent_directory = os.getcwd()
paths = os.path.join(parent_directory, directory)
full_file_path = paths + "//" + filename+".txt"
isdir = os.path.isdir(paths)
if not isdir:
    os.mkdir(paths)
    print("Directory Created")


name = input("Enter your name")
address = input("Enter your address")
phone = input("Enter your phone number")

file_content = f"{name},{address},{phone}"

file = open(full_file_path, "w+")
file.write(file_content)
file.close()

with open(full_file_path) as file:
    print('Reading your file please wait...')
    time.sleep(2)
    data = file.read()
    print(data)
