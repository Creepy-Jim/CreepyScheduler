import sys,os
'''def filereader()
def nociter(currentmode)
def filewriter()'''
def filecreator():
    while(1):
        userinput=input('Would you like to create a new file?(Yes/No)')
        if userinput=="Yes" or userinput="yes":
            file_c_indicator=1
            break
        elif userinput=="No" or userinput="no":
            file_c_indicator=0
            break
        else:
            print("Please input Yes or No")
    
##help():open a file and output all guts it have
def exception_handle(ok):
   print("I'm sorry, but there is a problem: ",ok)
def argument_length_check(arg):
    arglength=len(arg)
    if arglength!=3:
        exception_handle("Parameter Error")
        #help()
        exit()
    pass
a=sys.argv
argument_length_check(a)
