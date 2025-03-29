from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import face_recognition 
import customtkinter as ctk






class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        root.configure(bg="white")  # Set background color to white
  #Image-1
  
        img1=Image.open(r"Image\fd_title.png")  #Path of image
        img1=img1.resize((1530,152)) #Size of image
        self.img_1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.img_1)
        f_lbl.place(x=0,y=0,width=1530,height=152) #position of image
  
  

   #Image-2
  
        img2=Image.open(r"Image\fd_main.png")  #Path of image
        img2=img2.resize((410,536))
        self.img_2=ImageTk.PhotoImage(img2)  
        f_lbl=Label(self.root,image=self.img_2,bg="white")
        f_lbl.place(x=560, y=207, width=410, height=536,)
  
  
  #Image-3
  
        img3=Image.open(r"Image\back.png")  #Path of image
        img3=img3.resize((105,32))
        self.img_3=ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.img_3, bg="#2E75E9",fg="White",bd=0,activebackground="#2E75E9",cursor="hand2")
        b1.place(x=1374,y=61,width=105,height=32)
  
  #Button
        b1_bottom = ctk.CTkButton(self.root, text="Start Face Detection", font=("lato", 25,"bold"), fg_color="#2E75E9", hover_color="#1a5aa0", width=361, height=82,corner_radius=20,bg_color="#EBF3FA",command=self.face_recog)
        b1_bottom.place(x=584, y=640)
  
  











  #     #attendence
    def mark_attendance(self, i, r, n, d):
        with open("kiit.csv", "r+",newline="\n") as f:
            my_data_list = f.readlines()
            name_list = [entry.split(",")[0] for entry in my_data_list]
            if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines("\n{},{},{},{},{},{},".format(i, r, n, d, dtString, d1) + "Present")


    def face_recog(self):
            def draw_boundray(img,classifier,scaleFactor,minNeighbours,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

 
                coord=[]
            
                for (x,y,w,h) in features:
                   cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
                   id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                   confidence=int((100*(1-predict/300)))

                   conn=mysql.connector.connect(host="localhost",user="root",password="kiit",database="face_recognizer")
                   my_cursor=conn.cursor()
   
   
                   my_cursor.execute("select Name from student where student_id=" +str(id))
                   n=my_cursor.fetchone()
                   if n:
                        n = "+".join(n)
                   else:
                       n = "Unknown"
                   

                   
                  
                  
                  
                   my_cursor.execute("SELECT Roll FROM student WHERE student_id="+str(id))
                   r=my_cursor.fetchone()              
                   if r:
                        r = "+".join(r)
                   else:
                       r = "Unknown"
             

                
                   my_cursor.execute("select Dep from student where student_id="+str(id))
                   d=my_cursor.fetchone()                             
                   if d:
                        d = "+".join(d)
                   else:
                       d = "Unknown"
                   
                   my_cursor.execute("select student_id from student where Student_id="+str(id))
                   i=my_cursor.fetchone()                    
                   if i:
                        i = "+".join(i)
                   else:
                       i = "Unknown"
    
              

  




                   if confidence>77:
                        cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(i,r,n,d)
                   else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unkonwn Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              
                   coord=[x,y,w,h]
                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
        
            faceCascade=cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")
    

            video_cap=cv2.VideoCapture(0)
    
            while True:
               ret,img=video_cap.read()
               img=recognize(img,clf,faceCascade)
               cv2.imshow("Welcome To Face Recognition",img)
   
               if cv2.waitKey(1)==13:
                   break
            video_cap.release()
            cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root) 
    root.mainloop()     
