from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
from train import Train
from face_recognition import Face_Recognition




class Home:
   
 def __init__ (self, root) :
  self.root=root
  self.root.geometry( "1530x790+0+0" )
  self.root.title("Recognition System")  #Change the title to the name of software
  
  root.configure(bg="white")  # Set background color to white
  #Image-1
  
  img1=Image.open(r"Image\home_title.png")  #Path of image
  img1=img1.resize((1530,152)) #Size of image
  self.img_1=ImageTk.PhotoImage(img1)
 
  f_lbl=Label(self.root,image=self.img_1)
  f_lbl.place(x=0,y=0,width=1530,height=152) #position of image
  
  

   #Image-2
  
  img2=Image.open(r"Image\sd.png")  #Path of image
  img2=img2.resize((238,238))
  self.img_2=ImageTk.PhotoImage(img2)  
  b1 = Button(self.root, image=self.img_2, borderwidth=0,background="White",activebackground="white",cursor="hand2")
  b1.place(x=555, y=215, width=238, height=238)
  
  
  #Image-3
  
  img3=Image.open(r"Image\fr.png")  #Path of image
  img3=img3.resize((238,238))
  self.img_3=ImageTk.PhotoImage(img3)
  b1 = Button(self.root, image=self.img_3, borderwidth=0,background="White",activebackground="white",cursor="hand2",command=self.face_detect_window_open)
  b1.place(x=889,y=215,width=238,height=238)
  
  
  
  
  
    #Image-4
  
  img4=Image.open(r"Image\tr.png")  #Path of image
  img4=img4.resize((238,238))
  self.img_4=ImageTk.PhotoImage(img4)
  b1 = Button(self.root, image=self.img_4, borderwidth=0,background="White",activebackground="white",cursor="hand2",command=self.train_window_open)
  b1.place(x=1223,y=215,width=238,height=238)
  
  
  #Image-5
  
  img5=Image.open(r"Image\photos.png")  #Path of image
  img5=img5.resize((238,238))
  self.img_5=ImageTk.PhotoImage(img5)
  b1 = Button(self.root, image=self.img_5, borderwidth=0,background="White",activebackground="white",cursor="hand2",command=self.open_img)
  b1.place(x=555,y=512,width=238,height=238)
  
  
   #Image-6
  
  img6=Image.open(r"Image\dev.png")  #Path of image
  img6=img6.resize((238,238))
  self.img_6=ImageTk.PhotoImage(img6)
  b1 = Button(self.root, image=self.img_6, borderwidth=0,background="White",activebackground="white",cursor="hand2")
  b1.place(x=889,y=512,width=238,height=238)
  
   #Image-7
  
  img7=Image.open(r"Image\help.png")  #Path of image
  img7=img7.resize((238,238))
  self.img_7=ImageTk.PhotoImage(img7)
  b1 = Button(self.root, image=self.img_7, borderwidth=0,background="White",activebackground="white",cursor="hand2")
  b1.place(x=1223,y=512,width=238,height=238)
  
  



  
  
  #Attendance
  
     #image of button
  img_take_att=Image.open(r"Image\take_att.png")  #Path of image
  img_take_att=img_take_att.resize((410,536)) #Size of image
  self.img_std_button=ImageTk.PhotoImage(img_take_att)
  f_lbl=Label(self.root,image=self.img_std_button,bg="white")
  f_lbl.place(x=64,y=215,width=410,height=536) #position of image
  
  b1_bottom=Button(text="Take Attendance",cursor="hand2",font=("lato",15,"bold"),bg="#2E75E9",fg="White",bd=-4,relief="sunken",activebackground="#2E75E9",)
  b1_bottom.place(x=180,y=675)
  
  
  

 def open_img(self):
    os.startfile("data")
    
  
 def train_window_open(self):
    for widget in self.root.winfo_children():
     widget.destroy()
    self.app = Train(self.root)
    
    
    
 def face_detect_window_open(self):
    for widget in self.root.winfo_children():
     widget.destroy()
    self.app = Face_Recognition(self.root)

           


  
if __name__=="__main__":
 root=Tk()
 obj=Home(root)
 root.mainloop()
 