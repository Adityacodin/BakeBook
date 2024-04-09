import sqlite3
import customtkinter as ctk 
import tkinter as tk 
from PIL import Image, ImageTk


def get_path():
    conn = sqlite3.connect("C:/Users/33333333333333333333/gitdemo/BakeBook/trial.db")
    c = conn.cursor()

    c.execute('''
    SELECT * FROM IMAGES;
    ''')
    info  = c.fetchall()
    conn.commit()
    conn.close()
    return info

root = ctk.CTk()
root.geometry('600x600')
root.resizable(width =False, height=False)
frame = ctk.CTkFrame(root,fg_color='gray')
frame.pack(fill='both',expand=True)
frames = ['red','blue','green']
# global frame_name
point5 = 0.4
image_paths = get_path()
print(image_paths)
count = 0
for i in range(3):
    
    frame_name = ctk.CTkFrame(frame,fg_color=frames[i])
    frame_name.pack(fill='both',expand = True)
    for j in range (3):
        img = ctk.CTkImage(light_image=Image.open(image_paths[count][0]),size=(100,100))
        ctk.CTkLabel(frame_name,text='',image=img).pack(side = 'left', padx = 5,expand=True)
        count+=1
root.mainloop()