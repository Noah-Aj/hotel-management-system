from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#from login import Loginwindow
from tkinter import messagebox
import mysql.connector


class Forgetpassword:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("980x570+0+0")

        self.email=StringVar()
        self.security=StringVar()
        self.password=StringVar()       
         #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\login2.jpg")   
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        #left image
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\tea.jpg")   
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=40,y=70,width=300,height=400)
        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=270,y=70,width=600,height=400)

        register_lbl=Label(frame,text="RECOVER YOUR PASSWORD HERE",font=("times new roman",18,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        register_lbl=Label(frame,text="THERE USER KINDLY ENTER YOUR EMAIL ADDRESS AND SECURITY QUESTION ANSWER\n THEN CLICK ON FETCH BUTTON TO RECOVER YOUR PASSWORD",font=("times new roman",10,"bold"),fg="red",bg="white")
        register_lbl.place(x=20,y=70)
        #========labels and entries
        email=Label(frame,text="Enter The Email You Used To Register",font=("times new roman",15,"bold"),fg="green",bg="white")
        email.place(x=200,y=118)
        
        self.email_entry=ttk.Entry(frame,textvariable=self.email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=200,y=150,width=230)
        fetchbtn=Button(frame,text="FETCH",command=self.fetch,font=("times new roman",8,"bold"),bd=1,relief=GROOVE,fg="black",bg="red",activeforeground="black",activebackground="black")
        fetchbtn.place(x=420,y=147,width=100,height=35)
        

        security_a=Label(frame,text="Enter Your Security Answer",font=("times new roman",15,"bold"),fg="green",bg="white")
        security_a.place(x=200,y=184)
        self.security_a_entry=ttk.Entry(frame,textvariable=self.security,font=("times new roman",15,"bold"))
        self.security_a_entry.place(x=200,y=220,width=230)

        newpass_a=Label(frame,text="Your Password is",font=("times new roman",15,"bold"),fg="green",bg="white")
        newpass_a.place(x=200,y=260)
        self.pass_entry=ttk.Entry(frame,textvariable=self.password,font=("times new roman",15,"bold"))
        self.pass_entry.place(x=200,y=290,width=230)

        loginbtn=Button(frame,text="CLICK TO PROCEED",command=self.fetch,font=("times new roman",12,"bold"),bd=4,relief=GROOVE,fg="white",bg="green",activeforeground="white",activebackground="blue")
        loginbtn.place(x=240,y=500,width=180,height=38)

    def fetch(self):
        email=self.email.get()
        security=self.security.get()
        #password=password.get()
        
        if (self.email.get()=="" or self.security.get()==""):
            messagebox.showerror("error","Please User, Email and Security Answer are Compulsary",parent=self.root)
        if (self.email.get()!="" or self.security.get()!=""):
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select password from register where email='"+ self.email.get() +"' and securityA='"+ self.security.get() +"' ")
            rows=my_cursor.fetchall()
            for row in rows:   
                self.pass_entry.insert(0,row[0])
        if not rows:
            messagebox.showerror("Rocover Update","Email/Security Answer DoesNotExist",parent=self.root)
            return
                




if __name__ == '__main__':
    root=Tk()
    obj=Forgetpassword(root)
    root.mainloop()
