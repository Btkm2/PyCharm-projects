import tkinter as tk
import hashlib
from account import *

master = tk.Tk()

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def fill_doc():
    acc_list = []
    added_accs = []
    # open file and read the content in a list
    with open('lab#9/listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)

    new_enc = hashlib.md5(e2.get().encode()).hexdigest()
    for i in range(len(added_accs)):
        if(not added_accs.__contains__(e1.get())):
            acc_list.append(account(e1.get(),new_enc))
            msg = tk.Message(master, text="Success,created account!").grid(row=4, column=0,sticky=tk.W, pady=4)
            break
        else:
            #print("Error, you've entered login that already exists!!")
            msg = tk.Message(master, text="").grid(row=4, column=0,sticky=tk.W, pady=4)
            msg = tk.Message(master, text="Error, you've entered login that already exists!!").grid(row=4, column=0,sticky=tk.W, pady=4)
            break

    with open('lab#9/listfile.txt', 'a') as filehandle:
        for listitem in acc_list:
            filehandle.write('%s\n' % listitem.get_login())
            filehandle.write('%s\n' % listitem.get_pass())

def check_doc():
    #f = open("textfile.txt", "a")
    acc_list = []
    added_accs = []
    # open file and read the content in a list
    with open('lab#9/listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)
    enc_pass = hashlib.md5(e2.get().encode()).hexdigest()
    for i in range(len(added_accs)):
        if(added_accs.__contains__(e1.get()) and added_accs.__contains__(enc_pass)):
            #T = tk.Text(master,height = 5, width = 52).grid(row=4,column=0,sticky=tk.W,pady=4)
            #T.insert(tk.END,"You've successfully entered into your account!")
            msg = tk.Message(master, text="").grid(row=4, column=0,sticky=tk.W, pady=4)
            msg = tk.Message(master, text="You've successfully entered into your account!").grid(row=4,column=0,sticky=tk.W,pady=4)

            #msg.pack()
            break
        else:
            #print("Error, you've entered login that already exists!!")
            msg = tk.Message(master, text="").grid(row=4, column=0,sticky=tk.W, pady=4)
            msg = tk.Message(master, text="Error, something goes wrong, please check login or password that you've entered").grid(row=4,sticky=tk.W, pady=4)
            break

    """with open('listfile.txt', 'a') as filehandle:
        for listitem in acc_list:
            filehandle.write('%s\n' % listitem.get_login())
            filehandle.write('%s\n' % listitem.get_pass())"""
    #log = e1.get()
    #passwrd = str(e2.get())
    #f.write(log)
    #f.write("\n")
    #f.write(passwrd)
    #f.close()
#master = tk.Tk()
tk.Label(master, text="Login").grid(row=0)
tk.Label(master, text="Password").grid(row=1)

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
