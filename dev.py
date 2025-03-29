from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import customtkinter as ctk


class dev:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        root.configure(bg="white")  # Set background color to white
  #Image-1
  
        img1=Image.open(r"Image\dev_title.png")  #Path of image
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
        
        
        
  #Ritesh
  
        img4=Image.open(r"Image\ritesh.png")  #Path of image
        img4=img4.resize((318,93))
        self.img_4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.img_4,bg="white")
        f_lbl.place(x=84,y=296,width=318,height=93)
  #ashu
  
        img5=Image.open(r"Image\ashu.png")  #Path of image
        img5=img5.resize((318,93))
        self.img_5=ImageTk.PhotoImage(img5)
        f_lbl=Label(self.root,image=self.img_5,bg="white")
        f_lbl.place(x=84,y=508,width=318,height=93)
  #bijay
  
        img7=Image.open(r"Image\bijay.png")  #Path of image
        img7=img7.resize((318,93))
        self.img_7=ImageTk.PhotoImage(img7)
        f_lbl=Label(self.root,image=self.img_7,bg="white")
        f_lbl.place(x=665,y=296,width=318,height=93)
  #nitu
  
        img8=Image.open(r"Image\nitu.png")  #Path of image
        img8=img8.resize((318,93))
        self.img_8=ImageTk.PhotoImage(img8)
        f_lbl=Label(self.root,image=self.img_8,bg="white")
        f_lbl.place(x=1119,y=310,width=318,height=93)
  #tariq
  
        img9=Image.open(r"Image\tariq.png")  #Path of image
        img9=img9.resize((318,93))
        self.img_9=ImageTk.PhotoImage(img9)
        f_lbl=Label(self.root,image=self.img_9,bg="white")
        f_lbl.place(x=663,y=508,width=318,height=93)
        
        
        
        
        
        
        
        
        
        
        
        






if __name__=="__main__":
    root=Tk()
    obj=dev(root) 
    root.mainloop()  