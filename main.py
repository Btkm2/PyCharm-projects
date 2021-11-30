import hashlib
from account import *

result = hashlib.md5(b"Hello MD5").hexdigest()
print(result)

result = hashlib.md5("Hello MD5".encode("utf-8")).hexdigest()
print(result)

m = hashlib.md5(b"Hello MD5")
print(m.name)
print(m.digest_size) # 16 bytes (128 bits)
print(m.digest())    # bytes
print(m.hexdigest()) # bytes in hex representation


"""login = input("Enter your login: ")
password = input("Enter your password: ")
another_pass = input("2ns pass: ")
enc_pass = hashlib.md5(password.encode()).hexdigest()
scn_enc = hashlib.md5(another_pass.encode()).hexdigest()
print("Your login: ",login)
print("Entered version of your password is: ",password," and the encoded version: ",enc_pass)
print("2ns encoded pass: ",scn_enc)
print(enc_pass.__contains__(scn_enc))"""

list_acc = []
while(True):
    print("|-----MAIN PAGE-----|")
    print("Press [1] to register")
    print("Press [2] to authorize")
    print("Press [3] to exit the program")
    usr_choice = int(input())
    if(usr_choice == 1):
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        print("Press [1] to encode pass in md5")
        print("Press [2] to encode pass in sha256")
        print("Press [3] to encode pass in sha3")
        enc_choice = int(input())
        if(enc_choice == 1):
            enc_pass = hashlib.md5(password.encode()).hexdigest()
            list_acc.append(account(login, enc_pass))
        elif(enc_choice == 2):
            sha_pass = hashlib.sha256(password.encode()).hexdigest()
            list_acc.append(account(login, sha_pass))
        elif(enc_choice == 3):
            sha3_pass = hashlib.sha3_256(password.encode()).hexdigest()
            list_acc.append(account(login, sha3_pass))
    elif(usr_choice == 2):
        check_login = input("Enter login to check: ")
        check_pass = input("Enter password to check: ")
        print("Press [1] to encode pass in md5")
        print("Press [2] to encode pass in sha256")
        print("Press [3] to encode pass in sha3")
        check_choice = int(input())
        if(check_choice == 1):
            new_enc = hashlib.md5(check_pass.encode()).hexdigest()
            for i in range(len(list_acc)):
                if (list_acc[i].get_pass() == new_enc and list_acc[i].get_login() == check_login):
                    print("Your successfully entered to your account!")
                else:
                    print("Something went wrong, please re-check your login or password")
        elif(check_choice == 2):
            new_sha = hashlib.sha256(check_pass.encode()).hexdigest()
            for i in range(len(list_acc)):
                if (list_acc[i].get_pass() == new_sha and list_acc[i].get_login() == check_login):
                    print("Your successfully entered to your account!")
                else:
                    print("Something went wrong, please re-check your login or password")
        elif(check_choice == 3):
            new_sha3 = hashlib.sha3_256(check_pass.encode()).hexdigest()
            for i in range(len(list_acc)):
                if (list_acc[i].get_pass() == new_sha3 and list_acc[i].get_login() == check_login):
                    print("Your successfully entered to your account!")
                else:
                    print("Something went wrong, please re-check your login or password")
    elif(usr_choice == 3):
        break



"""import tkinter as tk
from account import *

master = tk.Tk()
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def fill_doc():
    added_accs = []
    open('listfile.txt', 'a')
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)

    acc_list = []
    for i in range(len(added_accs)):
        if(not added_accs.__contains__(e1.get())):
            acc_list.append(account(e1.get(),e2.get()))
            print("see")
            break
        else:
            print("Error, you've entered login that already exists!!")
            break

    with open('listfile.txt', 'a') as filehandle:
        for listitem in acc_list:
            filehandle.write('%s\n' % listitem.get_login())
            filehandle.write('%s\n' % listitem.get_pass())


def check_doc():
    #f = open("textfile.txt", "a")
    #acc_lists = []
    added_accs = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)

    if(added_accs.__contains__(e1.get()) and added_accs.__contains__(e2.get())):
        T = tk.Text(master, height=5, width=52)
        T.insert(tk.END, "You've successfully entered your account!")
    #log = e1.get()
    #passwrd = str(e2.get())
    #f.write(log)
    #f.write("\n")
    #f.write(passwrd)
    #f.close()
#master = tk.Tk()
tk.Label(master, text="Login").grid(row=0)
tk.Label(master, text="Password").grid(row=1)
#T = tk.Text(master,height = 5, width = 52)
#T.insert(tk.END,"You've successfully entered your account!")

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Login',
          command=check_doc).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Register', command=fill_doc).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)


master.mainloop()
"""