import tkinter as tk
from PIL import Image, ImageTk, ImageGrab
import keyboard
import time
from io import BytesIO
import pytesseract
from pytube import YouTube

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path

def take_screenshot():
    # Simulate the windows shortcut of Win + Shift + S keypress
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

        # Extract text using OCR
        text = pytesseract.image_to_string(screenshot)

        # Check if the extracted text is a valid YouTube URL
        if text.startswith("youtube.com/") or text.startswith("https://m.youtube.com/"):
            download_youtube_video(text)
        else:
            # Convert the resized screenshot to Tkinter PhotoImage format
            screenshot_image = ImageTk.PhotoImage(screenshot)

            # Update the label with the new resized screenshot and extracted text
            screenshot_label.config(image=screenshot_image)
            screenshot_label.image = screenshot_image  # Keep a reference to avoid garbage collection

            # Display the extracted text above the resized image
            text_label.config(text=text)

def download_youtube_video(url):
    try:
        # Download YouTube video
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()  # Downloads to the current working directory by default
        success_text = f"Video '{yt.title}' downloaded successfully."
        text_label.config(text=success_text)

    except Exception as e:
        error_text = f"Error: {str(e)}"
        text_label.config(text=error_text)

# Create the main window
root = tk.Tk()
root.title("Screenshot Display")
root.geometry("600x600")

# Create a button to trigger the screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=(20, 0), side="top", anchor="center")

# Create a label to display the resized screenshot
screenshot_label = tk.Label(root)
screenshot_label.pack(pady=(20, 0))

# Create a label to display the extracted text
text_label = tk.Label(root, text="")
text_label.pack(pady=(10, 0))

# Run the GUI loop
root.mainloop()
