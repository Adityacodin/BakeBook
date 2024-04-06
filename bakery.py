import tkinter as tk 
import customtkinter as ctk
from PIL import ImageTk, Image
import sqlite3

def validate(username,passkey):
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()

    c.execute('SELECT * FROM USER WHERE PASSKEY = ' + str(passkey))
    userFromdb = c.fetchone()
    if userFromdb == None or username != userFromdb[0]:
        print("username not in the database")
    elif username == userFromdb[0]:
        print(f"{userFromdb[0]} is in the database")

    conn.commit()
    conn.close()

def AddUser(parent,username,passk,cpass):
    flag = False
    if passk == cpass and (passk!=''and cpass!=''and username!=''):
        conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO USER (U_NAME,PASSKEY) VALUES ('{username}',{int(passk)});")
        conn.commit()
        conn.close()
        flag = not flag

    if flag:
        ctk.CTkLabel(parent,text='Registration Successfull').pack(side='bottom',pady=20)
    else :
        ctk.CTkLabel(parent,text='Registration unsuccessful,,try again').pack(side='bottom',pady=20)


    




def reg():
    R = ctk.CTk()
    R.geometry('400x400')
    R.title('Bake-Book Registration')
    frame = ctk.CTkFrame(R,fg_color='#D2B4DE')
    frame.pack(fill='both',expand=True)

    ctk.CTkLabel(frame,text='Enter your username : ').place(relx=0.3,rely=0.5,anchor=ctk.CENTER)
    u = ctk.CTkEntry(frame,placeholder_text='Username')
    u.place(relx = 0.65,rely=0.5,anchor = ctk.CENTER)

    ctk.CTkLabel(frame,text='Set a Password : ').place(relx=0.3,rely=0.6,anchor=ctk.CENTER)
    p = ctk.CTkEntry(frame,placeholder_text='Password')
    p.place(relx = 0.65,rely=0.6,anchor = ctk.CENTER)

    ctk.CTkLabel(frame,text='Confirm Password : ').place(relx=0.3,rely=0.7,anchor=ctk.CENTER)
    cp = ctk.CTkEntry(frame,placeholder_text='Confirm Password')
    cp.place(relx = 0.65,rely=0.7,anchor = ctk.CENTER)
        
        
    ctk.CTkButton(frame,text = 'Complete',fg_color='#A569BD',hover_color='#D2B4DE',command = lambda: AddUser(frame,u.get(),p.get(),cp.get())).place(relx = 0.65,rely = 0.8,anchor=ctk.CENTER)
        

    
    R.mainloop()


root = ctk.CTk()
root.geometry('600x600')
root.title("Bake-Book")

Main = ctk.CTkFrame(root,fg_color='white')

login_page = ctk.CTkFrame(Main,fg_color="#D2B4DE")
logo = ctk.CTkImage(light_image=Image.open('C:/Users/33333333333333333333/gitdemo/BakeBook/cake_cj7_icon.ico'),size=(200,200))
ctk.CTkLabel(login_page,text='',image=logo).pack(side='top')

ctk.CTkLabel(login_page,text='Bake-Book',font=('Garamond bold',24)).pack(side='top')
ctk.CTkLabel(login_page,text='Manage your bakery like a piece of cake :)',font=('Garamand bold',14)).pack(side='top')

u_name = ctk.CTkEntry(login_page,placeholder_text='Username')
u_name.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

passy = ctk.CTkEntry(login_page,placeholder_text='Passsword')
passy.place(relx=0.5,rely=0.57,anchor=ctk.CENTER)

ctk.CTkButton(login_page,text='Login',fg_color='#A569BD',hover_color='#D2B4DE',command = lambda: validate(u_name.get(),passy.get())).place(relx=0.5,rely=0.7,anchor=ctk.CENTER)
ctk.CTkButton(login_page,text='Register',fg_color='#A569BD',hover_color='#D2B4DE',command = reg).place(relx=0.5,rely=0.77,anchor=ctk.CENTER)

login_page.pack(expand=True,fill='both')
Main.pack(fill='both',expand=True)

bottom = ctk.CTkFrame(root)
Back = ctk.CTkButton(bottom,text='Back',font=('Garamond Bold',14),fg_color='#A569BD')
Back.pack(side='left',padx = 10)

Next = ctk.CTkButton(bottom,text='Next',font=('Garamond Bold',14),fg_color='#A569BD')
Next.pack(side='left',padx = 10)
bottom.pack(side='bottom',pady=10)
root.mainloop()