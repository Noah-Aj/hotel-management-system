from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
#from login import Loginwindow
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("980x570+0+0")

        self.var_fname=StringVar()
        self.var_username=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
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

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",18,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)
        #========labels and entries
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=40,y=70)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=40,y=95,width=230)

        lname=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=290,y=70)
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_username,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=290,y=95,width=230)

        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=40,y=128)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=40,y=150,width=230)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=290,y=128)
        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=290,y=150,width=230)

        s_question=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        s_question.place(x=40,y=180)
        combo_s_question=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        combo_s_question["value"]=("Select","Your Birth Place","Your Pet Name","Who you Love Most")
        combo_s_question.current(0)
        combo_s_question.place(x=40,y=206,width=230)
        #self.s_question_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
        #self.s_question_entry.place(x=40,y=206,width=230)

        security_a=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_a.place(x=290,y=184)
        self.security_a_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_a_entry.place(x=290,y=208,width=230)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=40,y=236)
        self.txt_pass=ttk.Entry(frame,textvariable=self.var_pass,show="*",font=("times new roman",15,"bold"))
        self.txt_pass.place(x=40,y=262,width=230)

        comfirm_p=Label(frame,text="Comfirm Password",font=("times new roman",15,"bold"),bg="white")
        comfirm_p.place(x=290,y=240)
        comfirm_p_entry=ttk.Entry(frame,show="*",textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        comfirm_p_entry.place(x=290,y=263,width=230)

        #check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,text="I Agreed The Terms & Conditions",variable=self.var_check,bg="white",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=40,y=294)
        #Buttons
        img=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\register.jpg")
        img=img.resize((180,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=318,width=180)

        #img1=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\loj.jpg")
        #img1=img1.resize((180,50),Image.ANTIALIAS)
        #self.photoimg1=ImageTk.PhotoImage(img1)
        #b2=Button(frame,image=self.photoimg1,borderwidth=0,cursor="hand2")
        #b2.place(x=230,y=318,width=180)

    #function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            return
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password Must be thesame",parent=self.root)
            return
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions",parent=self.root)
            return
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_username.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered successfully kindly proceed to login",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
                return

                

            
        
        

    




if __name__ == '__main__':
    root=Tk()
    obj=Register(root)
    root.mainloop()
