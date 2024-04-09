import sqlite3
import customtkinter as ctk 
import tkinter as tk 
from PIL import ImageTk, Image

new_win = ctk.CTk()
new_win.geometry('600x600')
frame = ctk.CTkFrame(new_win,fg_color='#D2B4DE')
frame.pack(fill='both',expand=True)

new_win.mainloop()