from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("790x435+200+140")
    

        #========variables=========

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        
        


        #########*title*########
        lbl_title=Label(self.root,text="ADD CUSTOMER'S DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1100,height=50)

        ######logo#######
        img2=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\logo.jpg")
        img2=img2.resize((80,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======labelframe========
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=330,height=480)

        #""""""""labels and entries""""""""""
        lbl_cust_ref=Label(labelframeleft,text="Customer ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=19,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #""""""""CUST NAME""""""""""
        cname=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=19,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)
        #""""""""mother NAME""""""""""
        lblmname=Label(labelframeleft,text="Mother Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=19,font=("times new roman",13,"bold"))
        txtmname.grid(row=2,column=1)

        #""""""""combo gender""""""""""
        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #""""""""postcode""""""""""
        lblpost=Label(labelframeleft,text="Postcode",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpost.grid(row=4,column=0,sticky=W)

        txtpost=ttk.Entry(labelframeleft,textvariable=self.var_post,width=19,font=("times new roman",13,"bold"))
        txtpost.grid(row=4,column=1)

        #""""""""Mobile Number""""""""""
        lblmobel=Label(labelframeleft,text="Mobile Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmobel.grid(row=5,column=0,sticky=W)

        txtmobel=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=19,font=("times new roman",13,"bold"))
        txtmobel.grid(row=5,column=1)

        #""""""""Email""""""""""
        lblemail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=19,font=("times new roman",13,"bold"))
        txtemail.grid(row=6,column=1)

        #""""""""nationality""""""""""
        lblnationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("times new roman",12,"bold"),state="readonly")
        combo_nationality["value"]=("Nigeria","USA","UK")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #""""""""id proof type combobox""""""""""
        lblidproof=Label(labelframeleft,text="Id Proof Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),state="readonly")
        combo_idproof["value"]=("VotersCard","DrivingLicence","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)

        #txtmobel=ttk.Entry(labelframeleft,width=19,font=("times new roman",13,"bold"))
        #txtmobel.grid(row=5,column=1)


        #""""""""ID Number""""""""""
        idlblnumber=Label(labelframeleft,text="Id Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        idlblnumber.grid(row=9,column=0,sticky=W)

        txtidnumber=ttk.Entry(labelframeleft,width=19,textvariable=self.var_id_number,font=("times new roman",13,"bold"))
        txtidnumber.grid(row=9,column=1)

        #""""""""address""""""""""
        lbladdress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=19,font=("times new roman",13,"bold"))
        txtaddress.grid(row=10,column=1)


        #"""""""Buttons frame"""""""""""
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=315,height=30)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnreset.grid(row=0,column=3,padx=1)

        # """""""table frame serach"""""""""
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2)
        tableframe.place(x=350,y=50,width=530,height=480)
        #======searchby=======
        lblsearchby=Label(tableframe,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,font=("times new roman",12,"bold"),width=12,state="readonly")
        combo_searchby["value"]=("Mobile","Ref")
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
        details_table.place(x=0,y=50,width=480,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("ref",text="Refer No")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Mother Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="PostCode")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationali")
        self.cust_details_table.heading("idproof",text="Id Proof")
        self.cust_details_table.heading("idnumber",text="Id Number")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from customer")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.cust_details_table.delete(*self.cust_details_table.get_children())
             for i in rows:
                 self.cust_details_table.insert("",END,values=i)
             conn.commit()
         conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,adnumber=%s,Address=%s where Ref=%s",(
                    
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_ref.get()
                    ))
        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been Updated Successfully",parent=self.root)
    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for j in rows:
                self.cust_details_table.insert("",END,values=j)
            conn.commit()
        conn.close()     
        
        
            
            
            
        

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                    ))
                conn.commit()
                self.fetch_data() 
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)


     
                
            
            
        
        
        

        
        


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
