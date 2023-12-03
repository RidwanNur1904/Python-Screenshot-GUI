import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import keyboard
import time
from io import BytesIO


def take_screenshot():
    # Simulate Win + Shift + S keypress
    keyboard.press('win+shift+s')

    # Wait for a moment to allow the screenshot region selection
    time.sleep(0.5)

    # Release the keys
    keyboard.release('win+shift+s')

    # Wait for another moment to allow the screenshot to be taken
    time.sleep(1)

    # Get the screenshot image
    screenshot = ImageGrab.grabclipboard()

    if screenshot:
        # Convert the screenshot to Tkinter PhotoImage format
        screenshot_image = ImageTk.PhotoImage(screenshot)

        # Update the label with the new screenshot
        screenshot_label.config(image=screenshot_image)
        screenshot_label.image = screenshot_image  # Keep a reference to avoid garbage collection


# Create the main window
root = tk.Tk()
root.title("Screenshot Display")
root.geometry("1000x1000")

# Create a button to trigger the screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=(20, 0), side="top", anchor="center")

# Create a label to display the screenshot
screenshot_label = tk.Label(root)
screenshot_label.pack(pady=(20, 0))

# Run the GUI loop
root.mainloop()