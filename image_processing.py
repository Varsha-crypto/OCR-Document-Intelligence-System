# image_processing.py
import cv2
import numpy as np
import os
from config import OUTPUT_FOLDER

def extract_center_label(image):
    """Extracts the center part (label) of a gramophone record."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)  # Reduce noise
    edges = cv2.Canny(blurred, 50, 150)  # Detect edges

    # Find circles using Hough Transform
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=50, param2=30, minRadius=100, maxRadius=500)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        x, y, r = circles[0][0]

        # Crop circular region
        mask = np.zeros_like(gray)
        cv2.circle(mask, (x, y), r, 255, -1)
        result = cv2.bitwise_and(image, image, mask=mask)

        # Crop bounding box
        x1, y1 = max(0, x - r), max(0, y - r)
        x2, y2 = min(image.shape[1], x + r), min(image.shape[0], y + r)
        cropped_label = result[y1:y2, x1:x2]

        return cropped_label
    else:
        print("No circle detected. Returning original image.")
        return image


def process_image(image_path):
    """Loads and processes an image."""
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image - {image_path}")
        return None, None

    label_img = extract_center_label(img)

    # Check if label_img is valid
    if label_img is None or label_img.size == 0:
        print(f"Error: Label extraction failed for {image_path}")
        return None, None

    # Ensure output directory exists before saving
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(OUTPUT_FOLDER, os.path.basename(image_path).replace(".jpg", "_label.jpg"))
    
    success = cv2.imwrite(output_path, label_img)

    if success:
        print(f" Saved extracted label image: {output_path}")
    else:
        print(f"Failed to save image: {output_path}")

    return label_img, output_path