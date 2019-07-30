


from loginpage import *
from addmenu import *
from treeviewDatabase import *
from updatemenu import *
from SEARCHMENU import *
from addstaff import *
from Addtocart import *
from stafftree import *
from kitchenscreen1 import *
from changepassword import *


'''SLIDER'''

from tkinter import *
from PIL import ImageTk,Image
import time
from threading import Thread





from ChangeEmail import *

from PIL import ImageTk,Image


class mainWindow:

    def loginpage(self):
        obj = login()

    def addMenu(self):
        obj = restaurant()


    def treeviewdatabase(self):
        obj = treeview()



    def searchMenu(self):
        obj = entermenu()


    def updateMenu(self):
        obj = updatemenu()



    '''STAFF'''


    def addStaff(self):
        obj = staff()

    def stafftree(self):
        obj = staffTree()

    def addToCart(self):
        obj = addtocart()



    def kitchenScreen(self):
        obj = kitchenscreen1()

    # '''SALE REPORT'''
    # def saleReport(self):
    #     obj = saleReport()

    '''CHANGE PASSWORD'''

    def changePass(self):
        obj = changePassword(self.username, self.password)

    # '''CHANGE EMAIL'''

    def changeEmailPass(self):
         obj=changeEmail(self.username,self.password)


    def slider(self):

        worker().start()
        self.root.configure(background='white')
        self.root.mainloop()


    def __init__(self, username, password):



        self.username = username
        self.password = password
        self.root = Tk()
        self.root.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")
        self.root.geometry("1200x1200")
        self.root.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")

        self.root.title("Main Page")
        self.root.iconbitmap("cart.ico")
        self.root.iconbitmap("dish.png")
        # self.root.attributes("-fullscreen", True)
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)
        '''MENU'''
        menuDetail = Menu(self.mainmenu, tearoff=0)
        menuDetail.add_command(label="ADD MENU", command=lambda: self.addMenu())
        menuDetail.add_command(label="FULL MENU DATABASE", command=lambda: self.treeviewdatabase())
        menuDetail.add_command(label="SEARCH MENU", command=lambda: self.searchMenu())
        menuDetail.add_command(label="UPDATE MENU", command=lambda: self.updateMenu())

        self.mainBar.add_cascade(label="MENU", menu=menuDetail)

        '''STAFF'''
        staffDetail = Menu(self.mainmenu, tearoff=0)
        staffDetail.add_command(label="ADD STAFF", command=lambda: self.addStaff())
        staffDetail.add_command(label="STAFF DETAILS", command=lambda: self.stafftree())

        self.mainBar.add_cascade(label="STAFF", menu=staffDetail)

        '''ADD TO CART'''
        self.AddToCart = Menu(self.mainmenu, tearoff=0)

        self.AddToCart.add_cascade(label="CART", command=lambda: self.addToCart())
        self.mainBar.add_cascade(label="ADDCART", menu=self.AddToCart)

        '''KITCHEN SCREEN'''

        self.mainmenu.add_cascade(label="KITCHEN SCREEN", command=lambda: self.kitchenScreen())

        '''SALE REPORT'''

        #self.mainBar.add_command(label="SALE REPORT", command=lambda: self.saleReport())

        '''CHANGE PASSWORD'''
        self.changePassword=Menu(self.mainmenu, tearoff=0)
        self.changePassword.add_cascade(label='CHANGE PASSWORD', command=lambda: self.changePass())
        self.mainBar.add_cascade(label="CHANGE PASSWORD",menu=self.changePassword)

        '''CHANGE EMAIL'''
        self.changeEmail = Menu(self.mainmenu, tearoff=0)
        self.changeEmail.add_cascade(label='CHANGE EMAIL', command=lambda: self.changeEmailPass())
        self.mainBar.add_cascade(label="CHANGE EMAIL", menu=self.changeEmail)






        '''EXIT'''
        self.loginExit = Menu(self.mainmenu, tearoff=0)
        self.loginExit.add_cascade(label='EXIT', command=lambda: sys.exit())
        self.mainBar.add_cascade(label="EXIT", menu=self.loginExit)



        '''SLIDER'''
        self.slider()

        self.root.mainloop()



class worker(Thread):
    def run(self):
        lst = ["restaurantimages/food0.jpeg", "restaurantimages/food1.jpg",
               "restaurantimages/food2.jpg", "restaurantimages/food3.jpeg","restaurantimages/food4.jpeg",
               "restaurantimages/food5.jpeg","restaurantimages/food6.jpeg","restaurantimages/images-2.jpg",
               "restaurantimages/food8.jpeg","restaurantimages/food9.jpeg"]
        i = 0
        while(TRUE):
            img = ImageTk.PhotoImage(Image.open(lst[i]))

            self.lb1 = Label("", image=img)
            self.lb1.grid(row=1, column=2)
            self.lb1.place(x=20, y=20)
            time.sleep(1)
            i = i + 1
            if i==9:
                i=0






#obj = mainWindow("","")