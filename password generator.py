from ast import Delete
from tkinter import*
import string
import random
import pyperclip

#FUNCTION FOR GENERATING PASSWORD
def generator():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    all = small_letters + capital_letters + numbers + special_characters
    password_length = int(passwordfield.get())
    
    password = random.sample(all,password_length)
    GenerateField.insert(0,password)

#FUNCTION FOR ACCEPTING
def accept():
    random_password= GenerateField.get()
    pyperclip.copy(random_password)

#FUNCTION FOR DELETING
def reset():
    GenerateField.delete(0,END)
    passwordField.delete(0,END)
    nameField.delete(0,END)


root = Tk()
root.title("password generator")
root.geometry("350x350")
root.config(bg="yellow")

#PASSWORD TEXT
passwordlabel=Label(root,text="PASSWORD GENERATOR",font=("times new roman","15","bold"))
passwordlabel.grid(pady=1)

#USER LABEL
userlabel=Label(root,text="Enter user name:",font=("times new roman","15","bold"),bg="White",fg="black")
userlabel.grid(padx=2,pady=10)
nameField=Entry(root,width=30,font=("times new roman","15","bold"))
nameField.grid(padx=20)

#PASSWORD LENGTH
password_label=Label(root,text="Password length:",font=("times new roman","15","bold"),bg="White",fg="Black")
password_label.grid(padx=2,pady=10)
passwordfield=Entry(root,width=30,font=("times new roman","15","bold"))
passwordfield.grid(padx=20)

#GENERATE TEXT
Generate_label=Label(root,text="Generated: ",font=("times new roman","15","bold"),bg="White",fg="Black")
Generate_label.grid(padx=2,pady=10)
GenerateField=Entry(root,width=30,font=("times new roman","15","bold"))
GenerateField.grid(padx=20)

#GENERATE BUTTON
Generatebutton=Button(root,text="GENERATE",font=("times of roman","15","bold"),bg="black",fg="White",command=generator)
Generatebutton.grid(padx=20,pady=10)

#ACCEPT BUTTON
Acceptbutton=Button(root,text="ACCEPT",font=("times new roman","15","bold"),bg="GREEN",fg="white",command=accept)
Acceptbutton.grid(padx=20,pady=10)

#RESET BUTTON
resetbutton=Button(root,text="RESET",font=("times new roman","15","bold"),bg="RED",fg="White",command=reset)
resetbutton.grid(padx=20,pady=10)


root.mainloop()   