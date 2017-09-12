import os

directory = input("Where:\t")
if directory == "":
    directory = "."
oldpattern = input("What:\t")
if oldpattern == "":
    oldpattern = "*"
newpattern = input("To:\t")
os.chdir(directory)
filenames = os.listdir()
i = 0
for old in filenames:
    if oldpattern == "*":
        i = i + 1
        new = newpattern + str(i)
        print(old + "\t\tchange to\t\t" + new)
        os.renames(old, new)
    elif oldpattern in old:
        i = i + 1
        new = old.replace(oldpattern, newpattern)
        new = new + str(i)
        print(old + "\t\tchange to\t\t" + new)
        os.renames(old, new)