import sys
import os
import configparser
# def nociter(currentmode)
# to notify user that they are writing files/databases,
# may used for nofitying users about the typ of databases or.ini files later

# You may notice that now the method for handling file names' messy
# --I will use .ini config in next ver
# And the func for checking the presence of files
# need to be caegorised in to one func, I think.

# Arg_handle: the argument handle. For detecting the length of the arguments,
# and calling necessary functions, if specified in the parameters.


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

# process_initialize: Something to do before starting the program.
# this part may be removed as I'm trying to directly induce the
# file directory by using parameters.


class process_initialize():
    def inireader(self):
        

    # read .ini files, by a standard, if exists.
    # use configparser

    def iniasker(self):
        loopindicator = True
        iniask = str(input(".ini config file not exists. Would you"
                           "like to create a new one? (y/n)"))
        while loopindicator = True:
            if iniask == 'Yes' or iniask == 'y':
                try:
                    filecreator('creesche_config.ini')
                    
            elif iniask == 'No' or iniask == 'n':
                print("As the configration file not found, "
                      "please use the software under non-config file"
                      " mode. (csche noini <filename>). Refer to helper files"
                      "for further information."
                exit()
            else:
                print("Please type either Yes/No or y/n.")

    def tempfileattacher(self):
        print("The current working directory is: ", os.getcwd())
        filename = str(input("Input the name of database: (.txt)"))
        # currently support txt files only, may change to sqlite
        return filename
        pass
    # 'attach' files, if the .ini file DNE, unless user specified.


# file_operation: Hand over requests and write or read data
# according to the requests.

class config():
    def ini_config(self,filename):


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


# filecheck: To check the validity of the files. Currently it has little use.


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
# filecreator: To create files directly in the program.
# It need to be improved and adapted.


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
database_name=pros.tempfileattacher()
filereader(database_name)'''