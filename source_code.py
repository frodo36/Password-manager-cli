from random import choice
from time import sleep
from pyperclip import copy
from os import name
from os import path
from os import system
from os import getlogin
from os import makedirs
from pickle import load
from pickle import dump
from string import ascii_letters
from string import ascii_uppercase
from string import digits
from pwinput import pwinput
from cryptography.fernet import Fernet
import platform
from termcolor import colored
from base64 import b64encode
from base64 import b64decode

#function to clear terminal
def clear():
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

if not platform.system() == "Windows":
    print("Sorry man, I am too lazy to add support for Linux and Mac :/ \n")
    input("Press any key to exit... \n")
    quit()

#define folder and file paths in variables
folder_path = f"C:/Users/{getlogin()}/password manager"
entries_path = f"C:/Users/{getlogin()}/password manager/entries.txt"
lock_path = f"C:/Users/{getlogin()}/password manager/lock.txt"
user_path = f"C:/Users/{getlogin()}/password manager/user.txt"
key_path = f"C:/Users/{getlogin()}/password manager/key.txt"
log_path = f"C:/Users/{getlogin()}/password manager/log.txt"

#creating required files if necessary
if not path.exists(folder_path):
    makedirs(folder_path)
    print("Creating file directoy...")
    print(f"File directory created at {folder_path}")
    sleep(0.5)
    sleep(0.5)
if not path.exists(key_path):
    open(key_path, "x")
    print("Creating keyfile...")
    sleep(0.5)
    print(f"Created keyfile at {key_path}")
if not path.exists(lock_path):
    open(lock_path, "x")
if not path.exists(user_path):
    open(user_path, "x")
if not path.exists(entries_path):
    open(entries_path, "x")
if not path.exists(log_path):
    open(log_path, "x")
    print("Creating  additional files...")
    sleep(0.5)
#loading encryption key into file if file is empty
if path.getsize(key_path) == 0:
    key = Fernet.generate_key()
    key = b64encode(key)
    with open(key_path, "bw") as x:
        dump(key, x)
else:
#loading encryption key from file
    with open(key_path, "br") as x:
        key = load(x)
key = b64decode(key)
f = Fernet(key)

#password strenth checking function
def checker():
    clear()
    special = ["!", "?", "@", "#", ".", ",", "$", "%", "&", "/", "(", ")", "[", "]", "+", "-", "*", "_", "'", "ä", "ö", "ü", "ß", "§", "{", "}"]

    points = 0
    user = input("\nPlease enter a pasword you would like to check:\n")
    if len(user) > 7:
        points += 3
    elif len(user) > 15:
        points += 5
    else:
        points -= 3
    if dict.check(user) == True:
        points -= 3
    digits_count = 0
    special_count = 0
    letters_count = 0
    for x in user:
        if x in special:
           points += 1
        if x in digits:
            points += 1
        if x in ascii_uppercase:
            points += 1
        if not x in digits:
            digits_count += 1
        if not x in special:
            special_count += 1
        if not x in ascii_uppercase:
            letters_count+= 1
    if digits_count == len(user):
        points -= 1
    if special_count == len(user):
        points -= 1
    if letters_count == len(user):
        points -= 1
    print("\nCalculating...\n")
    sleep(1)
    if points < 0:
        print(f"Your password '{user}' is extremely weak") 
    elif points < 5:
       print(f"Your password '{user}' is not strong")
    elif points < 11:
        print(f"Your password '{user}' is alright")
    elif points < 14:
        print(f"Your password '{user}' is decent")
    elif points < 16:
        print(f"Your password '{user}' is strong")
    elif points < 21:
        print(f"Your password '{user}' is very strong")
    else:
        print(f"Your password '{user}' is invincible")
    print("\nWould you like to check another password?")
    print("Yes")
    print("No")
    input_check = ["yes", "no"]
    user = input()
    while not user in input_check:
        print("Invalid input")
        print("\nWould you like to check another password?")
        print("Yes")
        print("No")
        user = input()
    if user.lower() == "yes":
        checker()
    elif user.lower() == "no":
        input("\nPress any key to return to the menu...")
    
