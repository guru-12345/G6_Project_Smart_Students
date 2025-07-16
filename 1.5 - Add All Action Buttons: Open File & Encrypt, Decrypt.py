# On line 49 loads and resizes the 'open_file.png' image to 70×70 pixels using 
# CTkImage for use in a CustomTkinter widget.



#Task - 1:Load encrypt.png and decrypt.png images just like you did for open_file.png.
#     Hint 1: Use encrypt.png and decrypt.png with CTkImage (size: 60x70).
#     Hint 2: Create CTkButton using these images.
#     Hint 3: Add these images in line 50 & 51.

#Task  - 2: Add two image buttons (Encrypt & Decrypt) inside buttons_container.
#     Hint_1: Use CTkButton for both buttons.
#     Hint_2: Use encrypt_image and decrypt_image.
#     Hint_3: Set text="", fg_color=background, hover_color=background.
#     Hint_4: Use .pack(side="left",padx = 25) to align side by side.

#(Refer to how the Open Image button is created and placed. 
# Now, in the respective lines, add the Encrypt and Decrypt buttons similarly)


import customtkinter as ctk
from PIL import Image, ImageTk


frame_background = "dimgrey"
root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Message Encoder")

##################################################

# Creating 3 frames for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

middle_frame = ctk.CTkFrame(root, fg_color=frame_background)
middle_frame.pack(fill="both", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=frame_background, height=100)
bottom_frame.pack(fill="x")

##########       Loading Images      ############

logo = ctk.CTkImage(Image.open('logo.png'), size=(120, 120)) 
orchids_image = ctk.CTkImage(Image.open('OIS.png'), size=(100, 100))

# Loads and resizes 'open_file.png' to 70x70 for use in CustomTkinter.
open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
 
 
 
sender = Image.open('logo.jpg') 
sender = sender.resize((240, 240))
label_image = ImageTk.PhotoImage(sender) 


#Top frame content
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=frame_background)
logo_image.pack(side="left", padx=(10, 0))

message_label = ctk.CTkLabel(top_frame, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=frame_background, text_color="white")
message_label.pack(side="left", padx=70)

orchids = ctk.CTkLabel(top_frame, image=orchids_image, text="", fg_color=frame_background)
orchids.pack(side="left", padx=(10, 20))

# Middle frame content - split into left and right
left_middle = ctk.CTkFrame(middle_frame, fg_color=frame_background, width=260)
left_middle.pack(side="left", padx=(25, 5), fill="both")

right_middle = ctk.CTkFrame(middle_frame, fg_color=frame_background)
right_middle.pack(side="left", padx=(5, 25), fill="both")

PhotoLabel = ctk.CTkLabel(left_middle, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.pack(pady=10)

Data_entry = ctk.CTkTextbox(right_middle, width=247, height=247,)
Data_entry.pack(fill="both", expand=True, pady=10)

# Botton frame content - Open,encrypt and decrypt buttons

# Creates a bottom frame to hold buttons with background color.
buttons_container = ctk.CTkFrame(bottom_frame, fg_color=frame_background)
# Expands the frame horizontally with some vertical padding.
buttons_container.pack(fill="x", expand=True, pady=15)


# Creates a button with an image (open_file) inside 
# 'buttons_container' to open an image when clicked.
open_button = ctk.CTkButton(buttons_container, image=open_file, text="", fg_color=frame_background, hover_color=frame_background,)
open_button.pack(side="left",padx = 25)  # Places the open_button on the left side of its container with horizontal padding of 25 pixels.

#Encrypt_Button:



#Decrypt_Button:




root.mainloop()
