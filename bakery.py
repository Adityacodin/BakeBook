import tkinter as tk 
import customtkinter as ctk
from PIL import ImageTk, Image
import sqlite3
import bcrypt
from tkinter import messagebox
from tkinter import ttk
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
        img_list.append(images[2])
    return img_list

def get_names(list,n):
    name_list = []
    for names in list:
        name_list.append(names[n])
    return name_list

def get_pastries(list):
    img_list = []
    for images in list:
        img_list.append(images[4])
    return img_list

def get_bread(list):
    img_list = []
    for images in list:
        img_list.append(images[6])
    return img_list

def get_inv(list,n):
    new_ls = []
    for names in list:
        new_ls.append(names[n])
    return new_ls

def cake(user,master):
    cake_fm = ctk.CTkFrame(master)
    scroll_cake = ctk.CTkScrollableFrame(cake_fm,fg_color='white')
    scroll_cake.pack(fill='both',expand=True)
    info = get_info(user)
    img_list = get_cakes(info)
    name_ls = get_names(info, 3)
    name_ls.reverse()
    print(name_ls)
    # print(img_list[1])
    size = len(img_list)
    # print(size)
    frame_no = math.ceil(size/3)
    # print(each_frame)
    count = len(img_list)
    k = 0
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_cake)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='#8E44AD')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame,fg_color='#AF7AC5')
        down.pack(side='bottom',fill = 'both',expand=True)

        for j in range(3):
            img = ctk.CTkImage(light_image=Image.open(img_list[count-1-k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            ctk.CTkLabel(down,text=name_ls[k]).pack(side='left',pady = 10,padx = 30)
            ctk.CTkButton(down,text='Add',width=30,fg_color='#8E44AD').pack(side='left')
            k+=1
            if k>=count:
                break

        
    return cake_fm    

def pastry(user,master):
    pastry_fm = ctk.CTkFrame(master,fg_color='#D2B4DE')
    scroll_pastry = ctk.CTkScrollableFrame(pastry_fm,fg_color='white')
    scroll_pastry.pack(fill='both',expand=True)
    info = get_info(user)
    img_list = get_pastries(info)
    name_ls = get_names(info, 5)
    name_ls.reverse()
    print(name_ls)
    print(img_list[0])
    size = len(img_list)
    # print(size)
    frame_no = math.ceil(size/3)
    # print(each_frame)
    count = len(img_list)
    k = 0
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_pastry)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='#8E44AD')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame,fg_color='#AF7AC5')
        down.pack(side='bottom',fill = 'both',expand=True)

        for j in range(3):
            img = ctk.CTkImage(light_image=Image.open(img_list[count-1-k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            ctk.CTkLabel(down,text=name_ls[k]).pack(side='left',pady = 10,padx = 30)
            ctk.CTkButton(down,text='Add',width=30,fg_color='#8E44AD').pack(side='left')
            k+=1
            if k>=count:
                break

    return pastry_fm

def bread(user,master):
    bread_fm = ctk.CTkFrame(master,fg_color='blue')
    scroll_bread = ctk.CTkScrollableFrame(bread_fm,fg_color='white')
    scroll_bread.pack(fill='both',expand=True)
    info = get_info(user)
    img_list = get_bread(info)
    name_ls = get_names(info, 7)
    name_ls.reverse()
    print(name_ls)
    print(img_list[0])
    size = len(img_list)
    # print(size)
    frame_no = math.ceil(size/3)
    # print(each_frame)
    count = len(img_list)
    k = 0
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_bread)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='#8E44AD')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame,fg_color='#AF7AC5')
        down.pack(side='bottom',fill = 'both',expand=True)

        for j in range(3):
            img = ctk.CTkImage(light_image=Image.open(img_list[count-1-k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            ctk.CTkLabel(down,text=name_ls[k]).pack(side='left',pady = 10,padx = 30)
            ctk.CTkButton(down,text='Add',width=30,fg_color='#8E44AD').pack(side='left')
            k+=1
            if k>=count:
                break
    return bread_fm

def disp_contents(window,product):
    product_name = None
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()
    info = None
    if product == 'c':
        product_name = 'Cakes'
        c.execute('''SELECT cake_name,c_qaunt FROM user_baked_goods''')
        info = c.fetchall()
        conn.commit()
    elif product == 'p':
        product_name = 'Pastries'
        c.execute('''SELECT patry_name,p_quant FROM user_baked_goods''')
        info = c.fetchall()
        conn.commit()
    elif product == 'b':
        product_name = 'Breads and Toast'
        c.execute('''SELECT bread_name,b_quant_integer FROM user_baked_goods''')
        info = c.fetchall()
        conn.commit()
    conn.close()
    table = ttk.Treeview(window,columns=('prod_name','Quantity'),show='headings')
    table.heading('prod_name',text = product_name)
    table.heading('Quantity',text = 'Quantity')
    for i in range(len(info)):
        data = info[i]
        table.insert(parent='',index = 0, values = data)
    table.pack()

def get_quant(list,n):
    quant = []
    for items in list:
        quant.append(items[n])
    return quant

def add_items(user,name,quant,dec):
    units = int(quant)
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()
    if dec == 'c':
        c.execute('''
        UPDATE user_baked_goods
        SET c_qaunt = ?
        WHERE username = ? AND cake_name = ?;
        ''',(units,user,name))
    elif dec == 'p':
        c.execute('''
        UPDATE user_baked_goods
        SET p_quant = ?
        WHERE username = ? AND patry_name = ?;
        ''',(units,user,name))
    elif dec == 'b':
        c.execute('''
        UPDATE user_baked_goods
        SET b_quant_integer = ?
        WHERE username = ? AND bread_name = ?;
        ''',(units,user,name))
    conn.commit()
    conn.close()

def update_inv(user):
    new_win = ctk.CTk()
    main = ctk.CTkFrame(new_win,fg_color='#D2B4DE')
    new_win.geometry('500x400')
    new_win.title('Update Inventory')
    info = get_info(user)
    cake = get_names(info, 3)
    cake_quant = get_quant(info, 8)
    pastry = get_names(info, 5)
    pastry_quant = get_quant(info, 9)
    bread = get_names(info, 7)
    bread_quant = get_quant(info, 10)
    Tab = ctk.CTkTabview(main,fg_color='#8E44AD',
    segmented_button_fg_color='#8E44AD',
    segmented_button_selected_color='#D2B4DE',
    segmented_button_unselected_color='#8E44AD',
    segmented_button_selected_hover_color='#D2B4DE',
    segmented_button_unselected_hover_color='#8E44AD')
    Tab.pack(padx = 10, pady = 10,fill = 'both',expand = True)
    cake_tab = Tab.add('Cake')
    pastry_tab = Tab.add('Pastry')
    bread_tab = Tab.add('Breads')

    cake_box = ctk.CTkComboBox(cake_tab,values = cake)
    cake_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    cake_units = ctk.CTkEntry(cake_tab, placeholder_text = 'Units',width = 50)
    cake_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_c = ctk.CTkButton(cake_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(user,cake_box.get(),cake_units.get(),'c'))
    add_c.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 
 
    pastry_box = ctk.CTkComboBox(pastry_tab,values = pastry)
    pastry_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    pastry_units = ctk.CTkEntry(pastry_tab, placeholder_text = 'Units',width = 50)
    pastry_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_p = ctk.CTkButton(pastry_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(user,pastry_box.get(),pastry_units.get(),'p'))
    add_p.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 

    bread_box = ctk.CTkComboBox(bread_tab,values = bread)
    bread_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    bread_units = ctk.CTkEntry(bread_tab, placeholder_text = 'Units',width = 50)
    bread_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_b = ctk.CTkButton(bread_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(user,bread_box.get(),bread_units.get(),'b'))
    add_b.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 

    ctk.CTkButton(main,text='Done',command = lambda: done(new_win),fg_color = '#A569BD',hover_color='#8E44AD').pack(side='bottom',pady = 10)
    main.pack(fill='both',expand=True)
    new_win.mainloop()

def scroll_cont(master):
    scroll = ctk.CTkScrollableFrame(master,fg_color='#8E44AD')
    scroll.pack(fill='both',expand = True)
    ctk.CTkLabel(scroll,text='Cakes',font=('Garamond Bold',25),text_color='#D2B4DE').pack(side='top',padx = 10, pady = 10)
    disp_contents(scroll,'c')
    ctk.CTkLabel(scroll,text='Pastries',font=('Garamond Bold',25),text_color='#D2B4DE').pack(side='top',padx = 10, pady = 10)
    disp_contents(scroll,'p')
    ctk.CTkLabel(scroll,text='Breads and Toast',font=('Garamond Bold',25),text_color='#D2B4DE').pack(side='top',padx = 10, pady = 10)
    disp_contents(scroll,'b')

def inv(user,master):
    inv_fm = ctk.CTkFrame(master,fg_color='#D2B4DE')
    inv_fm.pack(side = 'bottom', fill='both',expand = True)
    menu_fm = ctk.CTkFrame(inv_fm,fg_color = '#D2B4DE')
    update_button = ctk.CTkButton(menu_fm,text = 'Update Inventory',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda : update_inv(user))
    update_button.place(relx = 0.4, rely = 0.5,anchor = ctk.CENTER)
    add_new = ctk.CTkButton(menu_fm,text='Add New Item',fg_color = '#A569BD',hover_color='#8E44AD')
    add_new.place(relx = 0.7, rely = 0.5,anchor = ctk.CENTER)
    menu_fm.pack(side = 'bottom',pady=5)
    menu_fm.pack_propagate(False)
    menu_fm.configure(width=600,height=50) 
    scroll_fm = ctk.CTkFrame(inv_fm)
    scroll_fm.pack(fill='both',expand =True)
    scroll_cont(scroll_fm)
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
        messagebox.showerror('Error',"Invalid c#D2B4DEentials")

def AddUser(R,parent,username,passk,cpass):
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
        messagebox.showinfo('Success','User has been registe#D2B4DE')
        R.destroy()
        # get_started()
    else :
        messagebox.showerror('Error','Registration Failed ')

def reg():
    R = ctk.CTk()
    R.geometry('600x600')
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
        
        
    ctk.CTkButton(frame,text = 'Complete',fg_color='#A569BD',hover_color='#8E44AD',command = lambda: AddUser(R,frame,u.get(),p.get(),cp.get())).place(relx = 0.65,rely = 0.8,anchor=ctk.CENTER)
        

    
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