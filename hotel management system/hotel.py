from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roomboking
from reserve import Roomreserve
from reserveroom import Roomreserved
from details import Detailsroom
from login2 import Loginwindow2
from roomavailable import Roomavailable
from roombooked import Roombooked




class HotelManagementSystem:               
    def __init__(self,root):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("980x570+0+0")

        
        img1=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\4.jpg")
        img1=img1.resize((1030,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=9,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1030,height=80)

        ######logo#######
        img2=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\logo.jpg")
        img2=img2.resize((130,80),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=9,relief=RIDGE)
        lblimg.place(x=0,y=0,width=130,height=80)

        #########*title*########
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=80,width=1030,height=30)
        #"""""""""""main frame""""""""""""
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=105,width=1030,height=480)

        # """"""""menu"""""""""""""
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",9,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=110)

        #"""""""""""btn frame""""""""""""
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=25,width=150,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="BOOK ROOM",command=self.roomboking,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,pady=1)
        
        details_btn=Button(btn_frame,text="ADD ROOM",command=self.detailsroom,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",command=self.loginmanager,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        reserve_btn=Button(btn_frame,text="RESERVE ROOM",command=self.roomreserve,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        reserve_btn.grid(row=4,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=13,font=("times new roman",9,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        logout_btn.grid(row=5,column=0,pady=1)

        # """"""right side image """""""""""
        img3=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\3.jpg")
        img3=img3.resize((1300,550),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=9,relief=RIDGE)
        lblimg1.place(x=100,y=0,width=1300,height=550)
        logout=Button(main_frame,text="VIEW ROOMS AVAILABLE",command=self.roomavailable,width=10,font=("times new roman",9,"bold"),bg="green",fg="black",bd=0,cursor="hand2")
        logout.place(x=120,y=11,width=270,height=190)
        logout1=Button(main_frame,text="VIEW ROOMS ALREADY TAKEN",command=self.roombooked,width=10,font=("times new roman",9,"bold"),bg="gold",fg="black",bd=0,cursor="hand2")
        logout1.place(x=400,y=11,width=270,height=190)

        logout1=Button(main_frame,text="VIEW ROOMS RESERVED & DATE",command=self.roomreserved,width=10,font=("times new roman",9,"bold"),bg="red",fg="black",bd=0,cursor="hand2")
        logout1.place(x=680,y=11,width=270,height=190)

        # """""down images"""""""""""
        img4=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\4.jpg")
        img4=img4.resize((220,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(main_frame,image=self.photoimg4,bd=9,relief=RIDGE)
        #lblimg.place(x=0,y=220,width=220,height=210)

        img5=Image.open(r"C:\Users\SAMSUNG\Desktop\tkinter\hotel management system\images\font1.jpg")
        img5=img5.resize((225,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=9,relief=RIDGE)
        #lblimg1.place(x=0,y=230,width=220,height=190) 


    def cust(self):
                self.new_window=Toplevel(self.root)
                self.app=Cust_Win(self.new_window)
    def roomboking(self):
                self.new_window=Toplevel(self.root)
                self.app=Roomboking(self.new_window)
    def roomreserve(self):
                self.new_window=Toplevel(self.root)
                self.app=Roomreserve(self.new_window)
    def roomreserved(self):
                self.new_window=Toplevel(self.root)
                self.app=Roomreserved(self.new_window)
    def roomavailable(self):
                self.new_window=Toplevel(self.root)
                self.app=Roomavailable(self.new_window)
    def roombooked(self):
                self.new_window=Toplevel(self.root)
                self.app=Roombooked(self.new_window)
        
    def detailsroom(self):
                self.new_window=Toplevel(self.root)
                self.app=Detailsroom(self.new_window)
    def loginmanager(self):
                self.new_window=Toplevel(self.root)
                self.app=Loginwindow2(self.new_window)

    def logout(self):
        self.root.destroy()

           
                         
if __name__ == '__main__':
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
