# Run the code and observe the output
# In line 22 We are creating a top frame (like a box at the top of the window)
# It has a background color, a fixed height of 80, and a small gap (pady) below it
# 'fill="x"' means it stretches across the width of the window

#Task1:- Create the middle frame
# 👉 Hint: Use CTkFrame with fg_color as background
# 👉 Hint: Use pack() with fill="both" and expand=True so it stretches and grows

#Task2:-Create the bottom frame
# 👉 Hint: Set height=100 when creating the frame
# 👉 Hint: Use pack() with fill="x" so it stretches across the bottom
import customtkinter as ctk

frame_background = "dimgrey"  # Stores the color name 'dimgrey' to be used as the background color for frames
root = ctk.CTk()
root.geometry("600x500")
root.resizable(False, False)
root.title("Message Encoder")

# Create top_frame for layout
top_frame = ctk.CTkFrame(root, fg_color=frame_background, height=80)
top_frame.pack(fill="x", pady=5)

#Create middle_frame here for layout



#Create bottom_frame here for layout



root.mainloop()
