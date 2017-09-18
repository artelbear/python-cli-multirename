# For run you need Kivy, Python3


import os
# from kivy.app import App


directory = input("Search where:\t")

if directory == "":
    directory = "."


old_pattern = input("Contain what:\t")

if old_pattern == "":
    old_pattern = "*"


new_pattern = input("Rename to:\t")


os.chdir(directory)

file_names = os.listdir(".")


i = 0

for old in file_names:
    i = i + 1

    if old_pattern == "*":
        new = "{0}{1}{2}".format(new_pattern, str(i), old[-4:len(old)])
        print("{0}\t\tchange to\t\t{1}".format(old, new))
        os.renames(old, new)

    elif old_pattern in old:
        new = "{0}{1}{2}".format(new_pattern, str(i), old[-4:len(old)])
        print("{0}\t\tchange to\t\t{1}".format(old, new))
        os.renames(old, new)
