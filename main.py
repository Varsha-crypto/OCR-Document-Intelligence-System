# main.py
import os
import json
import matplotlib.pyplot as plt
from config import FOLDER_PATH, OUTPUT_FOLDER
from image_processing import process_image
from ocr_extraction import send_ocr_request

# Get all images from the `images/` folder
image_files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

if not image_files:
    print("No image files found.")
else:
    for image_file in image_files:
        image_path = os.path.join(FOLDER_PATH, image_file)
        processed_image, label_filename = process_image(image_path)

        if processed_image is not None:
            extracted_data = send_ocr_request(processed_image, image_file)

            if extracted_data:
                json_filename = os.path.join(OUTPUT_FOLDER, f"{os.path.splitext(image_file)[0]}.json")

                 # Ensure output directory exists before saving
                os.makedirs(OUTPUT_FOLDER, exist_ok=True)

                # Save JSON output inside VS Code's "output/" folder
                with open(json_filename, "w", encoding="utf-8") as json_file:
                    json.dump(extracted_data, json_file, indent=4, ensure_ascii=False)

                print(f" JSON saved: {json_filename}")

                # Display JSON data in VS Code output
                print("\n==== Extracted JSON Data ====")
                print(json.dumps(extracted_data, indent=4, ensure_ascii=False))

                # Show extracted JSON in a text window
                plt.figure(figsize=(6, 4))
                plt.text(0, 1, json.dumps(extracted_data, indent=4, ensure_ascii=False),
                         fontsize=10, wrap=True, verticalalignment='top', family='monospace')
                plt.axis('off')
                plt.title(f"Extracted JSON for {image_file}")
                plt.show()

print(f"Processing images from: {FOLDER_PATH}")
print(f"Saving outputs to: {OUTPUT_FOLDER}")
