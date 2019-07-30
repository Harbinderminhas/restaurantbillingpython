from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *



class staff:
    def reset(self):
        self.namebox.delete(0,END)
        self.emailbox.delete(0,END)
        self.mobilebox.delete(0,END)
        self.passwordbox.delete(0,END)
        self.combobox.set("")


    def staffAdition(self):
        print("Add Staff!")

        name=self.namebox.get()
        email=self.emailbox.get()
        mobile=self.mobilebox.get()
        password=self.passwordbox.get()
        staff=self.combobox.get()

        print(name)
        print(email)
        print(mobile)
        print(password)
        print(staff)


        if len(name)<1:
            showinfo("Message","PLEASE ENTER NAME")
        else:

            if len(email)<1:
                showinfo("Message","PLEASE ENTER EMAIL")
            else:

                if len(mobile)<1:
                     showinfo("Message","PLEASE ENTER YOUR MOBILE NUMBER")
                else:
                    if not (mobile).isnumeric() or len(mobile)!=10:
                        showinfo("","Mobile Number Invalid")
                    else:

                        if len(password)<1:
                            showinfo("Message","PLEASE ENTER PASSWORD")
                        else:

                            if len(password)<6 or len(password)>30:
                                showinfo("Message","Password Must Be Atleast Of 5  Character and Not more than 30 Character")

                            else:

                                if len(staff)<1:
                                        showinfo("MESSAGE","PLEASE ENTER STAFF INFORMATION")
                                else:
                                    cur = con.cursor()
                                    query='select * from staff where  email="'+email+'"'

                                    cur.execute(query)

                                    self.data=cur.fetchone()

                                    if self.data==None:
                                        query = 'Insert Into staff values("' + email + '","' + name + '","' + mobile + '","' + password + '","' + staff + '")'

                                        cur.execute(query)
                                        con.commit()
                                        showinfo("", "Data Inserted")
                                    else:
                                        showinfo("","Data Already Exit!")

                                    self.reset()
















    def __init__(self):
        self.window=Tk()

        self.window.title("ADD STAFF")
        self.window.geometry("600x550")

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.addstaff=Label(self.window,text="ADD STAFF")


        self.name=Label(self.window,text="NAME", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.email=Label(self.window,text="EMAIL", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.mobile=Label(self.window,text="MOBILE", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.password=Label(self.window,text="PASSWORD", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.staff=Label(self.window,text="STAFF TYPE", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))


        self.button=Button(self.window,text="ADD STAFF",command=self.staffAdition)







        self.namebox=Entry(self.window)

        self.emailbox=Entry(self.window)

        self.mobilebox=Entry(self.window)

        self.passwordbox=Entry(self.window)

        self.combobox=Combobox(self.window,values=["KITCHEN","CASHIER"],state="readonly")




        # '''''''''''GRID''''


        self.addstaff.grid(row=0,column=0)

        self.name.grid(row=1,column=0)

        self.email.grid(row=2,column=0)

        self.mobile.grid(row=3,column=0)

        self.password.grid(row=4,column=0)

        self.staff.grid(row=5,column=0)

        self.button.grid(row=6,column=0)




        self.namebox.grid(row=1,column=1)
        self.emailbox.grid(row=2,column=1)
        self.mobilebox.grid(row=3,column=1)
        self.passwordbox.grid(row=4,column=1)
        self.combobox.grid(row=5,column=1)


        self.button.grid(row=6,column=0)


        self.window.mainloop()


# obj=staff()

