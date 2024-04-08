import customtkinter  # Assuming you have customtkinter installed
from PIL import Image, ImageTk
import sqlite3  # Assuming you're using sqlite3 for the database
import os  # For path manipulation (optional)

# Connect to your database (replace with your actual path)
try:
    conn = sqlite3.connect("YOUR_DATABASE_PATH.db")
    cursor = conn.cursor()
except sqlite3.Error as e:
    print("Error connecting to database:", e)
    exit()

# Define function to fetch image paths
def get_image_paths():
    try:
        cursor.execute("SELECT path FROM IMAGE")  # Replace with your table/column name
        return [os.path.join(IMAGE_DIRECTORY, row[0]) for row in cursor.fetchall()]  # Construct full paths (optional)
    except sqlite3.Error as e:
        print("Error fetching image paths:", e)
        return []  # Return empty list on error

# Function to display images horizontally
def display_images():
    image_paths = get_image_paths()
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(fill="both", expand=True)

    row_count = 0
    image_count_in_row = 0

    # Loop through image paths and display them
    for i, path in enumerate(image_paths):
        try:
            img = Image.open(path)
            img = img.resize((200, 150))  # Adjust width and height as needed
            img = ImageTk.PhotoImage(img)
            label = customtkinter.CTkLabel(frame, image=img)

            # Check if image count in current row reaches the limit (adjust as needed)
            if image_count_in_row >= 3:
                row_count += 1
                image_count_in_row = 0

            # Pack the label with consideration for row number
            label.pack(side="left", padx=5, pady=5, **{"in": frame, "row": row_count})

            image_count_in_row += 1
        except (FileNotFoundError, sqlite3.Error) as e:
            print("Error processing image:", path, e)  # Handle specific error messages

# Initialize main window
root = customtkinter.CTk()
root.geometry("600x600")  # Adjust window size as needed
root.resizable(width=True, height=True)

# Call display_images function
display_images()

root.mainloop()

# Close database connection (recommended in a finally block)
conn.close()
