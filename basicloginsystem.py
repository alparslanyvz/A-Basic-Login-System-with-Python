# // Login System with Python // alparslanyvz //
# Modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import *



#--------------------------------------------------------------------->

class loginSystem(): # Class
    def __init__(self) -> None:
        # Login information
        self.username = "admin"
        self.password = "admin123"
        #--------------------------------------------------------------
        self.mainFrameSize = "500x250+400+200" # width x height + x + y
        self.mainFrameTitle = "Login System"   # Frame title

        self.tryPassword = 3 # Right to try password
        self.main()
        
    def main(self):
        # CustomTkinter basic Frame commands;
        self.mainFrame = ctk.CTk() 
        self.mainFrame.geometry(self.mainFrameSize) # Frame size
        self.mainFrame.title(self.mainFrameTitle)   # Frame title
        # Items
        # Username entry box
        self.usernameEntry = CTkEntry(master=self.mainFrame,placeholder_text="Username",width=200,corner_radius=20,font=CTkFont(family="Arial",size=16))
        self.usernameEntry.place(x=150,y=70)
        # Password entry box
        self.passwordEntry = CTkEntry(master=self.mainFrame,placeholder_text="Password",show="*",width=200,corner_radius=20,font=CTkFont(family="Arial",size=16))
        self.passwordEntry.place(x=150,y=110)
        # Login button
        self.loginButton = CTkButton(master=self.mainFrame,text="Login",fg_color="blue",hover_color="green",corner_radius=20,font=CTkFont(family="Arial",size=16),width=200,command=self.login)
        self.loginButton.place(x=150,y=150)
        
        
        self.mainFrame.mainloop() # Show window command

    def login(self): # Login function
        self.usernameGet = self.usernameEntry.get()
        self.passwordGet = self.passwordEntry.get()
        if self.username == self.usernameGet:
            if self.password == self.passwordGet:
                self.mainFrame.destroy()
                self.main_menu()
            else:
                if self.tryPassword <= 0:
                    messagebox.showwarning("Wrong Password","You entered the wrong password 3 times. The application closes.")
                    self.mainFrame.destroy()
                else:
                    self.tryPassword = self.tryPassword - 1
                    print(self.tryPassword)
                    messagebox.showwarning("Invalid password",f"Wrong password. Try again\nRight to try password: {self.tryPassword}")
        else:
            messagebox.showwarning("Invalid User","User not found")

    def main_menu(self):
        self.main_menuFrame = ctk.CTk()
        self.main_menuFrame.geometry("500x250+400+200")
        self.main_menuFrame.title("Main Menu")
        # Main menu items
        self.welcomeMessages = CTkLabel(master=self.main_menuFrame,font=CTkFont(family="Arial",size=16),text_color="green",text=f"Welcome {self.username}",width=200)
        self.welcomeMessages.place(x=150,y=100)

        self.main_menuFrame.mainloop()

appExe = loginSystem() # Run the program
        