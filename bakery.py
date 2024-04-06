import tkinter as tk 
import customtkinter as ctk
from PIL import ImageTk, Image

root = ctk.CTk()
root.geometry('600x600')
root.title("Bake-Book")

Main = ctk.CTkFrame(root,fg_color='white')

login_page = ctk.CTkFrame(Main,fg_color="#D2B4DE")
logo = ctk.CTkImage(light_image=Image.open('C:/Users/33333333333333333333/gitdemo/BakeBook/cake_cj7_icon.ico'),size=(200,200))
ctk.CTkLabel(login_page,text='',image=logo).pack(side='top')

ctk.CTkLabel(login_page,text='Bake-Book',font=('Garamond bold',24)).pack(side='top')
ctk.CTkLabel(login_page,text='Manage your bakery like a piece of cake :)',font=('Garamand bold',14)).pack(side='top')

ctk.CTkEntry(login_page,placeholder_text='Username').place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
ctk.CTkEntry(login_page,placeholder_text='Passsword').place(relx=0.5,rely=0.57,anchor=ctk.CENTER)
ctk.CTkButton(login_page,text='Login',fg_color='#A569BD',hover_color='#D2B4DE').place(relx=0.5,rely=0.7,anchor=ctk.CENTER)
ctk.CTkButton(login_page,text='Register',fg_color='#A569BD',hover_color='#D2B4DE').place(relx=0.5,rely=0.77,anchor=ctk.CENTER)

login_page.pack(expand=True,fill='both')
Main.pack(fill='both',expand=True)

bottom = ctk.CTkFrame(root)
Back = ctk.CTkButton(bottom,text='Back',font=('Garamond Bold',14),fg_color='#A569BD')
Back.pack(side='left',padx = 10)

Next = ctk.CTkButton(bottom,text='Next',font=('Garamond Bold',14),fg_color='#A569BD')
Next.pack(side='left',padx = 10)
bottom.pack(side='bottom',pady=10)
root.mainloop()