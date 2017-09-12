import os

directory = input("Where:\t")
if directory == "":
    directory = "."
oldpattern = input("What:\t")
newpattern = input("To:\t")
os.chdir(directory)
filenames = os.listdir()
for old in filenames:
    if oldpattern in old:
        new = old.replace(oldpattern, newpattern)
        print(old + "\t\tchange to\t\t" + new)
        os.renames(old, new)