import sqlite3
# import customtkinter as ctk 
# import tkinter as tk 
# from PIL import ImageTk, Image

# new_win = ctk.CTk()
# new_win.geometry('600x600')
# frame = ctk.CTkFrame(new_win,fg_color='#D2B4DE')
# frame.pack(fill='both',expand=True)

# new_win.mainloop()
conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
c = conn.cursor()

# c.execute("INSERT INTO cake VALUES ('aditya','Black Forest','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake1.jpg',0),('aditya','Red Velvet','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake2.jpg',0),('aditya','Chocolate Cake','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg',0)")

c.execute('SELECT * FROM cake')
print(c.fetchall())
conn.commit()
conn.close()

