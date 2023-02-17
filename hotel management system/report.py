from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("MANAGER ADMIN ONLY")
        self.root.geometry("980x570+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\tea.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=10,y=50,width=1200,height=480)
        #======searchby=======
        lblsearchby=Label(tableframe,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=12,state="readonly")
        combo_searchby["value"]=("check_in","check_out")
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

        self.cust_details_table=ttk.Treeview(details_table,column=("contact","check_in","check_out","roomtype","roomavailable","meal","noofdays","paidtax","actualtotal","total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("contact",text="Contact")
        self.cust_details_table.heading("check_in",text="Check In")
        self.cust_details_table.heading("check_out",text="Check Out")
        self.cust_details_table.heading("roomtype",text="Room Type")
        self.cust_details_table.heading("roomavailable",text="Room Available")
        self.cust_details_table.heading("meal",text="Purpose")
        self.cust_details_table.heading("noofdays",text="No of days")
        self.cust_details_table.heading("paidtax",text="Paid Tax")
        self.cust_details_table.heading("actualtotal",text="Actual Total")
        self.cust_details_table.heading("total",text="Total")

        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("contact",width=100)
        self.cust_details_table.column("check_in",width=100)
        self.cust_details_table.column("check_out",width=100)
        self.cust_details_table.column("roomtype",width=100)
        self.cust_details_table.column("roomavailable",width=100)
        self.cust_details_table.column("meal",width=100)
        self.cust_details_table.column("noofdays",width=100)
        self.cust_details_table.column("paidtax",width=100)
        self.cust_details_table.column("actualtotal",width=100)
        self.cust_details_table.column("total",width=100)

        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        #self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        self.seesum()
        
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from report")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.cust_details_table.delete(*self.cust_details_table.get_children())
             for i in rows:
                 self.cust_details_table.insert("",END,values=i)
             conn.commit()
         conn.close()
   # def get_cursor(self,event=""):
     #   cursor_row=self.cust_details_table.focus()
      #  content=self.cust_details_table.item(cursor_row)
      #  row=content["values"]

      #  self.var_.set(row[0]),
      #  self.var_cust_name.set(row[1]),
       # self.var_mother.set(row[2]),
        #self.var_gender.set(row[3]),
        #self.var_post.set(row[4]),
        #self.var_mobile.set(row[5]),
        #self.var_email.set(row[6]),
        #self.var_nationality.set(row[7]),
       # self.var_id_proof.set(row[8]),
       # self.var_id_number.set(row[9]),
       # self.var_address.set(row[10])
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from report where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for j in rows:
                self.cust_details_table.insert("",END,values=j)
            conn.commit()
        conn.close()
        
        
        





if __name__=="__main__":
    root=Tk()
    app=Report(root)
    root.mainloop()
