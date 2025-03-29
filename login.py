import customtkinter as ctk  # Import customtkinter for modern UI elements
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Label  # We still need Tk and Label from tkinter for the window and image labels
from main import Home

class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Login page")
        

        # Use customtkinter CTkFrame for a modern frame appearance, specifying width and height in the constructor
        login_frame = ctk.CTkFrame(self.root, width=425, height=262, corner_radius=100, fg_color="white")  # Width and height are now specified here
        login_frame.place(x=966, y=369.51)
        
        # Labels and Entries (CTkLabel and CTkEntry for a modern look)
       

        self.username_entry = ctk.CTkEntry(login_frame, corner_radius=100,fg_color="white",width=325,height=40,placeholder_text="username",text_color="#3D3D3D")  # Rounded corners for the entry field
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
    

        self.password_entry = ctk.CTkEntry(login_frame, corner_radius=100, show="*",fg_color="white",width=325,height=40,placeholder_text="password",text_color="#3D3D3D")  # Rounded corners
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Login button (CTkButton for a modern button look)
        login_button = ctk.CTkButton(login_frame, text="Login",corner_radius=100, command=self.validate_login, fg_color="#31C975", text_color="white",width=325,height=40,font=('lato bold',20))
        login_button.grid(row=2, column=1, pady=10, sticky="e")
        
        
        

        # Set background color
        self.root.configure(bg="white") 

        # Load and display images
        self.load_and_display_images()
        
    def validate_login(self):
        valid_username = "1"
        valid_password = "1"
    
        if self.username_entry.get() == valid_username and self.password_entry.get() == valid_password:
         messagebox.showinfo("Login Successful", "You have logged in successfully.")
         self.main_window_open()
        else:
            messagebox.showerror("Invalid Credentials", "The username or password is incorrect.")

    def load_and_display_images(self):
        
        # Image-2
        img2 = Image.open(r"Image\login_left.png")
        img2 = img2.resize((840, 686))
        self.img_2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.img_2,bg="white")
        f_lbl.place(x=-13, y=95, width=840, height=686)
        
        # signup button (CTkButton for a modern button look)
        signup_button = ctk.CTkButton(self.root, text="Signup", corner_radius=100, fg_color="#4383EC", text_color="white", width=460, height=50,font=('lato bold',20),hover_color="#31C975")
        signup_button.place(x=205, y=581)
        

        
        
        #Image-3
  
        img3=Image.open(r"Image\login_right.png")  #Path of image
        img3=img3.resize((372,69))
        self.img_3= ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.img_3,bg="white")
        f_lbl.place(x=992.84,y=249,width=372,height=69)
        
        
        # Image-1
        img1 = Image.open(r"Image\login_title.png")
        img1 = img1.resize((1530, 124))
        self.img_1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.img_1,bg="white")
        f_lbl.place(x=0, y=0, width=1530, height=124)
        
        
def main_window_open(self):
    for widget in self.root.winfo_children():
    
     widget.destroy()
    self.app = Home(self.root)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Set the appearance mode (Light/Dark/System)
    root = Tk()
    obj = login(root)
    root.mainloop()
