from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *

from connection import *


class changeEmail:


    def changeMailFun(self):
        if len(self.oldText.get())>1:
            if len(self.newText.get())>1:
                if self.newText.get()!=self.confirmText.get():
                    showinfo("","NEW EMAIL DOESNOT MATCH WITH CONFIRM EMAIL")
                    self.root.destroy()
                else:

                    self.newEmail = self.newText.get()
                    if self.oldEmail==self.oldText.get():


                        if len(self.newEmail) < 3:
                            showinfo("", "NEW Email MUST BE OF Atleast 3 Character")
                            self.root.destroy()
                        else:
                            cur = con.cursor()
                            query = 'update staff set  email="' + str(self.newEmail) + '"' + ' where password="' + str(
                                self.oldPassword) + '"'
                            print(query)
                            cur.execute(query)
                            con.commit()
                            showinfo("", "EMAIL CHANGED")
                            self.root.destroy()
                    else:

                      showinfo("", "OLD EMAIL WRONG!")
                      self.root.destroy()
            else:
                showinfo("","NEW EMAIL NOT ENTERED")
                self.root.destroy()

        else:
            showinfo("","OLD EMAIL EMPTY!")
            self.root.destroy()


    def __init__(self,username,password):

        #username="donald@gmail.com"

        self.root=Tk()
        self.root.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.root.iconbitmap("mail.ico")
        self.oldEmail=username
        self.oldPassword=password

        oldEmail=Label(self.root,text="OLD EMAIL", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        newEmail=Label(self.root,text="NEW EMAIL", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        confirmEmail=Label(self.root,text="CONFIRM EMAIL", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.oldText=Entry(self.root)
        self.newText=Entry(self.root)
        self.confirmText=Entry(self.root)

        changeBtn=Button(self.root,text="CHANGE",command=self.changeMailFun)


        oldEmail.grid(row=0,column=0,padx=10,pady=10)
        self.oldText.grid(row=0,column=1,padx=10,pady=10)

        newEmail.grid(row=1,column=0,padx=10,pady=10)
        self.newText.grid(row=1,column=1,padx=10,pady=10)

        confirmEmail.grid(row=2,column=0,padx=10,pady=10)
        self.confirmText.grid(row=2,column=1,padx=10,pady=10)

        changeBtn.grid(row=3,column=1,padx=10,pady=10)




        self.root.mainloop()


#obj=changeEmail()