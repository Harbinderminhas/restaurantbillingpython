from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *

from kitchenscreen1 import *
from mainmenu import *



class login:




    def log(self):
        self.username = self.usernambox.get().strip()
        self.password = self.passwrdbox.get().strip()
        position=self.combobox.get()
        print(self.username)
        print(self.password)
        if len(self.username) < 1:
            showinfo("MESSAGEBOX", "PLEASE FILL THE USERNAME")
        elif len(self.password) < 1:
            showinfo("MESSAGEBOX", "PLEASE FILL THE PASSWORD")
        elif position=="":
            showinfo('','select position')
        else:
            cur = con.cursor()
            query = "select * from staff where email='" + self.username + "' and password='" + self.password + "' and type='"+str(position)+"'"
            print(query)
            n=cur.execute(query)
            self.data = cur.fetchone()
            print("QUERY data FETCH!!!!!")
            print(self.data)
            if n>0:
                if position == "KITCHEN":
                    obj = kitchenscreen1()
                    self.window.geometry("1200x700")
                else:
                    obj = mainWindow(self.username, self.password)
            else:
                showinfo('','invalid credentials')










    def __init__(self):
        self.window = Tk()
        self.window.title("LOGIN PAGE")

        self.window.geometry("1200x700")

        self.window.iconbitmap("sign.ico")

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")


        self.username = Label(self.window, text="USERNAME", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.password = Label(self.window, text="PASSWORD", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.select = Label(self.window, text="SELECT POSITION", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.usernambox = Entry(self.window)
        self.passwrdbox = Entry(self.window, show="*")

        self.button = Button(self.window, text="LOGIN", command=self.log)
        self.combobox = Combobox(self.window, values=["KITCHEN", "CASHIER"], state="readonly")

        self.username.grid(row=0, column=0)
        self.password.grid(row=1, column=0)

        self.usernambox.grid(row=0, column=1)
        self.passwrdbox.grid(row=1, column=1)

        self.button.grid(row=3, column=1)

        self.combobox.grid(row=2, column=1)

        self.select.grid(row=2,column=0)

        self.window.mainloop()



if __name__ == '__main__':
    obj = login()