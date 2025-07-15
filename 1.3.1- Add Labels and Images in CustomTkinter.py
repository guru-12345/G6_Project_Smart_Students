# Task1: Create a label that says "Message Encrypter" on the top frame.

# 🔍 Hint 1: Use CTkLabel to create the label.
# 🔍 Hint 2: Set text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), text_color="white", fg_color=background.
# 🔍 Hint 3: Use .pack(side="left", padx=(10,0)) to place the label with some left padding.

# Task2: Display an image on the top frame using CTkLabel.

# 🔍 Hint 1: Use CTkImage to load and resize the image. Use: Image.open("OIS.png"), size=(100, 100)
# 🔍 Hint 2: Use CTkLabel to place the image. Set image=your_image, text="", fg_color=background
# 🔍 Hint 3: Use .pack(side="left", padx=(150, 10)) to position the image with proper spacing.


import customtkinter as ctk
from PIL import Image, ImageTk  # A library to work with pictures

background = "grey" 
root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Message Encoder")

# Create frames for layout
top_frame = ctk.CTkFrame(root, fg_color=background, height=80)
top_frame.pack(fill="x", pady=5)

middle_frame = ctk.CTkFrame(root, fg_color=background)
middle_frame.pack(fill="both", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=background, height=100)
bottom_frame.pack(fill="x")

##########       Loading Images      ############
logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100))  #Open the image and set its size

#load image for task 2 


## Create a label with the logo image, no text, and pack it on the window.
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=background)
logo_image.pack(side="left", padx=(10, 0))

#Create a label that says "Message Encrypter" here



#Create a label with the orchids_logo image, no text, and pack it on the window here similar to logo_image.






root.mainloop()