def checker2(user):
    special = ["!", "?", "@", "#", ".", ",", "$", "%", "&", "/", "(", ")", "[", "]", "+", "-", "*", "_", "'", "ä", "ö", "ü", "ß", "§", "{", "}"]

    points = 0
    if len(user) > 7:
        points += 3
    elif len(user) > 15:
        points += 5
    else:
        points -= 3

    digits_count = 0
    special_count = 0
    letters_count = 0
    for x in user:
        if x in special:
            points += 1
        if x in digits:
            points += 1
        if x in ascii_uppercase:
            points += 1
        if not x in digits:
            digits_count += 1
        if not x in special:
            special_count += 1
        if not x in ascii_uppercase:
            letters_count+= 1
    if digits_count == len(user):
        points -= 1
    if special_count == len(user):
        points -= 1
    if letters_count == len(user):
        points -= 1
    if points < 0:
        print(f"Your password is extremely weak")
    elif points < 5:
       print(f"Your password is not strong")
    elif points < 11:
        print(f"Your password is alright")
    elif points < 14:
        print(f"Your password is decent")
    elif points < 16:
        print(f"Your password is strong")
    elif points < 21:
        print(f"Your password is very strong")
    elif points < 26:
        print(f"Your password is invincible")
    print("\nWould you like to use a different password?")
    print("Yes")
    print("No")
    input_check = ["yes", "no"]
    user = input()
    while not user in input_check:
        print("Invalid input")
        print("\nWould you like to use a different password?")
        print("Yes")
        print("No")
        user = input()
    if user.lower() == "yes":
        print("")
        print("NOTE: Remeber this passsword well, becasue you CAN'T RECOVER IT!")
        print("Please enter a master password:")
        password = pwinput("")
        print("Please re-enter your password:")
        password2 = pwinput("")
        while not password2 == password:
            print("Passwords don't match!")
            print("Please enter a master password:")
            password = pwinput("")
            print("Please re-enter your password:")
            password2 = pwinput("")
        checker2(password)

    elif user.lower() == "no":
        pass
    
def checker3(user):
    special = ["!", "?", "@", "#", ".", ",", "$", "%", "&", "/", "(", ")", "[", "]", "+", "-", "*", "_", "'", "ä", "ö", "ü", "ß", "§", "{", "}"]

    points = 0
    if len(user) > 7:
        points += 3
    elif len(user) > 15:
        points += 5
    else:
        points -= 3

    digits_count = 0
    special_count = 0
    letters_count = 0
    for x in user:
        if x in special:
            points += 1
        if x in digits:
            points += 1
        if x in ascii_uppercase:
            points += 1
        if not x in digits:
            digits_count += 1
        if not x in special:
            special_count += 1
        if not x in ascii_uppercase:
            letters_count+= 1
    if digits_count == len(user):
        points -= 1
    if special_count == len(user):
        points -= 1
    if letters_count == len(user):
        points -= 1
    return points

#(not so) simple password generator
def generate():
    def gen(user):
        password = ""
        special = "!?#*+-/&%$§"
        chars = ascii_letters + digits + special
        count = 0
        while not count == user:
             password += choice(chars)
             count += 1
        return password
            
    user_list = []
    print("How many characters long do you want your password to be?")
    print("(Recommended password length is 20 characters)")
    user = input()
    is_integer = True
    for x in user:
        user_list.append(x)
    for x in user_list:
        if not x in digits:
            is_integer = False
    user_list = []
    while is_integer == False:
        is_integer = True
        print("\nInvalid input")
        print("How many characters long do you want your password to be?")
        user = input()
        for x in user:
            user_list.append(x)
        for x in user_list:
            if not x in digits:
                is_integer = False
        user_list = []
    user = int(user)
    password = gen(user)
    if len(password) > 15:
        check = checker3(password)
        while not check > 15:
            password = gen(user)
            check = checker3(password)
    print(password)
    return password

