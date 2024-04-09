import tkinter as tk
import customtkinter as ct
from PIL import Image, ImageTk
import sqlite3  # Assuming you're using sqlite3

# Database connection details (replace with your actual connection details)
db_name = "C:/Users/3333333333333;3333333/gitdemo/BakeBook/trial.db"
table_name = "IMAGES"
image_path_column = "img_path"

# Create the main window
root = ct.CTk()
root.geometry("500x300")  # Adjust window size as needed

# Function to retrieve image path from database
def get_image_path(num):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Modify query if you have additional criteria for selecting image path
    query = f"SELECT {image_path_column} FROM {table_name} WHERE id ="+str(num)
    cursor.execute(query)

    # Fetch the image path (assuming only one image record)
    image_path = cursor.fetchone()[0]

    conn.close()
    return image_path

# Function to display the image
def display_image():
    image_path = get_image_path(4)
    if image_path:
        try:
            # Load the image
           logo = ct.CTkImage(light_image=Image.open(image_path),size=(100,100))
           ct.CTkLabel(root,text='',image=logo).pack(side='top')
            # Create a label to display the image
            
        except FileNotFoundError:
            # Handle error if image file is not found
            error_label = ct.CTkLabel(master=root, text="Image not found!", text_color="red")
            error_label.pack(padx=20, pady=20)
    else:
        # Handle case if no image path is found in the database
        info_label = ct.CTkLabel(master=root, text="No image data found!", text_color="gray")
        info_label.pack(padx=20, pady=20)

# Call the display function
display_image()

# Start the main event loop
root.mainloop()
