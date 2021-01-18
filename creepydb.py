# This program is for using my homemade database
import os
#First open file and find upper bound & lower bond:
def upperlowerbound():
    f=open("CDB.txt", 'r')
    counter=0
    upperlimit=0
    lowerlimit=0
    for line in f:
        print(line)
        line.split()
        counter=counter+1
        if line == "{":
            upperlimit = counter
    for line in f:
        line.split()
        counter=counter+1
        print(line)
        if line == "}":
            lowerlimit = counter
    f.close()
    return upperlimit,lowerlimit
print(os.getcwd())
a=upperlowerbound()
print(a)