def generate2():
    def gen(user):
        password = ""
        special = "!?#*+-/&%$§"
        chars = ascii_letters + digits + special
        count = 0
        while not count == user:
             password += choice(chars)
             count += 1
        return password
            
    user_list = []
    print("How many characters long do you want your password to be?")
    print("(Recommended password length is 20 characters)")
    user = input()
    while int(user) > 50:
        print("Password can not be longer then 50 characters\n")
        print("How many characters long do you want your password to be?")
        print("(Recommended password length is 20 characters)")
        user = input()

    is_integer = True
    for x in user:
        user_list.append(x)
    for x in user_list:
        if not x in digits:
            is_integer = False
    user_list = []
    while is_integer == False:
        is_integer = True
        print("\nInvalid input")
        print("How many characters long do you want your password to be?")
        user = input()
        for x in user:
            user_list.append(x)
        for x in user_list:
            if not x in digits:
                is_integer = False
        user_list = []
    user = int(user)
    password = gen(user)
    if len(password) > 15:
        check = checker3(password)
        while not check > 15:
            password = gen(user)
            check = checker3(password)
    print(password)
    copy(password)
    sleep(0.5)
    print("Your password has been copied\n")
    input_check = ["yes", "no"]
    print("Would you like to generate a new password?")
    print("Yes")
    print("No")
    user = input()
    while not user in input_check:
        print("Invalid input")
        print("\nWould you like to generate a new password?")
        print("Yes")
        print("No")
        user = input()
    if user.lower() == "yes":
        clear()
        generate2()
    elif user.lower() == "no":
        input("Press any key to return to the menu...")
    
    return password

