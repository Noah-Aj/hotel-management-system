from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from time import strftime
from datetime import datetime
import random
import mysql.connector
from tkinter import messagebox



class Detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("790x435+200+140")

         #########*title*########
        lbl_title=Label(self.root,text="ROOMBOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1000,height=50)

        ######logo#######
        img2=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\logo.jpg")
        img2=img2.resize((80,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=80,height=40)

        #======labelframe========
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=470,height=335)
        #floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=19,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,padx=1,sticky=W)

        #room no
        lbl_roomno=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W,padx=20)

        self.var_roomno=IntVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=19,font=("arial",13,"bold"))
        entry_roomno.grid(row=1,column=1,padx=1,sticky=W)

        #room type
        lbl_roomtype=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W,padx=20)
        
        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=19,font=("arial",13,"bold"))
        entry_roomtype.grid(row=2,column=1,padx=1,sticky=W)

        #room status
        lbl_status=Label(labelframeleft,text="Room Status",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_status.grid(row=3,column=0,sticky=W,padx=20)

        self.var_roomstatus=StringVar()
        combo_status=ttk.Combobox(labelframeleft,textvariable=self.var_roomstatus,font=("times new roman",12,"bold"),state="readonly")
        combo_status["value"]=("Clean","Dirty","Free","Faulty")
        combo_status.current(0)
        combo_status.grid(row=3,column=1)

        #room update
        lbl_roomupdate=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        #lbl_roomtype.grid(row=2,column=0,sticky=W,padx=20)
        
        self.var_roomupdate=IntVar()
        entry_roomupdate=ttk.Entry(labelframeleft,textvariable=self.var_roomupdate,width=19,font=("arial",13,"bold"))
        #entry_roomtype.grid(row=2,column=1,padx=1,sticky=W)

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=180,width=315,height=30)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.rdelete,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7,cursor="hand2")
        btnreset.grid(row=0,column=3,padx=1)

        # """""""table serach system"""""""""
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        tableframe.place(x=500,y=55,width=500,height=328)
        
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)

        self.room_table=ttk.Treeview(tableframe,column=("floor","roomno","roomtype","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("status",text="Room Status")

        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("status",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2]),
        self.var_roomstatus.set(row[3])


    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter the floor number",parent=self.root)
        else: 
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomtype=%s,status=%s where roomno=%s",(                 
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomstatus.get(),
                self.var_roomno.get()
                ))
        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)
        
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s,%s,%s)",(
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get(),
                    self.var_roomstatus.get(),
                    self.var_roomupdate.get()
                    ))
                conn.commit()
                self.fetch_data() 
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
        
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from details")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.room_table.delete(*self.room_table.get_children())
             for i in rows:
                 self.room_table.insert("",END,values=i)
             conn.commit()
         conn.close()
    def rdelete(self):
        rdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if rdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not rdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set(""),
        self.var_roomstatus.set("")



if __name__ == "__main__":
    root=Tk()
    obj=Detailsroom(root)
    root.mainloop()        
