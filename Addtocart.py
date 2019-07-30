from tkinter import Tk,Entry,Label,Toplevel,Button,END,Text,PanedWindow
from tkinter.ttk import Combobox, Style, Treeview

from tkinter.messagebox import  *
from datetime import *
from EXCELSHEET import *
from connection import *
from http.client import*







class addtocart:

    def generateexcel(self):
        print(self.mainList)

        obj=EXCEL(self.mainList)









    def priceclear(self):
        self.amountbox = Entry(self.window)
        self.gstbox = Entry(self.window)
        self.netamntbox = Entry(self.window)



        self.amountbox.grid(row=7, column=1)
        self.gstbox.grid(row=8, column=1)
        self.netamntbox.grid(row=9, column=1)






    def addMenuItem(self):
        cur = con.cursor()
        query = "select * from menu "

        cur.execute(query)
        self.data = cur.fetchall()
        print(self.data)


        self.combobox1 = []

        for i in self.data:
            print(i[1])
            print(self.combobox1)
            self.combobox1.append(i[1])


        print(self.combobox1)



    def mainListfun(self):

        flag=False
        print("MainList:")
        print(self.mainList)

        print("SubList:")
        print(self.sublist)

        for i in range (0,len(self.mainList)):
            if self.sublist[1]==self.mainList[i][1]:


                flag=True
                print("Inside Mainlist[i][3]=")
                print(self.mainList[i][3])

                print("Inside Mainlist[i][4]=")
                print(self.mainList[i][4])
                self.mainList[i][3]=int(self.sublist[3])+int(self.mainList[i][3])
                self.mainList[i][4]=float(self.sublist[4])+float(self.mainList[i][4])




        if flag==False:
            self.serial = self.serial + 1
            self.mainList.append(self.sublist)






    def menu(self):
        self.mainList=[]





    def quantity(self):
        self.menuQuantity=[]
        for i in range(1,11):
            self.menuQuantity.append(i)
            print(self.menuQuantity)



    def combobox1(self):

        self.serial = self.serial + 1
        self.addMenuItem()
        self.Qantity = self.combobox2.get()
        self.MenuNam = self.combobox1.get()
        print("Quantity:" + self.Qantity)
        print("Price:" + str(self.Price))
        self.totalPrice = (int(self.price) * int(self.Qantity))
        print("Total Price:" + str(self.totalPrice))
        self.treeData = [self.SerialNum, self.MenuName, self.Price, self.Qantity, self.TotalPrice]
        self.row = self.row + 1
        self.treeview.insert("", self.row, values=self.treeData)

    def priceCalculationBox(self):

        self.priceclear()

        self.amountbox['state'] = "normal"
        self.gstbox['state'] = "normal"
        self.netamntbox['state'] = "normal"


        self.amountbox.insert(0, self.totalAmtVar)
        self.gstbox.insert(0, self.gstAmtVar)
        self.netamntbox.insert(0, self.netAmtVar)
        self.amountbox['state'] = "readonly"
        self.gstbox['state'] = "readonly"
        self.netamntbox['state'] = "readonly"




    def fillTreeview(self):

        self.resetTreeview()

        for i in range(0, len(self.mainList)):
            self.treeview.insert("", i, values=self.mainList[i])
        self.pricecalculation()
        self.priceCalculationBox()


    def pricecalculation(self):



        print(self.mainList)

        self.totalAmtVar=0
        for i in range(0,len(self.mainList)):

            self.totalAmtVar=self.mainList[i][4]+self.totalAmtVar

            # print("Total Amount="+str(self.totalAmtVar))

        self.gstAmtVar=5*(0.01)
        self.netAmtVar=self.totalAmtVar+(self.totalAmtVar*self.gstAmtVar)




        # print("Total Net:"+str(self.netAmtVar))

        # print(str(self.totalAmtVar))
        # print(str(self.gstAmtVar))
        # print(str(self.netAmtVar))
        # print('Total Amount: ' + str(self.totalAmtVar) + " " + str(self.gstAmtVar) + " " + str(self.netAmtVar))



    def reset(self):
        self.combobox1.set("")
        self.combobox2.set("")
        self.combobox3.set("")
        self.combobox4.set("")

        self.combobox3 = Combobox(self.window, value=["TAKE AWAY", "DINE IN", "HOME DELIVERY"], state="readonly")

        self.addrssbox = Entry(self.window)

        self.combobox4 = Combobox(self.window, value=["CASH", "CREDIT CARD", "PAYTM"], state="readonly")

        self.cashcollctedbox = Entry(self.window)

        self.retrndbox = Entry(self.window)

        self.mobilebox = Entry(self.window)



        self.combobox3.grid(row=7, column=3)
        self.addrssbox.grid(row=8, column=3)
        self.combobox4.grid(row=9, column=3)
        self.cashcollctedbox.grid(row=10, column=3)
        self.retrndbox.grid(row=11, column=3)
        self.mobilebox.grid(row=12, column=3)


        self.amountbox = Entry(self.window)
        self.gstbox = Entry(self.window)
        self.netamntbox = Entry(self.window)

        self.amountbox.grid(row=7, column=1)
        self.gstbox.grid(row=8, column=1)
        self.netamntbox.grid(row=9, column=1)




    def addCart(self):

            self.menuName=self.combobox1.get()
            cur=con.cursor()
            query='select * from menu where name="'+self.menuName +'"'
            # print(query)
            cur.execute(query)
            self.data=cur.fetchone()
            self.price=self.data[3]
            self.quantity=self.combobox2.get()
            self.totalPrice=(int(self.price)*int(self.quantity))








            self.sublist=[self.serial,self.menuName,self.price,self.quantity,self.totalPrice]

            self.mainListfun()





            self.fillTreeview()






    def resetTreeview(self):

         for i in self.treeview.get_children():
            self.treeview.delete(i)
            self.priceclear()


    def orderBar(self):

        print("Entry into Orderbar")
        self.typeoforder=self.combobox3.get()
        self.address=self.addrssbox.get()

        self.modeofpayment=self.combobox4.get()
        self.cashcollected=self.cashcollctedbox.get()
        self.cashreturned=self.retrndbox.get()
        self.mobileno=self.mobilebox.get()

        self.netamount=self.netamntbox.get()
        self.gst=self.gstbox.get()
        self.status="Pending"

        self.cashReturn =float( self.cashcollctedbox.get()) - float(self.netamntbox.get())
        self.retrndbox.insert(0, self.cashReturn)
        self.retrndbox['state'] = "readonly"




    def insertData(self):
        cur = con.cursor()
        query = "Insert into bill(typeoforder  ,address   ,modeofpayment ,cashcollected ,cashreturned, mobileno   ,netamount ,gst,  status ,date) values('" + self.typeoforder + "','" + self.address + "','" + self.modeofpayment + "'," + str(self.cashcollected) + "," + str(self.cashReturn) + "," + self.mobileno + "," + str(self.netamount) + "," + str(self.gst) + ",'" + self.status + "','"+str(self.date)+"')"

        print(query)
        cur.execute(query)
        con.commit()
        billid =0
        q="select billid from bill"
        cur.execute(q)
        rs=cur.fetchall()
        for row in rs:
            billid=row[0]
        for row in self.mainList:
            mname=str(row[1])
            q2="select menuid from menu where name ='"+mname+"'"
            cur.execute(q2)
            rs2=cur.fetchone()
            mid=rs2[0]
            q3="insert into billdetails values (NULL ,'"+str(billid)+"','"+str(mid)+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"')"
            cur.execute(q3)
            con.commit()








        showinfo("DATA INSERTED")
        msg="order placed successfully :  NetAmount is Rs."+str(self.netamntbox.get())+"  type of order: "+str(self.typeoforder)+" Mode of payment "+str(self.modeofpayment)
        mobile = str(self.mobileno)
        print('kkkkkk '+str(mobile))

        msg = msg.replace(" ", "%20")
        msg= msg.replace(":", "%3A")
        conn = HTTPConnection("server1.vmm.education")
        conn.request('GET',
                     "/VMMCloudMessaging/AWS_SMS_Sender?""username=harbinderminhas&password=8N1XG8UB&message="+msg+"&phone_numbers=" + mobile)
        response = conn.getresponse()
        print(response.read())
        self.reset()



    def  generateBill(self):



        print(self.mobilebox.get())
        if self.combobox3.get()=="":
            showinfo("PLEASE SELECT ORDER  TYPE")
        else:
            if self.combobox4.get()=="":
                showinfo("","SELECT PAYMENT MODE")
            else:
                if str(self.mobilebox.get()).isnumeric() and len(self.mobilebox.get().strip())==10:

                    if len(self.cashcollctedbox.get())<1:

                        showinfo("","CASH NOT Collected")
                    else:
                        if self.combobox3.get()=="HOME DELIVERY":
                            if len(self.addrssbox.get(0.0,END).strip())<1:
                                showinfo("","ADDRESS NOT FILLED")
                        else:
                            self.orderBar()
                            self.insertData()




                elif len(self.mobilebox.get().strip())==0:
                    showinfo('','enter mobile no')
                elif not str(self.mobilebox.get()).isnumeric():
                    showinfo("", "INVALID MOBILE NUMBER!")
                else:

                    self.inserData()
                    self.reset()






























    def __init__(self):

        self.mainList=[]
        self.sublist=["Serial Number","Item Name","Price","Quantity","Total Price"]


        self.serial = 1
        self.row = 0
        self.window=Toplevel()
        self.window.geometry("1200x800")

        #for background color

        self.window.config(bg="lightcyan", highlightthickness=8, highlightbackground="navy", highlightcolor="navy")

        self.window.title("ADD TO CART")


        self.date=datetime.now()




        self.datetime = str(self.date).split(" ")


        self.date = self.datetime[0]
        self.time = (self.datetime[1]).split(".")
        self.time = self.time[0]

        print("DATE:" + self.date)
        print("TIME:", self.time)

        print("DATETIME  AFTER SPLIT:", self.datetime)

        self.dateLabel = Label(self.window, text=self.date)
        self.timeLabel = Label(self.window, text=self.time)

        self.dateLabel.grid(row=0, column=2)
        self.timeLabel.grid(row=0, column=3)




        self.addMenuItem()
        self.quantity()

        #label color
        self.slctname=Label(self.window,text="SELECT NAME", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))




        self.combobox1=Combobox(self.window,value=self.combobox1,state="readonly")





        self.slctquantity=Label(self.window,text="SELECT QUANTITY")
        self.combobox2=Combobox(self.window,value=self.menuQuantity,state="readonly")



        self.addbttn=Button(self.window,text="ADD TO CART",command=self.addCart)


        self.slctname.grid(row=1,column=0,padx=10,pady=10)
        self.combobox1.grid(row=1,column=1,padx=10,pady=10)


        self.slctquantity.grid(row=1,column=2,padx=10,pady=10)
        self.combobox2.grid(row=1,column=3,padx=10,pady=10)


        self.addbttn.grid(row=1,column=4,padx=10,pady=10)











        self.treeview=Treeview(self.window,column=("SerialNum","MenuName","Price","Qantity","TotalPrice"))
        self.treeview.heading("SerialNum",text="SERIAL NUMBER")
        self.treeview.heading("MenuName",text="MENU NAME")
        self.treeview.heading("Price",text="PRICE")
        self.treeview.heading("Qantity",text="QUANTITY")
        self.treeview.heading("TotalPrice",text="TOTAL PRICE")

        self.treeview["show"]="headings"

        # scroll = Scrollbar(self.window, orient="vertical", command=self.treeview.yview)
        #
        # scroll.pack(pady=20, side=RIGHT, fill=Y)
        # self.treeview.configure(yscrollcommand=scroll.set)


        #for table color

        style = Style()
        style.configure("Treeview.Heading", font=("Script MT Bold", 16))
        style.configure("Treeview", font=("calibri", 13))




        self.treeview.grid(row=3,column=0,columnspan=7)









        self.totalAmnt = Label(self.window, text="TOTAL AMOUNT:", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.gst = Label(self.window, text="GST:", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.netAmnt = Label(self.window, text="NET AMOUNT:", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.totalAmtVar = ""
        self.gstAmtVar = ""
        self.netAmtVar = ""

        self.totalAmnt.grid(row=7, column=0)
        self.gst.grid(row=8, column=0)
        self.netAmnt.grid(row=9, column=0)



        self.typeofordr = Label(self.window, text="TYPE OF ORDER", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.adress = Label(self.window, text="ADDRESS", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.paymntmode = Label(self.window, text="MODE OF PAYMENT", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.cashcllectd = Label(self.window, text="CASH COLLECTED", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.retrnd = Label(self.window, text="CASH RETURNED", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))
        self.mobile = Label(self.window, text="MOBILE NUMBER", bg="lightcyan", fg="red",font=("Harlow Solid Italic", 40, "italic", "bold"))

        self.combobox3 = Combobox(self.window, value=["TAKE AWAY", "DINE IN", "HOME DELIVERY"], state="readonly")

        self.addrssbox = Entry(self.window)

        self.combobox4 = Combobox(self.window, value=["CASH", "CREDIT CARD", "PAYTM"], state="readonly")

        self.cashcollctedbox = Entry(self.window)

        self.retrndbox = Entry(self.window)

        self.mobilebox = Entry(self.window)

        self.typeofordr.grid(row=7, column=2)
        self.adress.grid(row=8, column=2)
        self.paymntmode.grid(row=9, column=2)
        self.cashcllectd.grid(row=10, column=2)
        self.retrnd.grid(row=11, column=2)
        self.mobile.grid(row=12, column=2)

        self.combobox3.grid(row=7, column=3)
        self.addrssbox.grid(row=8, column=3)
        self.combobox4.grid(row=9, column=3)
        self.cashcollctedbox.grid(row=10, column=3)
        self.retrndbox.grid(row=11, column=3)
        self.mobilebox.grid(row=12, column=3)









        self.genratbttn=Button(self.window,text="GENERATE EXCEL",command=self.generateexcel)
        self.genratbill=Button(self.window,text="GENERATE BILL",command=self.generateBill)


        self.genratbttn.grid(row=13,column=0)
        self.genratbill.grid(row=13,column=1)














        self.window.mainloop()







# obj =addtocart()