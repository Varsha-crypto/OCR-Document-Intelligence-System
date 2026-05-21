# OCR-Document-Intelligence-System

## Overview

Developed an OCR-based document intelligence pipeline using **LLaMA via Groq API** to transform unstructured image data into structured JSON outputs.
The system combines image preprocessing, OCR enhancement, and prompt-engineered LLM workflows for accurate data extraction from noisy and complex document images.



## Features

* Extracts structured JSON data from unstructured image inputs
* Uses **LLaMA models via Groq API** for intelligent text understanding
* Image preprocessing using **OpenCV**
* Contour detection and circular region extraction
* Noise reduction and image enhancement pipeline
* Prompt engineering for consistent LLM responses
* Converts visual document content into machine-readable formats



## Tech Stack

* Python
* OpenCV
* OCR
* LLaMA (Groq API)
* JSON Processing



## Workflow

1. Input image/document collection
2. Image preprocessing and enhancement
3. Contour detection & region extraction
4. OCR text extraction
5. LLM-based structured data generation
6. JSON post-processing and validation



## Image Processing Techniques

* Grayscale conversion
* Thresholding
* Noise removal
* Contour detection
* Circular region extraction
* ROI (Region of Interest) isolation



## LLM Integration

Implemented prompt engineering strategies to:

* Improve response consistency
* Enforce structured JSON formatting
* Handle noisy OCR outputs
* Extract relevant semantic information



## Output Example

```json
{
  "label": {
    "brand": "His Master's Voice",
    "record_number": "N 54607",
    "film": "Majboor",
    "language": "Hindustani",
    "recording_published": "1964",
    "song_title": "Tumhein Jo Bhi Dekh Lega",
    "singer": "Hemant Kumar",
    "production": "De Lux Films",
    "music_director": "Kalyanji Anandji",
    "lyricist": "Indiwar",
    "catalog_number": "OJE 21906",
    "manufacturer": "The Gramophone Co. Ltd.",
    "copyright_notice": "This copyright record must not be publicly performed without licence.",
    "additional_text": "Incorporated in England with limited liability"
  }
}




## Key Contributions

* Built preprocessing and post-processing pipelines for noisy image handling
* Developed structured data extraction workflows
* Improved OCR-to-JSON conversion accuracy using prompt engineering
* Automated extraction of machine-readable document data



## Future Improvements

* Multi-language OCR support
* Fine-tuned document-specific LLM prompts
* Layout-aware document parsing
* Real-time API deployment



## Use Cases

* Historical document digitization
* Invoice and receipt processing
* Form data extraction
* Archival record management
* Intelligent document automation
