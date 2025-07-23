import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
from stegano import lsb

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

background = "grey"
file_types = [("PNG files", "*.png")]
file_path = ""


def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=file_types)
    if file_path:
        image = Image.open(file_path)
        max_size = (240, 240)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        label_image = ImageTk.PhotoImage(image)
        PhotoLabel.configure(image=label_image)
        PhotoLabel.image = label_image

def encrypt():
    data = Data_entry.get(1.0, "end").strip()
    if file_path and data:
        encrypted_image = lsb.hide(file_path, data)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encrypted_image.save(save_path)
            messagebox.showinfo("Success", "Message encrypted in image successfully!")
            Data_entry.delete(1.0, "end")
        else:
            messagebox.showwarning("Save Cancelled", "Save operation was cancelled.")
    else:
        messagebox.showwarning("Error", "Please select an image and enter a message to encrypt.")

def decrypt():
    global file_path
    if file_path:
        try:
            message = lsb.reveal(file_path)
            Data_entry.delete(1.0, "end")
            if message:
                Data_entry.insert(1.0, message)
                messagebox.showinfo("Success", "Message decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"No hidden message found in the image.")
    else:
        messagebox.showwarning("No File", "Please select an image file first.")

root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.configure(fg_color=background)
root.title("Message Encoder")

##########       Loading Images      ############

logo = ctk.CTkImage(Image.open('logo.png'), size=(100, 100))
sender = Image.open('logo.jpg')
sender = sender.resize((240, 240))
label_image = ImageTk.PhotoImage(sender)

open_file = ctk.CTkImage(Image.open('open_file.png'), size=(70, 70))
encrypt_image = ctk.CTkImage(Image.open('encryption.png'), size=(60, 70))
decrypt_image = ctk.CTkImage(Image.open('decrypt.png'), size=(60, 70))
orchids_image = ctk.CTkImage(Image.open('OIS.png'), size=(100, 100))

##################################################

# Create frames for layout
top_frame = ctk.CTkFrame(root, fg_color=background, height=80)
top_frame.pack(fill="x", pady=5)

middle_frame = ctk.CTkFrame(root, fg_color=background)
middle_frame.pack(fill="both", expand=True)

bottom_frame = ctk.CTkFrame(root, fg_color=background, height=100)
bottom_frame.pack(fill="x")

# Top frame content
logo_image = ctk.CTkLabel(top_frame, image=logo, text="", fg_color=background)
logo_image.pack(side="left", padx=(10, 0))

message_label = ctk.CTkLabel(top_frame, text="Message Encrypter", font=("Cascadia Code SemiBold", 20, "bold"), fg_color=background, text_color="white")
message_label.pack(side="left", padx=10)

orchids = ctk.CTkLabel(top_frame, image=orchids_image, text="", fg_color=background)
orchids.pack(side="left", padx=(150, 10))

# Middle frame content - split into left and right
left_middle = ctk.CTkFrame(middle_frame, fg_color=background, width=260)
left_middle.pack(side="left", padx=(10, 5), fill="both")

right_middle = ctk.CTkFrame(middle_frame, fg_color=background)
right_middle.pack(side="right", padx=(5, 10), fill="both", expand=True)

# Photo in left middle frame
PhotoLabel = ctk.CTkLabel(left_middle, image=label_image, text="", width=247, height=247, fg_color="white")
PhotoLabel.pack(pady=10)

# Text entry in right middle frame
Data_entry = ctk.CTkTextbox(right_middle, width=250, height=200, border_width=5)
Data_entry.pack(fill="both", expand=True, pady=10)

# Button layout in bottom frame
buttons_container = ctk.CTkFrame(bottom_frame, fg_color=background)
buttons_container.pack(fill="x", expand=True, pady=15)

open_button = ctk.CTkButton(buttons_container, image=open_file, text="", fg_color=background, hover_color=background, command=open_image)
open_button.pack(side="left", expand=True)

encrypt_button = ctk.CTkButton(buttons_container, image=encrypt_image, text="", fg_color=background, hover_color=background, command=encrypt)
encrypt_button.pack(side="left", expand=True)

decrypt_button = ctk.CTkButton(buttons_container, image=decrypt_image, text="", fg_color=background, hover_color=background, command=decrypt)
decrypt_button.pack(side="left", expand=True)

root.mainloop()
