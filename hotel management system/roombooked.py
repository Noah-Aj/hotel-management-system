from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
#from roombooked import Roombooked

class Roombooked:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("980x570+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\tea.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details Of Rooms Already Booked",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=10,y=50,width=1200,height=480)
        #======searchby=======
        lblsearchby=Label(tableframe,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=12,state="readonly")
        combo_searchby["value"]=("roomno","status")
        combo_searchby.current(0)
        combo_searchby.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,textvariable=self.txt_search,width=12,font=("times new roman",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(tableframe,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold")
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(tableframe,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold")
        btnshowall.grid(row=0,column=4,padx=2)

        #==========show data table============
        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=800,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("floor","roomno","roomtype","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("floor",text="Floor")
        self.cust_details_table.heading("roomno",text="Room Number")
        self.cust_details_table.heading("roomtype",text="Room Type")
        self.cust_details_table.heading("status",text="Room Status")

        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("floor",width=100)
        self.cust_details_table.column("roomno",width=100)
        self.cust_details_table.column("roomtype",width=100)
        self.cust_details_table.column("status",width=100)

        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        #self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        btn_frame=Frame(tableframe,bd=4,relief=RIDGE)
        btn_frame.place(x=470,y=410,width=240,height=50)

        cust_btn=Button(btn_frame,text="BOOK ROOM HERE",command=self.roombooked,width=20,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)
        
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from details where roomstate=1")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.cust_details_table.delete(*self.cust_details_table.get_children())
             for i in rows:
                 self.cust_details_table.insert("",END,values=i)
             conn.commit()
         conn.close()
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from details where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for j in rows:
                self.cust_details_table.insert("",END,values=j)
            conn.commit()
        conn.close()

    def roombooked(self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooked(self.new_window)
        
        
        





if __name__=="__main__":
    root=Tk()
    app=Roombooked(root)
    root.mainloop()

