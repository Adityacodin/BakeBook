import sqlite3;
import customtkinter as ctk 
import tkinter as tk 
from PIL import ImageTk, Image
def getinfoFromDb():
    conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/trial.db')
    info =[]
    c = conn.cursor()
    c.execute("SELECT * FROM IMAGES")
    info = c.fetchone()
    conn.commit()
    conn.close()
    new_win = ctk.CTk()
    new_win.geometry('300x300')
    new_frame = ctk.CTkFrame(new_win,fg_color='gray')
    new_frame.pack(fill='both',expand = True)
    logo = ctk.CTkImage(Image.open('C:/Users/33333333333333333333/gitdemo/BakeBook/cake_cj7_icon.ico'),size=(200,200))
    ctk.CTkLabel(new_frame,text='',image=logo).pack(side='top')

    # for names in info:
    #     ctk.CTkLabel(new_frame,text=names[0]).pack(side = 'left',padx = 10)

    new_win.mainloop()
    print(info)
    

root = ctk.CTk()
root.geometry('300x300')
main_fm = ctk.CTkFrame(root,fg_color = 'gray')
main_fm.pack(fill ='both',expand = True)
ctk.CTkButton(main_fm,text='get names from database',command =lambda: getinfoFromDb()).place(relx=0.5,rely=0.5,anchor = ctk.CENTER)


root.mainloop() 