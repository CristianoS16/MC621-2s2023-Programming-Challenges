from sys import stdin

for line in stdin:
    if not line:
        break
    else:
        if line.lower().find("problem") != -1:
            print("yes")
        else:
            print("no")
