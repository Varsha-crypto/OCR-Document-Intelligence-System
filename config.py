import os

API_KEY = "YOUR API KEY"

# Use your actual folder path for images
FOLDER_PATH = r"C:\Users\varsh\Downloads\uploads"


# Define output folder inside the same location
OUTPUT_FOLDER = os.path.join(FOLDER_PATH, "output")  # Output folder for images and JSON

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)