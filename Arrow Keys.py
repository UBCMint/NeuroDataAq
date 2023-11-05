import tkinter as tk
import keyboard
from PIL import Image, ImageTk

# Create a tkinter window
window = tk.Tk()
window.title("Arrow Key Image Display")
window.geometry("400x400")

# Create a tkinter canvas to display the arrow images
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create a dictionary to map arrow keys to their corresponding image file paths
arrow_key_mapping = {
    'up': 'images/Up.png',
    'down': 'images/Down.png',
    'left': 'images/Left.png',
    'right': 'images/Right.png'
}

arrow_images = {
    'images/Up.png': (150, 0),
    'images/Down.png': (150, 300), #
    'images/Left.png': (0, 150),
    'images/Right.png': (300, 150) #
}

# Function to update the canvas with the arrow image
def update_arrow_image(event):
    if event.name in arrow_key_mapping:
        x, y = arrow_images[arrow_key_mapping[event.name]]
        image_path = arrow_key_mapping[event.name]
        img = Image.open(image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)  # Adjust the size as needed
        img = ImageTk.PhotoImage(img)
        canvas.create_image(x, y, image=img, anchor=tk.NW)  # Use the canvas's create_image method
        canvas.image = img

# Register arrow key press events
for key in arrow_key_mapping:
    keyboard.on_press_key(key, update_arrow_image)

# Start the tkinter main loop
window.mainloop()
