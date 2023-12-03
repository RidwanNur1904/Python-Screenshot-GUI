# Screenshot and YouTube Video Downloader

This Python script utilizes the `tkinter` library for creating a simple graphical user interface (GUI) application to take screenshots and download YouTube videos. The application allows users to capture a screenshot of a selected region, extract text from the screenshot using Optical Character Recognition (OCR), and download YouTube videos if the extracted text is a valid YouTube URL.

## Requirements

Ensure you have the required libraries installed before running the script:

- **tkinter**: GUI toolkit for creating the application window.
- **PIL (Pillow)**: Image processing library for working with screenshots.
- **keyboard**: Library for simulating keypress events.
- **time**: Standard Python library for adding delays.
- **pytesseract**: OCR library for extracting text from images.
- **pytube**: Library for downloading YouTube videos.

You also need to set the correct path to the Tesseract executable (`tesseract_cmd`) in the script:

```python
# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path
```

## How to Use

1. **Run the script.**
2. A GUI window titled "Screenshot Display" will appear.
3. **Click the "Take Screenshot" button** to capture a screenshot of a selected region.
4. The script will extract text using OCR and display the resized screenshot along with the extracted text.
5. If the extracted text is a valid YouTube URL, **the script will attempt to download the corresponding video.**

*Note: Ensure you have an active internet connection for YouTube video downloads to work.*

## GUI Components

- **Take Screenshot Button:** Initiates the screenshot capture process.
- **Resized Screenshot Display:** Shows the captured screenshot resized to a maximum of 500x500 pixels.
- **Extracted Text Display:** Displays the text extracted from the screenshot or error messages.

## Important Information

- Ensure Tesseract OCR is installed, and its executable path is correctly set.
- The YouTube video is downloaded to the current working directory by default.

## Dependencies

- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [keyboard](https://github.com/boppreh/keyboard)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [pytube](https://python-pytube.readthedocs.io/en/latest/)

