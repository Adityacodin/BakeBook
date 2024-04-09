import tkinter as tk 
import customtkinter as ctk
from PIL import ImageTk, Image
import sqlite3
import bcrypt
from tkinter import messagebox
import math


global next
def validate(username,passkey):
    flag = False
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE password = '+str(passkey))
    userFromdb = c.fetchone()
    if userFromdb != None and username == userFromdb[0]:
        flag = True
    conn.commit()
    conn.close()

    return flag

def get_info(user):
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()
    c.execute("SELECT * from user_baked_goods WHERE username = ?;",(user,))
    info = c.fetchall()
    conn.commit()
    conn.close()
    return info

def get_cakes(list):
    img_list = []
    for images in list:
        img_list.append(images[1])
    return img_list

def get_pastries(list):
    pass

def get_bread(list):
    pass

def get_inv(user):
    pass

def cake(user,master):
    cake_fm = ctk.CTkFrame(master)
    scroll_cake = ctk.CTkScrollableFrame(cake_fm,fg_color='white')
    scroll_cake.pack(fill='both',expand=True)
    info = get_info(user)
    img_list = get_cakes(info)
    print(img_list[0])
    size = len(img_list)
    # print(size)
    frame_no = math.ceil(size/3)
    # print(each_frame)
    count = len(img_list)
    k = 0
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_cake)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='green')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame)
        down.pack(side='bottom',fill = 'both',expand=True)

        for j in range(3):
            img = ctk.CTkImage(light_image=Image.open(img_list[count-1-k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            k+=1
            if k>count:
                break
        d = ctk.CTkFrame(down,fg_color ='red')
        d.pack()
        ctk.CTkLabel(d,text='cake names').pack(side='bottom')
    return cake_fm    

def pastry(user,master):
    pastry_fm = ctk.CTkFrame(master,fg_color='red')
    return pastry_fm

def bread(user,master):
    bread_fm = ctk.CTkFrame(master,fg_color='blue')
    return bread_fm    

def inv(user,master):
    inv_fm = ctk.CTkFrame(master,fg_color='green')
    return inv_fm


def switch(page,master):

    if not isinstance(page, ctk.CTkFrame) or not isinstance(master, ctk.CTkFrame):
        raise TypeError("Both 'page' and 'master' must be customtkinter CTkFrame widgets.")

    if not page.winfo_exists():
        page.pack(fill=ctk.BOTH, expand=True) 

    for child in master.children.values():
        child.pack_forget()

    page.pack(fill=ctk.BOTH, expand=True)

def inside(user):
    login_page.destroy()
    menu_page = ctk.CTkFrame(Main,fg_color="#D2B4DE")
    options = ctk.CTkFrame(menu_page,fg_color='white')
    options.pack(pady=5)
    options.pack_propagate(False)
    options.configure(width=600,height=35)

    display_frame = ctk.CTkFrame(menu_page,fg_color='#8E44AD')
    display_frame.pack(fill='both',expand=True)

    # menu options buttons
    cake_btn = ctk.CTkButton(options,text='Cakes',font=('Garamond Bold',13),fg_color='white',hover_color='white',text_color='#8E44AD',command = lambda: switch(cake(user,display_frame),display_frame))
    cake_btn.pack(side='left',pady = 5)
    # cake(userdisplay_frame)


        
    space1 = ctk.CTkLabel(options,text ='',bg_color='#8E44AD')
    space1.pack(side='left',padx=5)

    pastry_btn = ctk.CTkButton(options,text='Pastries',font=('Garamond Bold',13),fg_color='white',hover_color='white',text_color='#8E44AD',command = lambda : switch(pastry(user,display_frame),display_frame))
    pastry_btn.pack(side='left',pady=5)

    space2 = ctk.CTkLabel(options,text ='',bg_color='#8E44AD')
    space2.pack(side='left',padx=5)

    bread_btn = ctk.CTkButton(options,text='Breads & Toast',font=('Garamond Bold',13),fg_color='white',hover_color='white',text_color='#8E44AD',command = lambda: switch(bread(user,display_frame),display_frame))
    bread_btn.pack(side='left',pady=5)

    space3 = ctk.CTkLabel(options,text ='',bg_color='#8E44AD')
    space3.pack(side='left',padx=5)

    invent_btn = ctk.CTkButton(options,text='Inventory',font=('Garamond Bold',13),fg_color='white',hover_color='white',text_color='#8E44AD',command = lambda: switch(inv(user,display_frame),display_frame))
    invent_btn.pack(side='left',pady=5)    
    menu_page.pack(fill='both',expand=True)
    # root1.mainloop()

def nextStep(user,passk):
    if validate(user,passk):
        inside(user)
    else:
        messagebox.showerror('Error',"Invalid credentials")


def AddUser(parent,username,passk,cpass):
    flag = False
    if passk == cpass and (passk!=''and cpass!=''and username!=''):
        # encode_pass = passk.encode('utf-8')
        conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username,password) VALUES (?,?)",[username,passk])
        conn.commit()
        conn.close()
        flag = not flag

    if flag:
        messagebox.showinfo('Success','User has been registered')
    else :
        messagebox.showerror('Error','Registration Failed ')


    




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
        
        
    ctk.CTkButton(frame,text = 'Complete',fg_color='#A569BD',hover_color='#8E44AD',command = lambda: AddUser(frame,u.get(),p.get(),cp.get())).place(relx = 0.65,rely = 0.8,anchor=ctk.CENTER)
        

    
    R.mainloop()
okflag = False
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

passy = ctk.CTkEntry(login_page,placeholder_text='Passsword',show='*')
passy.place(relx=0.5,rely=0.57,anchor=ctk.CENTER)

ctk.CTkButton(login_page,text='Login',fg_color='#A569BD',hover_color='#8E44AD',command = lambda: nextStep(u_name.get(),passy.get())).place(relx=0.5,rely=0.7,anchor=ctk.CENTER)
ctk.CTkButton(login_page,text='Register',fg_color='#A569BD',hover_color='#8E44AD',command = reg).place(relx=0.5,rely=0.77,anchor=ctk.CENTER)

login_page.pack(expand=True,fill='both')
Main.pack(fill='both',expand=True)

root.mainloop()