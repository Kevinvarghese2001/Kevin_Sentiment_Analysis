import mysql.connector
from tkinter import *
from tkinter import messagebox

from Admin import AdminHome

#creating the application main window.
top = Tk()
top.geometry("600x400")
u_name = StringVar()
u_pass = StringVar()
large_font = ('Verdana', 15)
top.title("Login")

def checkuser():
    get_name = u_name.get().strip()
    get_pass = u_pass.get().strip()
    print("Name:", get_name, ",", "Password:", get_pass)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="speech"
    )
    if get_name=="" and get_pass=="":
        messagebox.showinfo("Entry","username and pass missing")
    elif get_name=="":
        messagebox.showinfo("Entry","username is blank")
    elif get_pass=="":
        messagebox.showinfo("Entry","password is blank")
    else:
        mycursor = mydb.cursor()
        sql = "SELECT * FROM login WHERE userid = %s and password=%s"
        adr = (get_name,get_pass)

        mycursor.execute(sql, adr)

        print("I am here...")
        myresult = mycursor.fetchall()
        print("Count:",mycursor.rowcount)
        if mycursor.rowcount:
            top.withdraw()
            cp=Toplevel()
            print("I am here...")
            w=AdminHome(cp)
            #adminhome()
        else:
            messagebox.showinfo("Entry","no such user")
        print("done....")

def login():
    #creating label
    uname = Label(top, text = "Username",font=large_font).place(x = 30,y = 50)
    e1 = Entry(top,width = 20,textvariable=u_name,font=large_font).place(x = 140, y = 50)

    #creating label
    password = Label(top, text = "Password",font=large_font).place(x = 30, y = 90)
    e2 = Entry(top, width = 20,textvariable=u_pass,font=large_font,show="*").place(x = 140, y = 90)
    sbmitbtn = Button(top, text="Cancel", activebackground="pink", font=large_font, activeforeground="blue", command=top.destroy).place(x=300, y=130)

    sbmitbtn = Button(top, text = "Submit",activebackground = "pink",font=large_font, activeforeground = "blue",command=checkuser).place(x = 200, y = 130)

    top.mainloop()

login()

class AdminHome:
    def __init__(self,master):
        self.master=master
        self.duration=StringVar()
        self.fpath=StringVar()
        self.lbl_text=StringVar()

        self.lbl_text.set("waiting")
        #master1 = Toplevel()
        master.title("Admin Home")
        master.state("zoomed")
        large_font = ('Verdana', 25)

        lbl_2 = Label(master, text="Duration", height=2, width=20, font=large_font).place(x=700, y=10)
        dur = Entry(master,textvariable=self.duration, width=3, font=large_font).place(x=1000, y=20)
        #dur = Entry(master, text="Select a Voice...", width=20, font=large_font).place(x=400, y=20)
        sbmitbtn = Button(master, text="RECORD VOICE", height = 2, width = 20,font=large_font,command=self.recordvoice ).place(x=700, y=75)
        lbl = Label(master, text="Select a Voice...", height=2, width=20, font=large_font).place(x=700, y=200)
        voice_emotion = Label(master,textvariable=self.lbl_text, text="Emotion...", height=2, width=20, font=large_font).place(x=100, y=200)
        txt = Entry(master,textvariable=self.fpath, width=20, font=large_font).place(x=700, y=300)
        browse = Button(master, text="Browse",  font=large_font,command=self.browsefunc).place(x=1150, y=300)
        emotion = Button(master, text="VIEW EMOTION", height=2, width=20, font=large_font,command=self.viewemotion).place(x=700, y=400)
        ext = Button(master, text="Exit", height=2, width=20, font=large_font,command=master.destroy).place(x=700, y=550)
        master.mainloop()
