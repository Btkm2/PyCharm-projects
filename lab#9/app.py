from tkinter import *
import hashlib
import account
from mail import *

master = Tk()

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def fill_doc():
    acc_list = []
    added_accs = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)

    new_enc = hashlib.md5(e2.get().encode()).hexdigest()
    for i in range(len(added_accs)):
        if(not added_accs.__contains__(e1.get())):
            acc_list.append(account.account(e1.get(), new_enc , e5.get()))
            msg = Message(master, text="Success,created account!").grid(row=7, column=0,sticky=W, pady=4)
            send_mail(e5.get(),e1.get())
            break
        else:
            #print("Error, you've entered login that already exists!!")
            msg = Message(master, text="").grid(row=7, column=0,sticky=W, pady=4)
            msg = Message(master, text="Error, you've entered login or email address that already exists!!").grid(row=7, column=0,sticky=W, pady=4)
            break

    with open('listfile.txt', 'a') as filehandle:
        for listitem in acc_list:
            filehandle.write('%s\n' % listitem.get_login())
            filehandle.write('%s\n' % listitem.get_pass())
            filehandle.write('%s\n' % listitem.get_email())

def check_doc():
    #f = open("textfile.txt", "a")
    acc_list = []
    added_accs = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
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
            msg = Message(master, text="").grid(row=7, column=0,sticky=W, pady=4)
            msg = Message(master, text="You've successfully entered into your account!").grid(row=7,column=0,sticky=W,pady=4)

            #msg.pack()
            break
        else:
            #print("Error, you've entered login that already exists!!")
            msg = Message(master, text="").grid(row=7, column=0,sticky=W, pady=4)
            msg = Message(master, text="Error, something goes wrong, please check login or password that you've entered").grid(row=7,sticky=W, pady=4)
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
def log_btn(lojin,passwors,text):
    # f = open("textfile.txt", "a")
    acc_list = []
    added_accs = []
    # open file and read the content in a list
    with open('listfile.txt', 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentacc = line[:-1]

            # add item to the list
            added_accs.append(currentacc)
    enc_pass = hashlib.md5(passwors.get().encode()).hexdigest()
    message_check = "Hey {}.".format(lojin.get())
    print("msg",message_check)
    print("doesn't work")
    names = lojin.get()
    print(names)
    print("text itself->",text.get())
    for i in range(len(added_accs)):
        if (added_accs.__contains__(lojin.get()) and added_accs.__contains__(enc_pass) and message_check.__contains__(text.get())):
            # msg = Message(master, text="").grid(row=7, column=0, sticky=W, pady=4)
            Message(master, text="You've successfully nnnn entered into your account!").grid(row=7, column=0, sticky=W, pady=4)
            break
        else:
            Message(master,text="Error, something goes wrong, please check login or password that you've entered").grid(row=7, sticky=W, pady=4)
            break

def login():

    log_login = Label(master, text="Login")
    log_pass = Label(master, text="Password")
    log_message = Label(master, text="Message")
    log_login.grid(row=0)
    log_pass.grid(row=1)
    log_message.grid(row=2)
    log_login_entry= Entry(master)
    log_pass_entry = Entry(master, show="*")
    log_message_entry = Entry(master)

    log_login_entry.grid(row=0,column=1)
    log_pass_entry.grid(row=1,column=1)
    log_message_entry.grid(row=2,column=1)

    btn_for_login = Button(master,text='acc',command=lambda :log_btn(log_login_entry,log_pass_entry,log_message_entry))
    btn_for_login.grid(row=6,column=0,sticky=W,pady=4)


def hide_labels():
    e1.grid_remove()
    e2.grid_remove()
    e3.grid_remove()
    e4.grid_remove()
    e5.grid_remove()
    e6.grid_remove()
    log.grid_remove()
    password.grid_remove()
    fname.grid_remove()
    lname.grid_remove()
    phone.grid_remove()
    e_mail.grid_remove()
    log_in.grid_remove()


log = Label(master, text="Login")
password = Label(master, text="Password")
fname = Label(master, text="First name")
lname = Label(master, text="Last name")
e_mail = Label(master, text="Email")
phone = Label(master, text="Phone")
# log_message = Label(master, text="Rermove")
""".grid(row=4)"""

log.grid(row=0)
password.grid(row=1)
fname.grid(row=2)
lname.grid(row=3)
e_mail.grid(row=4)
phone.grid(row=5)
# log_message.grid(row=2)
# log_message.pack_forget()

e1 = Entry(master)
e2 = Entry(master,show="*")
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
# N

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
# message.grid(row=2, column=1)
# message.pack_forget()


log_in = Button(master,
          text='Login',
          command=check_doc)
log_in.grid(row=6,column=0,sticky=W,pady=4)
Button(master,text='Register', command=fill_doc).grid(row=6,column=1,sticky=W,pady=4)

Button(master,text='Log into account', command=lambda:[login(), hide_labels()]).grid(row=6,column=2,sticky=W,pady=4)



master.mainloop()
