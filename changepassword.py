from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *

from connection import *



class changePassword:






    def changePassFun(self):
        if len(self.oldText.get())>1:
            if len(self.newText.get())>1:
                if self.newText.get()!=self.confirmText.get():
                    showinfo("","NEW PASSWORD DOESNOT MATCH WITH CONFIRM PASSWORD")
                    self.root.destroy()
                else:

                    self.newPassword = self.newText.get()
                    if self.oldText.get()==self.oldPassword:


                        if len(self.newPassword) < 6:
                            showinfo("", "NEW PASSWORD MUST BE OF Atleast 6 Character")
                            self.root.destroy()
                        else:
                            cur = con.cursor()
                            query = 'update staff set  password="' + str(self.newPassword) + '"' + ' where email="' + str(
                                self.email) + '"'
                            print(query)
                            cur.execute(query)
                            con.commit()
                            showinfo("", "PASSWORD CHANGED")
                            self.root.destroy()
                    else:

                      showinfo("", "OLD PASSWORD WRONG!")
                      self.root.destroy()
            else:
                showinfo("","NEW PASSWORD NOT ENTERED")
                self.root.destroy()

        else:
            showinfo("","OLD PASSWORD EMPTY!")
            self.root.destroy()


    def __init__(self,username,password):

        print("I AM CHANGE PASSWORD")
        #username="donald@gmail.com"
        self.root=Tk()
        self.root.geometry("600x600")
        self.root.iconbitmap("mail.ico")

        self.root.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.root.title("CHANGE PASSWORD")
        self.email=username
        self.oldPassword=password

        oldPassword=Label(self.root,text="OLD PASSWORD", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        newPassword=Label(self.root,text="NEW PASSWORD", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        confirmPassword=Label(self.root,text="CONFIRM PASSWORD", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.oldText=Entry(self.root)
        self.newText=Entry(self.root)
        self.confirmText=Entry(self.root)

        changeBtn=Button(self.root,text="CHANGE",command=self.changePassFun)


        oldPassword.grid(row=0,column=0,padx=10,pady=10)
        self.oldText.grid(row=0,column=1,padx=10,pady=10)

        newPassword.grid(row=1,column=0,padx=10,pady=10)
        self.newText.grid(row=1,column=1,padx=10,pady=10)

        confirmPassword.grid(row=2,column=0,padx=10,pady=10)
        self.confirmText.grid(row=2,column=1,padx=10,pady=10)

        changeBtn.grid(row=3,column=1,padx=10,pady=10)




        self.root.mainloop()


#obj=changePassword('','')
