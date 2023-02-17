from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import random
import mysql.connector
from tkinter import messagebox



class Roomboking:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("790x435+200+140")


        #============variables==========
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=IntVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.var_status=StringVar()
        
        
        

        #########*title*########
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1000,height=50)

        ######logo#######
        img2=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\logo.jpg")
        img2=img2.resize((80,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======labelframe========
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roomboking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=410,height=500)

        #""""""""labels and entries""""""""""
        #CONTACT
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=19,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,padx=1,sticky=W)
        #FETCH DATA BUTTON
        btnfetchdata=Button(labelframeleft,text="Fetch",command=self.fetch_contact,font=("arial",7,"bold"),bg="black",fg="gold",height=2,width=4)
        btnfetchdata.place(x=370,y=4)
        
          #=========check in date=========
        
        check_in_date=Label(labelframeleft,text="Check_in Date:dd/mm/yyyy",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=19,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1,sticky=W)

         #=========check out date=========
        
        lbl_check_out=Label(labelframeleft,text="Check Out:dd/mm/yyyy",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,width=19,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txt_check_out.grid(row=2,column=1,sticky=W)

        #room type

        label_roomtype=Label(labelframeleft,width=19,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_roomtype.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide=my_cursor.fetchall()

        combo_roomtype=ttk.Combobox(labelframeleft,font=("times new roman",13,"bold"),textvariable=self.var_roomtype,width=19,state="readonly")
        combo_roomtype["value"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1,padx=2,sticky=W)

        #room available
        lblroomavailable=Label(labelframeleft,text="Room Available:",font=("arial",12,"bold"),padx=2,pady=6)
        lblroomavailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        combo_roomno=ttk.Combobox(labelframeleft,font=("times new roman",13,"bold"),textvariable=self.var_roomavailable,width=19,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1,padx=2,sticky=W)

        #txtroomavailable=ttk.Entry(labelframeleft,width=19,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
        #txtroomavailable.grid(row=4,column=1,sticky=W)

        #meal
        lblmeal=Label(labelframeleft,text="Purpose:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmeal.grid(row=5,column=0,sticky=W)

        txtmeal=ttk.Entry(labelframeleft,width=19,textvariable=self.var_meal,font=("arial",13,"bold"))
        txtmeal.grid(row=5,column=1,sticky=W)

        
        #no of days
        lblnoofdays=Label(labelframeleft,text="No of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=6,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,width=19,textvariable=self.var_noofdays,font=("arial",13,"bold"))
        txtnoofdays.grid(row=6,column=1,sticky=W)

        #paid tax

        lblnoofdays=Label(labelframeleft,text="Paid Tax:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=7,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,width=19,textvariable=self.var_paidtax,font=("arial",13,"bold"))
        txtnoofdays.grid(row=7,column=1,sticky=W)

        #sub total
        lblnoofdays=Label(labelframeleft,text="Sub Total:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnoofdays.grid(row=8,column=0,sticky=W)

        txtnoofdays=ttk.Entry(labelframeleft,width=19,textvariable=self.var_actualtotal,font=("arial",13,"bold"))
        txtnoofdays.grid(row=8,column=1,sticky=W)

        #total cost
        lblidnumber=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        txtidnumber=ttk.Entry(labelframeleft,width=19,textvariable=self.var_total,font=("arial",13,"bold"))
        txtidnumber.grid(row=9,column=1,sticky=W)

        #room status
        status=Label(labelframeleft,text="Room Status:",font=("arial",12,"bold"),padx=2,pady=6)
        status.grid(row=10,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select status from details")
        stu=my_cursor.fetchall()

        combo_status=ttk.Combobox(labelframeleft,font=("times new roman",13,"bold"),textvariable=self.var_status,width=19,state="readonly")
        combo_status["value"]=stu
        combo_status.current(0)
        combo_status.grid(row=10,column=1,padx=2,sticky=W)
        #Bill btn
        btnbill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnbill.grid(row=11,column=0,padx=1,sticky=W)
        

         #"""""""Buttons frame"""""""""""
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=415,width=315,height=30)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="unbook",command=self.rdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnreset.grid(row=0,column=3,padx=1)



        #------rightside image-------
        img3=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\3.jpg")
        img3=img3.resize((330,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=650,y=50,width=330,height=200)
        

         # """""""table serach system"""""""""
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        tableframe.place(x=450,y=250,width=530,height=260)
        #======searchby=======
        lblsearchby=Label(tableframe,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=12,state="readonly")
        combo_searchby["value"]=("Contact","Room")
        combo_searchby.current(0)
        combo_searchby.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtsearch=ttk.Entry(tableframe,width=12,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(tableframe,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold")
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(tableframe,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold")
        btnshowall.grid(row=0,column=4,padx=2)

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=400,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-In")
        self.room_table.heading("checkout",text="Check-Out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noofdays",text="NoOfDays")

        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)


        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.room_table.pack(fill=BOTH,expand=1)


        self.fetch_data()
    #add data
        #roomstate=1
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            if self.var_status.get()=="Clean":              
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                    my_cursor=conn.cursor()
                    
                    my_cursor.execute("insert into mydata_room values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get()
                        ))
                    #roomstate=1
                    roomno=self.var_roomavailable.get()
                    sql=("update  details set roomstate=1 where roomno=%s")
                    my_cursor.execute(sql,[(roomno)])
                    
                    my_cursor.execute("insert into report values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_roomavailable.get(),
                        self.var_meal.get(),
                        self.var_noofdays.get(),
                        self.var_paidtax.get(),
                        self.var_actualtotal.get(),
                        self.var_total.get()          
                        ))
                    #room avalaible
                    #my_cursor.execute("update details set roomstate=1 where roomno=self.var_roomavailable.get()")
                    
                    conn.commit()
                    conn.commit()
                    self.fetch_data() 
                    conn.close()
                    messagebox.showinfo("Success","Room Booked",parent=self.root)
                    
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

            #fetch data
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    #update
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update mydata_room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                    
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                    ))
            my_cursor.execute("update report set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                    
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                    ))
        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)
    def reset(self):
        #self.var_ref.set(""),
        self.var_contact.set(""),
        self.var_checkin.set(""),
        #self.var_gender.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        #self.var_nationality.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        #self.var_address.set("")        
        
    
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from mydata_room")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)
             conn.commit()
         conn.close()
    

        
    #ALL DATA FETCH
    def rdelete(self):
        rdelete=messagebox.askyesno("Hotel Management System","Do you want to unbook this room",parent=self.root)
        if rdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query="delete from mydata_room where roomavailable=%s"
            sql="delete from details where roomno=%s"
            value=(self.var_roomavailable.get(),)
            value2=(self.var_roomavailable.get(),)
            my_cursor.execute(sql,value2)
            my_cursor.execute(query,value)
        else:
            if not rdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
       
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Phone Number Does Not Exist In Our Database",parent=self.root)
            else:
                conn.commit()
                conn.close()


                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=200,height=160)

                lblname=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)


                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #Gender
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdataframe,text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)
                lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #Email
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showdataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)
                lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showdataframe,text="Nationality:",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=90)
                lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #address
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showdataframe,text="Address:",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=120)
                lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=120)
    #searching system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from mydata_room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for j in rows:
                self.room_table.insert("",END,values=j)
            conn.commit()
        conn.close()     
                
    def total(self):
        indate=self.var_checkin.get()
        outdate=self.var_checkout.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outdate-indate).days)
        if self.var_roomtype.get()=="Luxury":
            q1=float(30000)
            q2=float(7000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.1))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
            

        if self.var_roomtype.get()=="Double":
            q1=float(23000)
            q2=float(65500)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=float(q5*0.001+q5) 
            tax="#"+str("%.2f"%((q5)*0.01))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.01)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
            

        if self.var_roomtype.get()=="Single":
            q1=float(4500)
            q2=float(20000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.001))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.001)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        if self.var_roomtype.get()=="Luxury":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.1))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Double":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.01))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.01)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
            

        if self.var_roomtype.get()=="Single":
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.001))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.001)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)


        if self.var_roomtype.get()=="Luxury":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.1))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Double":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.01))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.01)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Single":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5            
            tax="#"+str("%.2f"%((q5)*0.001))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.001)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        if self.var_roomtype.get()=="Luxury":
            q1=float(30000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.1))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Double":
            q1=float(40000)
            q2=float(70000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.01))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.01)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Single":
            q1=float(300)
            q2=float(7000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.001))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.001)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)
        if (self.var_meal.get()=="conference" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.1))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Double":
            q1=float(300000)
            q2=float(700000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.01))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.01)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

        if self.var_roomtype.get()=="Single":
            q1=float(300000)
            q2=float(700000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            q6=q5*0.001+q5 
            tax="#"+str("%.2f"%((q5)*0.001))
            st="#"+str("%.2f"%((q5)))
            tt="#"+str("%.2f"%(q5+((q5)*0.001)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(tt)

                




        


                           
                           
                    







            

            
            

            










if __name__ == "__main__":
    root=Tk()
    obj=Roomboking(root)
    root.mainloop()        
