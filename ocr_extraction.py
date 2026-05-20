# ocr_extraction.py
import base64
import json
import cv2
from groq import Groq
from config import API_KEY

# Initialize Groq API client
client = Groq(api_key=API_KEY)

def encode_image(image):
    """Encodes an image to Base64 format."""
    _, encoded_img = cv2.imencode('.jpg', image)
    return base64.b64encode(encoded_img.tobytes()).decode("utf-8")

def send_ocr_request(image, image_filename):
    """Sends an image to Groq OCR API and returns extracted text."""
    base64_image = encode_image(image)

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                },
                {
                    "type": "text",
                     "text": (
                            f"Analyze the image {image_filename} and extract the following information accurately. "
                            "Extract Hindi, Urdu, and Bengali text with high accuracy. "
                            "Ensure that extracted text is structured properly even if it is handwritten or stylized. "
                            "Focus on:\n\n"
                            "1. **Publisher**: Identify the publisher name.\n"
                            "2. **Film Name**: Extract the movie name.\n"
                            "3. **Catalog Number**: Identify any catalog number.\n"
                            "4. **Matrix Number**: Extract the matrix number.\n"
                            "5. **Movie Banner**: Identify the production house or banner.\n"
                            "6. **Music Director**: Retrieve the music director’s name.\n"
                            "7. **Lyricist**: Extract the lyricist's name.\n"
                            "8. **Text by Language**:\n"
                            "- Hindi text in Devanagari script.\n"
                            "- Urdu text in Perso-Arabic (Nastaliq) script.\n"
                            "- Bengali text in Bengali script.\n"
                            "Ensure that Hindi, Urdu, and Bengali text are separated properly.\n"
                            "Return only valid JSON, without extra explanations."
                    )
                }
            ]
        }
    ]

    try:
        # Send request to Groq API
        completion = client.chat.completions.create(
            model="llama-3.2-90b-vision-preview",
            messages=messages,
            temperature=0.2,
            max_completion_tokens=3730
        )

        # Extract response
        extracted_data = completion.choices[0].message.content

        # Print raw API response to debug
        print(f"Raw API Response for {image_filename}:\n{extracted_data}\n")

        # Validate JSON
        try:
            extracted_json = json.loads(extracted_data)
            return extracted_json  # Return the parsed JSON data
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON response for {image_filename}")
            return None

    except Exception as e:
        print(f"Error processing {image_filename}: {e}")
        return None