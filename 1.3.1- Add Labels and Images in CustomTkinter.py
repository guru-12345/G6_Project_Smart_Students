# Line no 40 loads and resizes the logo.png image to 100×100 pixels using CTkImage for use in a CustomTkinter app.

# Line 46 & 47 creates a label (CTkLabel) in the top_frame to display the logo image without any text and with a 
# frame_background color, then places it on the left side with padding.

# Task1: Create a label that says "Message Encrypter" on the top frame.

#  Hint - 1: Use CTkLabel to create the label.
#  Hint - 2: Set text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), text_color="white", fg_color=background.
#  Hint - 3: Use .pack(side="left", padx=(70,0)) to place the label with some left padding.
#  Hint - 4: Store the label object in a variable named message_label. 

# Task2: Display an image on the top frame using CTkLabel.

# Hint - 1: Use CTkLabel with image=orchids_image, text="", and fg_color=frame_background.
# Hint - 2: Position it with .pack(side="left", padx=(10, 20)).
# Hint - 3: Store the label object in a variable named orchids.


import customtkinter as ctk
from PIL import Image, ImageTk  # A library to work with pictures

frame_background = "dimgrey" 
root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Message Encoder")

# Create frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

middle_frame = ctk.CTkFrame(root, fg_color=frame_background)
middle_frame.pack(fill="both", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=frame_background, height=100)
bottom_frame.pack(fill="x")

##########       Loading Images      ############
logo = ctk.CTkImage(Image.open('logo.png'), size=(120, 120))  #Open the image and set its size

#load image for task 2 


## Create a label with the logo image, no text, and pack it on the window.
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=frame_background)
logo_image.pack(side="left", padx=(25, 0))

#Create a label that says "Message Encrypter" here





#Create a label with the orchids_logo image, no text, and pack it on the window here similar to logo_image.






root.mainloop()
