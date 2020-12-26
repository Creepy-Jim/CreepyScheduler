import sys,os
##def nociter(currentmode)## to notify user that they are writing files/databases, may used for nofitying users about the type of databases or.ini files in the future ##
def filereader(filename):
    fileread=open(filename,"r")
    for counter in fileread:
        print(counter.strip())
    fileread.close()
##def filewriter()
def fileattacher():##'attach' files
    print("The current working directory is: ",os.getcwd())
    filename=str(input("Input the name of database you would like to attach: (.txt)"))##currently support txt files only, may change to sqlite
    return filename
def filecreator():##Create file if certain files not found and if user necessary:
    while(1):
        userinput=input('Would you like to create a new file?(Yes/No)')
        if userinput=="Yes" or userinput=="yes":
            file_c_indicator=1
            break
        elif userinput=="No" or userinput=="no":
            file_c_indicator=0
            break
        else:
            print("Please input Yes or No")
    if file_c_indicator==1:
        try:
            filename=str(input("Input the name of the file: "))
            filecreate=open("x",filename)
            print("File",filename,"created.")
            filecreate.close()
        except:
            exception_handle(sys.exc_info[0])
    else:
        print("The file will not be created.")
    pass
    
##help():open a file and output all guts it have
def exception_handle(ok):
    print("I'm sorry, but there is a problem: ",ok)
    pass
def argument_length_check(arg):
    arglength=len(arg)
    if arglength!=3:
        exception_handle("Parameter Error, see if the following helps: \n")
        #help()
        exit()
    pass


'''a=sys.argv
argument_length_check(a)'''
database_name=fileattacher()
filereader(database_name)