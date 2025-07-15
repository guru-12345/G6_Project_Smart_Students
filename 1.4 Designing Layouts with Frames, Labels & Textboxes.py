# Task1: Create a right-side frame inside the middle_frame similar to left_middle frame.

# 🔍 Hint 1: Use CTkFrame and set its parent to middle_frame.
# 🔍 Hint 2: Set fg_color=background to match the window color.
# 🔍 Hint 3: Use .pack(side="right", padx=(5, 10), fill="both", expand=True) to position and resize the frame properly.


#Task 2: Add a Textbox to Type Your Message inside right_middle frame
#       You need to create a box where you can type a secret message.
#       🔹 Name it: Data_entry
#       🔹 Size: width = 250, height = 200
#       🔹 Border width: 5 (so the box has a visible border)
#       🔹 Use .pack(fill="both", expand=True,pady=10) to position and resize the frame properly.

import customtkinter as ctk
from PIL import Image, ImageTk 

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


logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100)) 
orchids_image = ctk.CTkImage(Image.open('OIS.png'), size=(100, 100))

sender = Image.open('logo.jpg') # Open the image 'logo.jpg' to use it in the program
sender = sender.resize((240, 240)) # Resize the image to be 240 pixels wide and 240 pixels tall
label_image = ImageTk.PhotoImage(sender) # Convert the resized image into a format that Tkinter can use

#Top frame content
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=background)
logo_image.pack(side="left", padx=(10, 0))

message_label = ctk.CTkLabel(top_frame, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.pack(side="left", padx=100)

orchids = ctk.CTkLabel(top_frame, image=orchids_image, text="", fg_color=background)
orchids.pack(side="left", padx=(10, 10))

# Middle frame content - split into left and right
left_middle = ctk.CTkFrame(middle_frame, fg_color=background, width=260)
left_middle.pack(side="left", padx=(10, 5), fill="both")

#Create a right_middle frame here




# Create a label in the window to display the image with no text, and set its size and color
PhotoLabel = ctk.CTkLabel(left_middle, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.pack(pady=10)


#create a textbox here 




root.mainloop()
