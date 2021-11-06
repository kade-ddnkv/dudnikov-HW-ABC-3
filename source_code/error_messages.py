# Файл содержит методы для вывода сообщений о некорректных данных на этапе запуска программы.
#----------------------------------------------
def help():
    print("Two options of starting program:\n" + 
        "Input data from file:\n" + 
        "    command -f infile outfile\n" + 
        "Generate random data:\n" + 
        "    command -r number(from 1 to 10000) realistic_random(1 or 0) outfile")

def err_message_incorrect_command():
    print("Incorrect command line!\n" + 
        "Expected:\n" + 
        "    command -f infile outfile\n" + 
        "Or:\n" + 
        "    command -r number(from 1 to 10000) realistic_random(1 or 0) outfile")

def err_message_incorrect_number():
    print("Incorrect number!\n" + 
        "Set number from 1 to 10000.")

def err_message_incorrect_realistic_random():
    print("Incorrect boolean value!\n" + 
        "Set realistic_random qualifier to 1 or 0.")