from tkinter import *
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
from login3 import Loginwindow3
from hotel import HotelManagementSystem
from forgotpassword import Forgetpassword


class Loginwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("980x570+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\login2.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=125,width=300,height=340)

        img1=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\user2.png")
        img1=img1.resize((60,60),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bg="black",borderwidth=0,relief=RIDGE)
        lblimg.place(x=460,y=130,width=60,height=60)

        get_str=Label(frame,text="Get Started",font=("times new roman",13,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=60)

        #label
        username=Label(frame,text="Username",font=("times new roman",14,"bold"),fg="white",bg="black")
        username.place(x=60,y=90)

        self.txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))
        self.txtuser.place(x=40,y=115,width=170)

        password=Label(frame,text="Password",font=("times new roman",14,"bold"),fg="white",bg="black")
        password.place(x=60,y=158)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",13,"bold"))
        self.txtpass.place(x=40,y=185,width=170)
        #icon images=========
        img2=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\username.jpeg")
        img2=img2.resize((20,20),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bg="black",borderwidth=0,relief=RIDGE)
        lblimg.place(x=391,y=220,width=20,height=20)

        img3=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\password.jpg")
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg3,bg="black",borderwidth=0,relief=RIDGE)
        lblimg.place(x=391,y=287,width=20,height=20)
        #login button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",14,"bold"),bd=3,relief=GROOVE,fg="white",bg="red",activeforeground="white",activebackground="blue")
        loginbtn.place(x=80,y=220,width=100,height=30)
        #register button
        registerbtn=Button(frame,text="New User Register",command=self.loginmanager1,font=("times new roman",8,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=263,width=120)
        #forgot password
        loginbtn=Button(frame,text="Forgot Password",command=self.forgot,font=("times new roman",8,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=8,y=285,width=120)
    def login(self):
        username=self.txtuser.get()
        password=self.txtpass.get()
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Username/Password cannot be null",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
            my_cursor=conn.cursor()
            sql=("select * from register where username= %s and password= %s")
            my_cursor.execute(sql,[(username),(password)])
            result=my_cursor.fetchall()
            if result:
                messagebox.showinfo("Login status","Login Successfully",parent=self.root)
                self.main()
            else:
                messagebox.showinfo("Login status","Invalid Username or Password",parent=self.root)
       
                         
            
            

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def main(self):
        self.new_window=Toplevel(self.root)
        self.app=HotelManagementSystem(self.new_window)

    def loginmanager1(self):
                self.new_window=Toplevel(self.root)
                self.app=Loginwindow3(self.new_window)

    def forgot(self):
                self.new_window=Toplevel(self.root)
                self.app=Forgetpassword(self.new_window)


            
            
   
        
        
        




if __name__=="__main__":
    root=Tk()
    app=Loginwindow(root)
    root.mainloop()
