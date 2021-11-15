# Main menu - login, register, or quit program
def main():
    while (True):
        print("\n======= MENU =======")
        print("1 - Log In")
        print("2 - Register")
        print("0 - Quit\n")
        choice = int(input("Choice: "))

        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 0:
            print("\nEnd of Program\n")
            quit()
        else:
            print("\nInvalid Choice!")


# Register new user
def register():

    print("\n===== REGISTER =====")
    isSuccessful = False
    attempt = 3

    while (attempt != 0 and isSuccessful == False):

        # Get a valid username
        username = None
        while (True):
            username = input("Enter new username    : ")
            if (username == "-1"):
                return # Abort

            if (doesUsernameExist(username)):
                print("Username has been taken! Choose another one.\n")
            else:
                break

        # Get two passwords that match
        password = input("Enter new password    : ")
        if (password == "-1"):
            return # Abort
        re_password = input("Re-enter new password : ")
        if (re_password == "-1"):
            return # Abort

        if (password == re_password):
            isSuccessful = True
        else:
            print("Passwords mistmatched!\n")
            attempt = attempt - 1
    
    if (isSuccessful and addNewUser(username, password)):
        print("\nRegister successful! Proceed to login.")
        login()
    else :
        print("\nRegister failed!")


# Add new user
def addNewUser(username, password):
    try:
        fileR = open("users.txt")
        currentID = 1
        for line in fileR:
            line = line.rstrip()
            currentID  = currentID + 1
        fileR.close()

        fileW = open("users.txt", "a")
        fileW.write("\n" + str(currentID) + "," + username + "," + password)
        fileW.close()
        return True
    except:
        return False

# Handle user login 
def login():

    print("\n======= LOGIN =======")
    isSuccessful = False
    attempt = 3

    while (attempt != 0 and isSuccessful == False):

        # Get an existing username
        while (True):
            username = input("Enter username : ")
            if (username == "-1"):
                return # Abort

            if (doesUsernameExist(username)):
                break
            else:
                print("Username does not exist! Please retype.\n")

        # Get password
        password = input("Enter password : ")
        if (password == "-1"):
            return # Abort

        # Validate user
        if (validateUser(username, password)):
            isSuccessful = True
        else:
            print("Username and Password Mismatched!\n")
            attempt = attempt - 1
        
    if (isSuccessful):
        print("\nLogin Successful!")
    else:
        print("\nLogin Failed! Account is Locked.")


# Return True if username and password are valid, otherwise False
def validateUser(username, password):
    try:
        file = open("users.txt")
    except:
        print("\nSomething went wrong. :(")
        return False

    isValid = False
    for line in file:
        line = line.rstrip() # Strips newline
        tokens = line.split(',')        
        if (username == tokens[1] and password == tokens[2]):
            isValid = True
            break
    
    file.close()
    return isValid
        

# Return True if username exists, otherwise False
def doesUsernameExist(username):
    try:
        file = open("users.txt")
    except:
        print("\nSomething went wrong. :(")
        return False

    isFound = False
    for line in file:
        line = line.rstrip() # Strips newline
        tokens = line.split(',')        
        if (username == tokens[1]):
            isFound = True
            break
    
    file.close()
    return isFound

# Start Program
main()