#shows list of commands
#triggers "password_generator" function if requested
def start():
    with open(key_path, "br") as x:
        key = load(x)
    key = b64decode(key)
    f = Fernet(key)
    
    if not path.getsize(log_path) == 0:
        print("Password manager has detected an attempt to steal your data")
        print("For security reasons password manager has deleted your entries")
        file = open(log_path, "w")
        file.close()
     
    #loading entries from file and creating empty variable if file is empty
    if not path.getsize(entries_path) == 0:
        with open(entries_path, "br") as x:
            entries = load(x)
    else:
        entries = []
    
    print("\n'n' -Create a new entry'")
    print("'e' -Edit an entry'")
    print("'d' -Delete an entry'")
    print("'g' -Generate a strong password'")
    print("'c' -Check a passwords strength'")
    print("'x' -Log out'")
    print("\nChoose an action:")
    user = input()
    if user.lower() == "c":
        checker()
        display()
        start()
    elif user.lower() == "g":
        clear()
        generate2()
        display()
        start()
    elif user.lower() == "x":
        print("Encrypting data...")
        sleep(0.5)
        print("logging out...")
        sleep(1)
        clear()
        lock()
    elif user.lower() == "n":
        clear()
        #creates new entries and stores them in "entries" list
        print("Please enter a name for your new entry:")
        a = input()
        check = []
        for x in entries:
            x = f.decrypt(x)
            x = x.decode()
            check.append(x)
        check_place = 1
        for x in check:
                check.pop(check_place)
                check.pop(check_place)
                check_place += 1
        while a in check:
            print("An entry with this name already exists")
            print("Please enter a name for your entry:")
            a = input()
        name = a
        print("Please enter an E-mail address for your new entry:")
        mail = input()
        print("Please input a password for your new entry")
        print("'g' -Generate a strong password with password manager'")
        print("'m' -Manually enter a password'")
        print("\nChoose an action:")
        user = input()
        check_input = ["g", "m"]
        while not user in check_input:
            print("Invalid input\n")
            print("Please input a password for your new entry")
            print("'g' -Generate a strong password with password manager'")
            print("'m' -Manually enter a password'")
            print("\nChoose an action:")
            user = input()
        if user.lower() == "m":
            print("Input a password:")
            password = input()
        elif user.lower() == "g":
            password = generate()
        #encrypting and storing variables
        name = name.encode()
        name = f.encrypt(name)
        mail = mail.encode()
        mail = f.encrypt(mail)
        password = password.encode()
        password = f.encrypt(password)
        entries.append(name)
        entries.append(mail)
        entries.append(password)
        with open(entries_path, "bw") as x:
            dump(entries, x)
        print("New entry created successfully! \n")
        input("Press any key to return to the menu...")
        display()
        start()
    elif user.lower() == "e":
        clear()
        #edits items in 'entries' list
        display()
        print("Please enter the name of the entry that you want to edit:")
        var = input()
        check = []
        entries2 = []
        for x in entries:
            x = f.decrypt(x)
            x = x.decode()
            check.append(x)
            entries2.append(x)
        check_place = 1
        for x in check:
            check.pop(check_place)
            check.pop(check_place)
            check_place += 1
        while not var in check:
            print("Specified entry does not exist")
            start()
        place = entries2.index(var)
        print(f"Editing entry '{var}'")
        del var
        #replacing, encrypting and storing new variables
        print("Please enter a new name for your entry:")
        var = input()
        entries[place] = var
        entries[place] = entries[place].encode()
        entries[place] = f.encrypt(entries[place])
        print("Please enter a new E-mail for your entry:")
        entries[place + 1] = input()
        entries[place + 1] = entries[place + 1].encode()
        entries[place + 1] = f.encrypt(entries[place + 1])
        print("Please input a password for your new entry")
        print("'g' -Generate a strong password with password manager'")
        print("'m' -Manually enter a password'")
        print("\nChoose an action:")
        user = input()
        check_input = ["g", "m"]
        while not user in check_input:
            print("Invalid input\n")
            print("Please input a password for your new entry")
            print("'g' -Generate a strong password with password manager'")
            print("'m' -Manually enter a password'")
            print("\nChoose an action:")
            user = input()
        if user.lower() == "m":
            print("Input a password:")
            password = input()
        elif user.lower() == "g":
            password = generate()
        entries[place + 2] = password
        entries[place + 2] = entries[place +2].encode()
        entries[place + 2] = f.encrypt(entries[place + 2])
        with open(entries_path, "bw") as x:
            dump(entries, x)
        print("Entry edited successfully! \n")
        del var
        del place
        input("Press any key to return to the menu...")
        display()
        start()
    elif user.lower() == "d":
        clear()
        #deletes items in 'entries' list
        display()
        print("Please enter the name of the entry you want to delete:")
        print("Please seperate different entries with a comma (,)")
        var = input()
        var = var.split(",")
        var2 = []
        for a in var:
            j = a.replace(' ', '')
            var2.append(j)
        for y in var2:
            check = []
            check2 = []
            for x in entries:
                x = f.decrypt(x)
                x = x.decode()
                check.append(x)
                check2.append(x)
            place = 1
            for x in check:
                check.pop(place)
                check.pop(place)
                place += 1
            if not y in check:
                print(f"Specified entry '{y}'does not exist \n")
                input("Press any key to return to the menu...")
                display()
                start()
            place = check2.index(y)
            print("")
            print(f"Deleleting entry '{y}'...")
            sleep(1)
            entries.pop(place)
            entries.pop(place)
            entries.pop(place)
            with open(entries_path, "bw") as x:
                dump(entries, x)
            print("Entry deleted succesfully! \n")
        input("Press any key to return to the menu...")
        display()
        start()

    else:
        print("Invalid input")
        start()

#used to display items from "entries" variable
def display():
    clear()
    if not path.getsize(entries_path) == 0:
        with open(entries_path, "br") as x:
            entries = load(x)
    else:
        entries = []
    with open(user_path, "br") as x:
        name = load(x)

    name = f.decrypt(name)
    name = name.decode()
    count = 0
    name_count = 2
    print(f"Welcome {name}!")
    print("")
    if not entries:
        print("--------------------------------")
        print("You have no entries yet")
        print("--------------------------------")
    if entries:
        print("--------------------------------")
        print("Your current entries:")
        print("--------------------------------")
        for x in entries:
            x = f.decrypt(x)
            x = x.decode()
            name_count += 1
            if not name_count == 3:
                print(x)
            if name_count == 3:
                print(colored(x, "blue", attrs=["bold"]))
                name_count = 0
            count += 1
            if count == 3:
                print("--------------------------------")
                count = 0

