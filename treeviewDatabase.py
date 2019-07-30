from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview
from tkinter.messagebox import  *
from connection import *

class treeview:
    def clearTreeData(self):
        for x in self.treeview.get_children():
            self.treeview.delete(x)

    def fullDataFetchQuery(self):
        cur = con.cursor()
        query="select * from menu"

        cur.execute(query)

        self.data=cur.fetchall()
        print(self.data)


    def showFullData(self):

        self.fullDataFetchQuery()

        for i in range(0,len(self.data)):
            self.treeview.insert("",i,values=self.data[i])












    def deleteCommand(self):
        v = self.treeview.focus()
        c = self.treeview.item(v)
        v1 = c['values']
        if len(v1) > 0:
            ''' GET DATA FROM TREEVIEW'''
            self.treeData = self.treeview.item(self.treeview.focus())['values']
            print(self.treeData)
            print(self.treeData[0])
            ''' ASK YES NO CONFIRMATION '''
            confirm = askyesno("ARE YOU SURE YOU WANT TO DELETE")
            if confirm == True:
                cur = con.cursor()
                query = "delete from menu where menuid=" + str(self.treeData[0])
                print(query)
                cur.execute(query)
                con.commit()

                message = "Data Deleted for MenuId:" + str(self.treeData[0]) + " with Menu Item:" + str(
                    self.treeData[1])
                showinfo("Message", message)

                self.clearTreeData()
                self.showFullData()
        else:
            showinfo('','select any menu first')

    def __init__(self):

        self.window=Toplevel()

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")



        # *******************FRAME 1 Tree view***************************

                            #DATA QUERY



        self.frame1=PanedWindow(self.window)
        self.treeview= Treeview(self.frame1, columns=("menu","name","description","price"))
        self.treeview.heading("menu",text="Menu Item")
        self.treeview.heading("name", text="Name")
        self.treeview.heading("description", text="Description")
        self.treeview.heading("price", text="Price")


        self.treeview["show"]="headings"

        # for table color

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))

        self.treeview.pack()


       #*********EVENT BIND TREEVIW**************





        self.frame1.pack()
        self.showFullData()




        # ***************FRAME 2********************

        self.frame2 = PanedWindow(self.window)

        self.delBtn = Button(self.frame2, text="Delete",command=self.deleteCommand)
        self.delBtn.grid(row=0, column=1)

        self.frame2.pack()
        self.window.mainloop()



# obj=treeview()



