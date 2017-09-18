# For Run you need os, Cython, Kivy, Python3


import os
# from kivy.app import App


directory = input("Where:\t")

if directory == "":
    directory = "."


old_pattern = input("What:\t")

if old_pattern == "":
    old_pattern = "*"


new_pattern = input("To:\t")


os.chdir(directory)

file_names = os.listdir()


i = 0

for old in file_names:

    if old_pattern == "*":
        i = i + 1
        new = new_pattern + str(i)
        print(old + "\t\tchange to\t\t" + new)
        os.renames(old, new)

    elif old_pattern in old:
        i = i + 1
        new = old.replace(old_pattern, new_pattern)
        new = new + str(i)
        print(old + "\t\tchange to\t\t" + new)
        os.renames(old, new)