#funtion used to unlock the password vault (starting 'start()' function)
def lock():
    clear()
    #loading password and username from files if specified files exist
    if not path.getsize(lock_path) == 0:
        with open(lock_path, "br") as x:
            password = load(x)
        with open(user_path, "br") as x:
            name = load(x)
        f = Fernet(key)
        password = f.decrypt(password)
        password = password.decode()
        name = f.decrypt(name)
        name = name.decode()  
    else:
        password = None
        name = None
    
    print("\nHi, and welcome to Password Manager! \n")
    print("'L' -Log in'")
    print("'e' -Edit profile'")
    print("'c' -Create account'")
    print("'x' -Log out")
    print("\nChoose an action:")
    var = input()
    if var.lower() == "x":
        print("Closing...")
        clear()
        quit()
    elif var.lower() == "l":
        if not path.getsize(entries_path) == 0 and path.getsize(lock_path) == 0:
            print("Password manager has detected file modifications that will compromise your saved entries!")
            print("Hence, for security reasons, password manager will not allow you to log in and reset your profile")
            input("\nPress any key to aknowlege...\n")
            print("Deleting profile data...")
            sleep(0.5)
            print("Deleting encryption keys....")
            with open(entries_path,'w') as f:
                pass
            with open(lock_path,'w') as f:
                pass
            with open(user_path,'w') as f:
                pass
            with open(key_path,'w') as f:
                pass
            with open(log_path, "bw") as x:
                dump("Data", x)
            sleep(1)
            print("All profile data deleted successfully!")
            sleep(0.5)
            print("To complete the deletetion process, the program will now be closed")
            sleep(0.5)
            print("Closing...")
            sleep(1)
            clear()
            quit()

        #verifying password and unlocking vault if password is correct
        error_count = 6
        clear()
        if not path.getsize(lock_path) == 0:
            print("Please input your master password:")
            user_input = pwinput("")
            while not user_input == password:
                error_count -= 1
                print("\nIncorrect master password!")
                print(f"You have {error_count} tries left")
                print("Please input your master password:")
                user_input = pwinput("")
                if error_count == 1:
                    print("\nYou have entered an incorrect password too many times!")
                    print("Your stored data is potentially at risk of a brute force attack")
                    print("For security reasons, your entries will be deleted")
                    file = open(entries_path, "w")
                    file.close()
                    with open(log_path, "bw") as x:
                        dump("Data", x)
                    lock()
            del user_input
            print("")
            print("Retrieving encryption key...")
            sleep(0.5)
            sleep(0.5)
            print("Decrypting data...")
            sleep(0.5)
            clear()
            print("")
            display()
            start()
                
        else:
            print("You do not have a master password yet, please create one\n")
            input("Press any key to create an account...")
            create()

    elif var.lower() == "r":
        clear()
        #clearing all files for profile reset
        print("Are you ANSOLUTELY SURE you want to reset your profile?")
        print("This will ERASE ALL YOUR ENTRIES")
        print("yes")
        print("no")
        if input().lower() == "yes":
            sleep(1)
            print("Deleting profile data...")
            sleep(0.5)
            print("Deleting encryption keys....")
            with open(entries_path,'w') as f:
                pass
            with open(lock_path,'w') as f:
                pass
            with open(user_path,'w') as f:
                pass
            with open(key_path,'w') as f:
                pass
            sleep(1)
            print("All profile data deleted successfully!")
            sleep(0.5)
            print("To complete the deletetion process, the program will now be closed")
            sleep(0.5)
            print("Closing...")
            sleep(1)
            clear()
            quit()
            
        else:
            print("Cancelling...")
            sleep(0.5)
            lock()

    elif var.lower() == "e":
        clear()
        #editing profile by replacing old file contents with new variables
        if path.exists(lock_path):
            error_count = 6
            print("Please enter your master password to edit your profile::")
            user_input = pwinput("")
            while not user_input == password:
                error_count -= 1
                print("")
                print("Incorrect master password!")
                print(f"You have {error_count} tries left")
                print("Please input your master password:")
                user_input = pwinput("")
                if error_count == 1:
                    print("")
                    print("You have entered an incorrect password too many times!")
                    print("Your stored data is potentially at risk of a brute force attack")
                    print("For security reasons, your entries will be deleted")
                    file = open(entries_path)
                    file.close()
                    with open(log_path, "bw") as x:
                        dump("Data", x)
                    lock()
            del user_input
            print("Please enter a new username:")
            username = input()
            print("Please enter a new master password:")
            password = pwinput("")
            print("Please re-enter your master password:")
            password2 = pwinput("")
            while not password2 == password:
                print("Passwords don't match!")
                print("Please enter a master password:")
                password = pwinput("")
                print("Please re-enter your password:")
                password2 = pwinput("")
            checker2(password)
            #encrypting and storing variables
            password = password.encode()
            password = f.encrypt(password)
            username = username.encode()
            username = f.encrypt(username)
            with open(lock_path, "bw") as x:
                dump(password, x,)
            with open(user_path, "bw") as x:
                dump(username, x,)
            print("Profile edited successfully!")
            print("You can log in now")
            input("\nPress any key to return to the menu...")
            lock()
        else:
            print("You haven't set a master password yet, please create one\n")
            input("Press any key to create an account")
            create()

    elif var.lower() == "c":
        clear()
        if not password:
            create()
        else:
            print("You already have a master password, please log in\n")
            input("Press any key to return to the menu...")
            lock()
    else:
        print("Invalid input\n")
        input("Press any key to return to the menu...")
        lock()
    del var

