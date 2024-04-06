import customtkinter as ctk 
import tkinter as tk
from PIL import ImageTk, Image

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("light")


class Login(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        

class Main():
    def __init__(self,master):
        mainFrame = ctk.CTkFrame(master,fg_color='#F1C40F')
        mainFrame.pack(padx = 10,pady=10,fill = 'both',expand=True)


        self.my_img = ctk.CTkImage(light_image=Image.open('C:/Users/33333333333333333333/gitdemo/BakeBook/cake_cj7_icon.ico'),size=(200,400))
        label = ctk.CTkLabel(mainFrame,text='',image=self.my_img)
        label.pack()

        self.Label = ctk.CTkLabel(mainFrame,text ='Bake-Book',font=('Cooper Black',24))
        self.Label.pack(padx =10,pady = 10)

        ctk.CTkButton(mainFrame,fg_color = '#E67E22',text='Login').pack(padx = 10, pady = 10)
        ctk.CTkButton(mainFrame,fg_color='#E67E22', text='Register').pack(padx =10, pady = 10)



root = ctk.CTk()
root.title('Bake-Book')
root.geometry('600x600')
win = Main(root)
root.mainloop()