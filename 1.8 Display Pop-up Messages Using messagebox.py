# On line 32 get the message from the text box 
# (starting from line 1, char 0 to the end)
# On line 41 show a warning if no image is selected or message is missing.

#Task 1: Uncomment line 36 & write the code to hide the message 
#        in the image using:lsb.hide(file_path,data)

import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox  # Import tools to open files
from stegano import lsb #Import the lsb(Least Significant Bit) module from stegano for hiding and revealing messages in images
file_types = [("PNG files", "*.png")]   # Set allowed file type to only PNG images
file_path = ""   # Create an empty variable to store the selected file path

def open_image():
    global file_path
    #Open image file
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=file_types)

    if file_path:
        # Open and resize the image
        image = Image.open(file_path)
        max_size = (240, 240)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)

        # Convert to Tkinter-compatible image and update PhotoLabel
        label_image = ImageTk.PhotoImage(image)
        PhotoLabel.configure(image=label_image)
        PhotoLabel.image = label_image  # Keep reference to avoid garbage collection
        
def encryption():
    data = Data_entry.get(1.0, "end").strip() #Get the message from the text box
    #Check if an image is selected
    if file_path:
        # ✅ TASK: Use lsb.hide() to hide the message in the image
        # encrypted_image = ...
        # Ask the user where to save the new image
        messagebox.showinfo("Success", "Message encrypted in image successfully!")
    else:
        # Show a warning if no image was selected
        messagebox.showwarning("Error", "Please select an image and enter a message to encrypt.")


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
encrypt= ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
decrypt= ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))

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
open_button = ctk.CTkButton(buttons_container, image=open_file, text="", fg_color=frame_background, hover_color=frame_background,command=open_image)
open_button.pack(side="left",padx = 25)  # Places the open_button on the left side of its container with horizontal padding of 25 pixels.

#Encrypt_Button:
encrypt_button = ctk.CTkButton(buttons_container, image=encrypt, text="", fg_color=frame_background, hover_color=frame_background,command=encryption)
encrypt_button.pack(side="left",padx = 25)


#Decrypt_Button:
decrypt_button = ctk.CTkButton(buttons_container, image=decrypt, text="", fg_color=frame_background, hover_color=frame_background,)
decrypt_button.pack(side="left",padx = 25)

root.mainloop()
