from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import customtkinter as ctk


class contact:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        root.configure(bg="white")  # Set background color to white
  #Image-1
  
        img1=Image.open(r"Image\contact_title.png")  #Path of image
        img1=img1.resize((1530,152)) #Size of image
        self.img_1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.img_1)
        f_lbl.place(x=0,y=0,width=1530,height=152) #position of image
  
  

   #Image-2
  
        img2=Image.open(r"Image\footer.png")  #Path of image
        img2=img2.resize((1531,80))
        self.img_2=ImageTk.PhotoImage(img2)  
        f_lbl=Label(self.root,image=self.img_2,bg="white")
        f_lbl.place(x=0, y=709, width=1531, height=80,)
  
  
  #Image-3
  
        img3=Image.open(r"Image\back.png")  #Path of image
        img3=img3.resize((105,32))
        self.img_3=ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.img_3, bg="#2E75E9",fg="White",bd=0,activebackground="#2E75E9",cursor="hand2")
        b1.place(x=1374,y=61,width=105,height=32)
        
        
        
  #main
  
        img4=Image.open(r"Image\contact_main.png")  #Path of image
        img4=img4.resize((515,515))
        self.img_4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.img_4,bg="white")
        f_lbl.place(x=508,y=174,width=515,height=515)
 
        
        
        
        
        
        
        
        
        
        
        






if __name__=="__main__":
    root=Tk()
    obj=contact(root) 
    root.mainloop()  