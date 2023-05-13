# =======> Login System <=========

from tkinter import *
from tkinter import ttk

# Take Object From Tkinter Module
root = Tk()

# Main Screen Configuration (Width And Height And Style)
root.geometry('500x500+320+200')
root.configure(background='#1c1f28')
# Title Program
root.title('Login System')
# Prevent The User For Control Width And Height
root.resizable(False,False)
# Set The Programming Icon
root.iconbitmap('./login.ico')
# The Header Of Program (Title)
Header = Label(root,text='LOGIN SYSTEM',bg='Black',fg='White',font=10)
Header.pack(fill=X)
# Main Frame
mainFrame = Frame(root,width='350',height='375',background='White')
mainFrame.place(x=75,y=70)
# Password Encryption Logo
PasswordLogo = PhotoImage (file="D:\\Ziad\\programming\\Projects\\Python\\Login-System-GUI\\PWLogo.png")
pwlogoLabel = Label (root,image=PasswordLogo)
pwlogoLabel.place(x=185,y=70)
# Labels And Inputs
username = Entry(mainFrame,width='25',bg='White',fg='Black',font=('Tajawal',11))
username.place(x=100,y=150)
userlabel = Label (mainFrame,text='Username :',bg='White',fg='Black',font=('Tajawal',13))
userlabel.place(x=10,y=150)
password = Entry(mainFrame,width='25',bg='White',fg='Black',font=('Tajawal',11))
password.place(x=100,y=180)
passlabel = Label (mainFrame,text='Password :',bg='White',fg='Black',font=('Tajawal',13))
passlabel.place(x=10,y=180)
email = Entry(mainFrame,width='25',bg='White',fg='Black',font=('Tajawal',11))
email.place(x=100,y=210)
emaillabel = Label (mainFrame,text='E-mail :',bg='White',fg='Black',font=('Tajawal',18))
emaillabel.place(x=10,y=210)
# Checkbox Forgot Password
checkforgot = ttk.Checkbutton(mainFrame,text='Forgot Password .!!')
checkforgot.place(x=100,y=250)
# Login - Signup Buttons
loginbutton = Button(mainFrame,text='LOGIN',width='15',justify='center',fg='Black',bg='Aqua',font=('Tajawal',13))
loginbutton.place(x=20,y=290)
signupbutton = Button(mainFrame,text='Signup',width='15',justify='center',fg='Black',bg='#841414',font=('Tajawal',13))
signupbutton.place(x=180,y=290)
# Copy Right
copyrightTM = Label(root,text='This Program Developed By Ziad,Wael @2023',font=('Tajawal',16),fg='White',background='#ff69b4')
copyrightTM.place(x=30,y=460)
# Main Loop
root.mainloop()