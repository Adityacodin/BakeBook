import tkinter as tk 
import customtkinter as ctk
from PIL import ImageTk, Image
import sqlite3
import bcrypt
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
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

def get_info(user,dec):
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()
    if dec =='c':
        c.execute('''
        SELECT * FROM cakes WHERE user = ?
        ''',(user,))
    elif dec =='p':
        c.execute('''
        SELECT * FROM pastries WHERE user = ?
        ''',(user,))
    elif dec  == 'b':
        c.execute('''
        SELECT * FROM breads WHERE user = ?
        ''',(user,))

    info = c.fetchall()
    conn.commit()
    conn.close()
    return info

def get_name(lst):
    name_ls = []
    for entries in lst:
        name_ls.append(entries[1])
    return name_ls

def get_img(lst):
    img_ls = []
    for entries in lst:
        img_ls.append(entries[2])
    return img_ls

def get_price(lst):
    price_ls = []
    for entries in lst:
        price_ls.append(entries[4])
    return price_ls

def getInfo(product_name,dec):
    info = None
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')        
    c = conn.cursor()
    if dec == 'c':
        c.execute('SELECT cake_name,c_quant,price FROM cakes WHERE cake_name = ?',(product_name,))
        info = c.fetchone()
        if info[1] == 0:
            messagebox.showerror("Error",'Product is out of stock')
        else :
            c.execute('UPDATE cakes SET c_quant = ?-1 WHERE cake_name = ?',(info[1],product_name))
        conn.commit()
    elif dec == 'p':
        c.execute('SELECT pastry_name,p_quant,price FROM pastries WHERE pastry_name = ?',(product_name,))
        info = c.fetchone()
        if info[1] == 0:
            messagebox.showerror("Error",'Product is out of stock')
        else :
            c.execute('UPDATE pastries SET p_quant = ?-1 WHERE pastry_name = ?',(info[1],product_name))
        conn.commit()
    elif dec == 'b':
        c.execute('SELECT bread_name,b_quant,price FROM breads WHERE bread_name = ?',(product_name,))
        info = c.fetchone()
        if info[1] == 0:
            messagebox.showerror("Error",'Product is out of stock')
        else :
            c.execute('UPDATE breads SET b_quant = ?-1 WHERE bread_name = ?',(info[1],product_name))
        conn.commit()
    Cart(info[0],info[2])
    conn.close()

def Cart(name,price):
    cart.append((name,price))

def newCart():
    global cart
    cart = []
    return

customer_info = None
def send_userinfo(master,name,phone):
    if name == '':
        messagebox.showerror('Error','Name field is empty')
        master.destroy()
    elif phone == '':
        messagebox.showerror('Error','Phone field is empty')
        master.destroy()
    elif len(phone) > 10 or len(phone) < 10:
        messagebox.showerror('','Number invalid')
        master.destroy()
    else :
        customer_info = (name,phone)
        generateBill(customer_info,master)

def customer():
    win = ctk.CTk()
    win.geometry('200x200')
    fm = ctk.CTkFrame(win,fg_color='#D2B4DE')
    fm.pack(fill='both',expand = True)
    name = ctk.CTkEntry(fm, placeholder_text = 'Customer name')
    name.place(relx = 0.5, rely = 0.3,anchor = ctk.CENTER)
    phone = ctk.CTkEntry(fm,placeholder_text = 'Phone No.')
    phone.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)
    proceed_btn = ctk.CTkButton(fm,text='Proceed',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: send_userinfo(win,name.get(),phone.get()))
    proceed_btn.place(relx = 0.5, rely = 0.7, anchor = ctk.CENTER)
    close_btn = ctk.CTkButton(fm,text='Proceed',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: win.close())
    close_btn.place(relx = 0.5, rely = 0.9, anchor = ctk.CENTER)

    win.mainloop()



def generateBill(customer_info,master):
    if len(cart) == 0:
        messagebox.showinfo('Warning',"Cart is Empty")
    else:
        products = []
        price = []
        quant = []
        for item in cart:
            if item[0] in products:
                index = products.index(item[0])
                price[index] += item[1]
                quant[index] += 1
            else :
                products.append(item[0])
                price.append(item[1])
                quant.append(1)
        
        if customer_info != None:
            print("Customer Name:", customer_info[0])
            print("Phone Number:", customer_info[1])
            print("\n===================================")
            print("            YOUR BILL")
            print("===================================")
            print("Product        Quantity      Price")
            print("------------------------------------")
            for i in range(len(products)):
                print(f"{products[i]:<15} {quant[i]:<10} ${price[i]:.2f}")
            messagebox.showinfo('Success',"Receipt Successfully generated")
        else :
            messagebox.showerror('Error','Try again')

