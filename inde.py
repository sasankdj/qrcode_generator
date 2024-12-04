import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.save("qrcode.png")

        # Display the QR code on the GUI
        img = Image.open("qrcode.png")
        img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Use LANCZOS for resizing
        qr_tk_image = ImageTk.PhotoImage(img)

        qr_label.config(image=qr_tk_image)
        qr_label.image = qr_tk_image  # Keep reference to prevent garbage collection
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initialize the main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")

# Add a label for instructions
label = tk.Label(root, text="Enter URL:", font=("Arial", 12))
label.pack(pady=10)

# Add a text entry box
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Add a button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", font=("Arial", 12), command=generate_qr)
generate_button.pack(pady=10)

# Add a label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=20)

# Run the application
root.mainloop()
