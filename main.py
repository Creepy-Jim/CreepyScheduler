import sys
import os
# def nociter(currentmode)
# to notify user that they are writing files/databases,
# may used for nofitying users about the typ of databases or.ini files later

# You may notice that now the method for handling file names' messy
# --I will use .ini config in next ver
# And the func for checking the presence of files
# need to be caegorised in to one func, I think.


class arg_handle():
    def arg_err(self, arg):
        arglength = len(arg)
        if arglength == 1:
            print("Parameter Error, see if the following helps: \n")
            help()
            exit()
        pass

    def argchecker(self, arg):
        print(arg)
        if arg == 'help':
            help()
        elif arg == 'form':
            help()


class process_initialize():
    def fileattacher(self):  # 'attach' files
        print("The current working directory is: ", os.getcwd())
        filename = str(input("Input the name of database: (.txt)"))
        # currently support txt files only, may change to sqlite
        return filename
        pass


class file_operation():
    def filereader(self, filename):
        print("reading files")
        fileread = open(filename, "r")
        for counter in fileread:
            print(counter.strip())
        fileread.close()

    def filewriter(self, filename, operation_name):
        filewrite = open(filename, "a")
        print("Writing ")
        filewrite.close()


class filecheck():
    def filelengthchecker(self, filename):
        try:
            file_oper.fileread = open(filename, "r")
        except(Exception):
            exc.exception_handle(sys.exc_info[0])


def filecreator():  # Create file if user necessary:
    while(1):
        userinput = input('Would you like to create a new file?(Yes/No)')
        if userinput == "Yes" or userinput == "yes":
            file_c_indicator = 1
            break
        elif userinput == "No" or userinput == "no":
            file_c_indicator = 0
            break
        else:
            print("Please input Yes or No")
    if file_c_indicator == 1:
        try:
            filename = str(input("Input the name of the file: "))
            filecreate = open("x", filename)
            print("File", filename, "created.")
            filecreate.close()
        except(Exception):
            exc_pros.exception_handle(sys.exc_info)
    else:
        print("The file will not be created.")
    pass


def help():
    try:
        file_oper.filereader("help.txt")
        print("reading files")
    except(Exception):
        exc_pros.exception_handle(sys.exc_info)
# open a file and output all guts it have


class exc():
    def exception_handle(self, exc_code):
        print("I'm sorry, but there is a problem: ", exc_code)
        exit()


# Defining for each function
arg = sys.argv
arg_oper = arg_handle()
file_oper = file_operation()
# pros=process_initialize()
exc_pros = exc()


arg_oper.argchecker(arg)
arg_oper.argchecker(arg[1])
'''
database_name=pros.fileattacher()
filereader(database_name)'''