def create():
    if not path.getsize(entries_path) == 0 and path.getsize(lock_path) == 0:
        print("Password manager has detected file modifications that will compromise your saved entries!")
        print("Hence, for security reasons, password manager will not allow you to create a new user and reset your profile")
        input("\nPress any key to aknowlege...\n")
        print("Deleting profile data...")
        sleep(0.5)
        print("Deleting encryption keys....")
        with open(entries_path,'w') as f:
            pass
        with open(lock_path,'w') as f:
            pass
        with open(user_path,'w') as f:
            pass
        with open(key_path,'w') as f:
            pass
        with open(log_path, "bw") as x:
            dump("Data", x)
        sleep(1)
        print("All profile data deleted successfully!")
        sleep(0.5)
        print("To complete the deletetion process, the program will now be closed")
        sleep(0.5)
        print("Closing...")
        sleep(1)
        clear()
        quit()

    f = Fernet(key)
    #function to create a new user
    #puts all provided variables into designated files
    print("Please enter a username:")
    username = input()
    #encrypting and storing username variable
    username = username.encode()
    username = f.encrypt(username)
    with open(user_path, "bw") as x:
            dump(username, x,)
    print("")
    print("NOTE: Remeber this passsword well, becasue you CAN'T RECOVER IT!")
    print("Please enter a master password:")
    password = pwinput("")
    print("Please re-enter your password:")
    password2 = pwinput("")
    while not password2 == password:
        print("Passwords don't match!")
        print("Please enter a master password:")
        password = pwinput("")
        print("Please re-enter your password:")
        password2 = pwinput("")
    checker2(password)
    #encrypting and storing password variable
    password = password.encode()
    password = f.encrypt(password)
    with open(lock_path, "bw") as x:
            dump(password, x,)
    print("\nCreating encryption keys...")
    sleep(0.5)
    print("Encrypting profile data...")
    sleep(0.5)
    print("\nNew user created successfully!")
    print("You can log in now")
    lock()
copy('')
lock()
start()

