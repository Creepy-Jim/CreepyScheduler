import sys
import os

# You may notice that now the method for handling file names' messy
# --I will use .ini config in next ver
# And the func for checking the presence of files
# need to be categorised in to one func, I think.

# Arg_handle: the argument handle. For detecting the length of the arguments,
# and calling necessary functions, if specified in the parameters.

# In this version, your database name must be 'CDB.txt', as I'm lazy...


def arg_err(arg):
    print("Parameter Error, see if the following helps: \n")
    help()
    exit()
    pass

# May be I should refine the arg_err checker? 

def argchecker(arg):
    for counter in arg:
        if arg == 'help':
            help()
        elif arg == 'form':
            help()
        elif arg == '--dir':
            os.chdir(arg[counter+1])
#        elif arg == 'add':
#            arg[counter+1]
#        elif arg == 'finish':
#            arg[counter+1]
#        elif arg == 'list':


##file attachment
def tempfileattacher():
    print("The current working directory is: ", os.getcwd())
    # currently support txt files only, may change to sqlite
    pass

# file_operation: Hand over requests and write or read data
# according to the requests.

def filereader(filename):
    fileread = open(filename, "r")
    for counter in fileread:
        print(counter.strip())
    fileread.close()

def filewriter(filename, operation_name):
    filewrite = open(filename, "a")
    filewrite.close()

def filecreator(filename):  # Create file if user necessary:
    filecreate = open(filename, "x")
    filecreate.close()
    print("File", filename, "created.")

#    except(Exception):
#        exception_handle(sys.exc_info)
# filecreator: To create files directly in the program.

def help():
    try:
        file_oper.filereader("help.txt")
        print("reading files")
    except(Exception):
        exc_pros.exception_handle(sys.exc_info)
# open a file and output all guts it have


def exception_handle(exc_code):
    print("I'm sorry, but there is a problem: ", exc_code)
    exit()

#Major part of the program
print('Welcome to the Creepy Scheduler 0.0.1, by Jim.')
fname = "CDB.txt"
if (os.path.exists(fname)) == False:
    filecreator(fname)
tempfileattacher()
argchecker(sys.argv)