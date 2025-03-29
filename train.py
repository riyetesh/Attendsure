from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import customtkinter as ctk


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")


        root.configure(bg="white")  # Set background color to white
  #Image-1
  
        img1=Image.open(r"C:\Users\KIIT01\Documents\KIIT\6th SEM\Project\images\td_title.png")  #Path of image
        img1=img1.resize((1530,152)) #Size of image
        self.img_1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.img_1)
        f_lbl.place(x=0,y=0,width=1530,height=152) #position of image
  
  

   #Image-2
  
        img2=Image.open(r"C:\Users\KIIT01\Documents\KIIT\6th SEM\Project\images\td_main.png")  #Path of image
        img2=img2.resize((855,548))
        self.img_2=ImageTk.PhotoImage(img2)  
        f_lbl=Label(self.root,image=self.img_2,bg="white")
        f_lbl.place(x=318, y=207, width=855, height=548,)
  
  
  #Image-3
  
        img3=Image.open(r"C:\Users\KIIT01\Documents\KIIT\6th SEM\Project\images\back.png")  #Path of image
        img3=img3.resize((105,32))
        self.img_3=ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.img_3, bg="#2E75E9",fg="White",bd=0,activebackground="#2E75E9",cursor="hand2")
        b1.place(x=1374,y=61,width=105,height=32)
  
  #Button
        b1_bottom = ctk.CTkButton(self.root, text="Take Attendance", font=("lato", 27,"bold"), fg_color="#2E75E9", hover_color="#1a5aa0", width=361, height=82,corner_radius=20,bg_color="#EBF3FA",command=self.train_classifier)
        b1_bottom.place(x=584, y=649)

        

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
          

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training! Please Wait",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)



        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!")






if __name__=="__main__":
    root=Tk()
    obj=Train(root) 
    root.mainloop()  