def cake(user,master):
    cake_fm = ctk.CTkFrame(master)
    scroll_cake = ctk.CTkScrollableFrame(cake_fm,fg_color='white')
    scroll_cake.pack(fill='both',expand=True)
    info = get_info(user,'c')
    img_ls = get_img(info)
    name_ls = get_name(info)
    price_ls = get_price(info)
    size = len(info)
    frame_no = math.ceil(size/3)
    # print(frame_no)
    count = len(info)    
    k = 0
    c_buttons = []
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_cake)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='#8E44AD')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame,fg_color='#AF7AC5')
        down.pack(side='bottom',fill = 'both',expand=True)
        for j in range(3):
            product_name = name_ls[k]
            img = ctk.CTkImage(light_image=Image.open(img_ls[k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            ctk.CTkLabel(down,text=product_name+'  '+str(price_ls[k])+'Rs').pack(side='left',pady = 10,padx = 20)
            c_buttons.append(ctk.CTkButton(down,text='Add',width=30,fg_color='#8E44AD',command = lambda name = product_name: getInfo(name,'c')))
            c_buttons[k].pack(side='left')
            k+=1
            if k>=size:
                break
    return cake_fm    

def pastry(user,master):
    pastry_fm = ctk.CTkFrame(master,fg_color='#D2B4DE')
    scroll_pastry = ctk.CTkScrollableFrame(pastry_fm,fg_color='white')
    scroll_pastry.pack(fill='both',expand=True)
    info = get_info(user,'p')
    img_ls = get_img(info)
    name_ls = get_name(info)
    price_ls = get_price(info)
    size = len(info)
    frame_no = math.ceil(size/3)
    k = 0
    p_buttons = []
    for i in range (0,frame_no):
        frame = ctk.CTkFrame(scroll_pastry)
        frame.pack(fill='both',expand=True)
        up = ctk.CTkFrame(frame,fg_color ='#8E44AD')
        up.pack(side='top',fill = 'both',expand=True)
        down = ctk.CTkFrame(frame,fg_color='#AF7AC5')
        down.pack(side='bottom',fill = 'both',expand=True)

        for j in range(3):
            product_name = name_ls[k]
            img = ctk.CTkImage(light_image=Image.open(img_ls[k]),size=(100,100))
            ctk.CTkLabel(up,text='',image=img).pack(side='left',pady = 10,padx =40)
            ctk.CTkLabel(down,text=product_name+'  '+str(price_ls[k])+'Rs').pack(side='left',pady = 10,padx = 20)
            p_buttons.append(ctk.CTkButton(down,text='Add',width=30,fg_color='#8E44AD',command=lambda name=product_name: getInfo(name,'p')))
            p_buttons[k].pack(side='left')
            k+=1
            if k>=size:
                break

    return pastry_fm


def bread(user, master):
    bread_fm = ctk.CTkFrame(master, fg_color='blue')
    scroll_bread = ctk.CTkScrollableFrame(bread_fm, fg_color='white')
    scroll_bread.pack(fill='both', expand=True)
    info = get_info(user, 'b')
    img_ls = get_img(info)
    name_ls = get_name(info)
    price_ls = get_price(info)
    size = len(img_ls)
    frame_no = math.ceil(size / 3)
    k = 0
    b_buttons = []
    for i in range(0, frame_no):
        frame = ctk.CTkFrame(scroll_bread)
        frame.pack(fill='both', expand=True)
        up = ctk.CTkFrame(frame, fg_color='#8E44AD')
        up.pack(side='top', fill='both', expand=True)
        down = ctk.CTkFrame(frame, fg_color='#AF7AC5')
        down.pack(side='bottom', fill='both', expand=True)
        for j in range(3):
            product_name = name_ls[k]
            img = ctk.CTkImage(light_image=Image.open(img_ls[k]), size=(100, 100))
            ctk.CTkLabel(up, text='', image=img).pack(side='left', pady=10, padx=40)
            ctk.CTkLabel(down, text=product_name+'  '+str(price_ls[k])+'Rs').pack(side='left', pady=10, padx=20)
            b_buttons.append(ctk.CTkButton(down, text='Add', width=30,fg_color = '#A569BD',hover_color='#8E44AD', command=lambda name=product_name: getInfo(name,'b')))
            b_buttons[k].pack(side='left')
            k += 1
            if k >= size:
                break
    return bread_fm

def disp_contents(window,product):
    product_name = None
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()
    info = None
    if product == 'c':
        c.execute('''SELECT cake_name,c_quant FROM cakes''')
        info = c.fetchall()
        conn.commit()
    elif product == 'p':
        c.execute('''SELECT pastry_name,p_quant FROM pastries''')
        info = c.fetchall()
        conn.commit()
    elif product == 'b':
        c.execute('''SELECT bread_name,b_quant FROM breads''')
        info = c.fetchall()
        conn.commit()
    conn.close()
    table = ttk.Treeview(window,columns=('prod_name','Quantity'),show='headings')
    table.heading('prod_name',text = 'Product')
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

def mixedletters(master,quant):
    for i in range(len(quant)):
            if quant[i].isalpha():
                return True
    return False

def add_items(window,user,name,quant,dec):
    flag = None
    if '.' in quant:
        messagebox.showerror('Error','Entered a fractional value')
        window.destroy()
    elif quant.isalpha() or mixedletters(window,quant):
        messagebox.showerror('Error','Only numerical values allowed')
        window.destroy()
    else:
        units = int(quant)
        conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
        c = conn.cursor()
        if dec == 'c':
            c.execute('SELECT c_quant FROM cakes WHERE user = ? AND cake_name = ?',(user,name))
            q = c.fetchone()[0]
            print(q)
            c.execute('''
            UPDATE cakes
             SET c_quant = ?
            WHERE user = ? AND cake_name = ?;
            ''',(q+units,user,name))

        elif dec == 'p':
            c.execute('SELECT p_quant from pastries WHERE user = ? AND pastry_name = ?',(user,name))
            q = c.fetchone()[0]
            c.execute('''
            UPDATE pastries
            SET p_quant = ?
            WHERE user = ? AND pastry_name = ?;
            ''',(q+units,user,name))

        elif dec == 'b':
            c.execute('SELECT b_quant FROM breads WHERE user = ? AND bread_name = ?',(user,name))
            q = c.fetchone()[0]
            c.execute('''
            UPDATE breads
            SET b_quant = ?
            WHERE user = ? AND bread_name = ?;
            ''',(q+units,user,name))
        conn.commit()
        conn.close()
        messagebox.showinfo('Success','Item quantity updated in the inventory')

def update_inv(user):
    new_win = ctk.CTk()
    main = ctk.CTkFrame(new_win,fg_color='#D2B4DE')
    new_win.geometry('500x400')
    new_win.title('Update Inventory')
    c_info = get_info(user,'c')
    c_name = get_name(c_info)
    p_info = get_info(user,'p')
    p_name = get_name(p_info)
    b_info = get_info(user,'b')
    b_name = get_name(b_info)

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

    cake_box = ctk.CTkComboBox(cake_tab,values = c_name)
    cake_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    cake_units = ctk.CTkEntry(cake_tab, placeholder_text = 'Units',width = 50)
    cake_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_c = ctk.CTkButton(cake_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(new_win,user,cake_box.get(),cake_units.get(),'c'))
    add_c.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 
 
    pastry_box = ctk.CTkComboBox(pastry_tab,values = p_name)
    pastry_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    pastry_units = ctk.CTkEntry(pastry_tab, placeholder_text = 'Units',width = 50)
    pastry_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_p = ctk.CTkButton(pastry_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(new_win,user,pastry_box.get(),pastry_units.get(),'p'))
    add_p.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 

    bread_box = ctk.CTkComboBox(bread_tab,values = b_name)
    bread_box.place(relx = 0.3, rely = 0.3, anchor = ctk.CENTER)
    bread_units = ctk.CTkEntry(bread_tab, placeholder_text = 'Units',width = 50)
    bread_units.place(relx = 0.7,rely = 0.3, anchor = ctk.CENTER)
    add_b = ctk.CTkButton(bread_tab,text='Add',hover_color = '#D2B4DE',fg_color='#A569BD',command = lambda:add_items(new_win,user,bread_box.get(),bread_units.get(),'b'))
    add_b.place(relx = 0.5,rely = 0.5, anchor = ctk.CENTER) 

    ctk.CTkButton(main,text='Done',command = lambda: done(new_win),fg_color = '#A569BD',hover_color='#8E44AD').pack(side='bottom',pady = 10)
    main.pack(fill='both',expand=True)
    new_win.mainloop()

def refresh(user,master,s1,s2,big_m):
    s1.destroy()
    s2.destroy()
    inv(user,big_m)

def save_img(user,master,item_name,price,radio_var):
    img_path = filedialog.askopenfilename()
    ctk.CTkLabel(master,text = 'Image added succesfully').place(relx = 0.7, rely = 0.8 ,anchor =ctk.CENTER)
    add = ctk.CTkButton(master,text = 'Add',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda:Add(user,item_name,img_path,price,radio_var))
    add.place(relx = 0.5,rely = 0.9, anchor = ctk.CENTER)


def Add(user,item,img,price,dec):
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
    c = conn.cursor()

    if dec == 'c':
        c.execute('INSERT INTO cakes VALUES (?,?,?,0,?)',(user,item,img,price))
    elif dec == 'p':
        c.execute('INSERT INTO pastries VALUES (?,?,?,0,?)',(user,item,img,price))
    elif dec == 'b':
        c.execute('INSERT INTO breads VALUES (?,?,?,0,?)',(user,item,img,price))

    conn.commit()
    conn.close()


def add_new_item(user):
    new_win = ctk.CTk()
    new_win.geometry('500x400')
    new_win.resizable(width = False,height=False)
    main_fm = ctk.CTkFrame(new_win,fg_color='#D2B4DE')
    main_fm.pack(fill='both',expand = True)
    item_name_lb = ctk.CTkLabel(main_fm,text = 'Add Item name : ')
    item_name_lb.place(relx = 0.3,rely = 0.2, anchor=ctk.CENTER)
    item_name = ctk.CTkEntry(main_fm)
    item_name.place(relx = 0.6,rely = 0.2,anchor =ctk.CENTER)
    item_category_lb = ctk.CTkLabel(main_fm,text = 'Item Category : ')
    item_category_lb.place(relx = 0.3, rely = 0.4,anchor = ctk.CENTER)
    radio_var = ctk.StringVar(value = 'other')
    c = ctk.CTkRadioButton(main_fm,text = 'Cake',value = 'c',variable = radio_var)
    c.place(relx = 0.7, rely = 0.4, anchor = ctk.CENTER)
    p = ctk.CTkRadioButton(main_fm,text = 'Pastry',value = 'p',variable = radio_var)
    p.place(relx = 0.7, rely = 0.5, anchor = ctk.CENTER)
    b = ctk.CTkRadioButton(main_fm,text = 'Breads',value = 'b',variable = radio_var)
    b.place(relx = 0.7, rely = 0.6, anchor = ctk.CENTER)
    price_lb = ctk.CTkLabel(main_fm,text = 'Price of the Item : ')
    price_lb.place(relx = 0.3, rely = 0.7, anchor = ctk.CENTER)
    price = ctk.CTkEntry(main_fm,placeholder_text='Price',width = 40)
    price.place(relx = 0.7, rely = 0.7, anchor = ctk.CENTER)
    img_lb = ctk.CTkLabel(main_fm,text = 'Image of the item : ')
    img_lb.place(relx = 0.3, rely = 0.8, anchor =ctk.CENTER)
    img_btn = ctk.CTkButton(main_fm, text = 'Select',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: save_img(user,main_fm,item_name.get(),int(price.get()),radio_var.get()))
    img_btn.place(relx = 0.7, rely = 0.8 ,anchor =ctk.CENTER)
    
    new_win.mainloop()


def scroll_cont(user,master,s1,s2,big_m):
    scroll = ctk.CTkScrollableFrame(master,fg_color='#8E44AD')
    scroll.pack(fill='both',expand = True)
    refresh_btn = ctk.CTkButton(scroll,text='Refresh ',hover_color = '#D2B4DE',fg_color='#A569BD',width = 40,command = lambda: refresh(user,master,s1,s2,big_m))
    refresh_btn.pack(side = 'top',padx = 10, pady = 10)
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
    update_button = ctk.CTkButton(menu_fm,text = 'Update Inventory',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda : update_inv(user),width = 50)
    update_button.place(relx = 0.2, rely = 0.5,anchor = ctk.CENTER)
    add_new = ctk.CTkButton(menu_fm,text='Add New Item',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: add_new_item(user),width = 50)
    add_new.place(relx = 0.4, rely = 0.5,anchor = ctk.CENTER)
    new_cart = ctk.CTkButton(menu_fm,text='New Cart',fg_color = '#A569BD',hover_color='#8E44AD',command = newCart,width = 50)
    new_cart.place(relx = 0.6, rely = 0.5,anchor = ctk.CENTER)
    gen_bill = ctk.CTkButton(menu_fm,text='Generate Bill',fg_color = '#A569BD',hover_color='#8E44AD',command = lambda: customer(), width = 50)
    gen_bill.place(relx = 0.8, rely = 0.5,anchor = ctk.CENTER)


    menu_fm.pack(side = 'bottom',pady=5)
    menu_fm.pack_propagate(False)
    menu_fm.configure(width=600,height=50) 
    scroll_fm = ctk.CTkFrame(inv_fm)
    scroll_fm.pack(fill='both',expand =True)
    scroll_cont(user,scroll_fm,inv_fm,menu_fm,master)
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

    new_cart = ctk.CTkButton(display_frame,text = 'New Cart',font=('Garamond Bold',13),fg_color='white',hover_color='light gray',text_color='#8E44AD',command = newCart)
    new_cart.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

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
root.geometry('700x600')
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