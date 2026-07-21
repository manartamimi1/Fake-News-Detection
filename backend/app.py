from flask_cors import CORS  # Allow frontend to connect
from flask import Flask, request, jsonify
from transformers import pipeline
from huggingface_hub import login
import pytesseract
from PIL import Image
import os
login(os.getenv('HUGGINGFACE_TOKEN'))
from dotenv import load_dotenv
load_dotenv()
# Login to Hugging Face
# Load pipeline with your hosted model
pipe = pipeline("text-classification", model="ManarTami/Bert")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Text detection route
@app.route('/detect', methods=['POST'])
def detect():

    
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # Run the model prediction
        result = pipe(text)[0]

        # Map model labels
        label_map = {
            "LABEL_0": "Fake",
            "LABEL_1": "Real"
        }

        readable_label = label_map.get(result['label'], "Unknown")
        confidence = round(result['score'] * 100, 2)

        return jsonify({
            "prediction": readable_label,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Image-based text extraction and prediction route
@app.route('/predict_from_image', methods=['POST'])
def predict_from_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    try:
        image_file = request.files['image']
        image = Image.open(image_file.stream)

        # Extract text from image using Tesseract OCR
        extracted_text = pytesseract.image_to_string(image).strip()

        if not extracted_text:
            return jsonify({'error': 'No text found in image'}), 400

        # Run the extracted text through your model for prediction
        result = pipe(extracted_text)[0]

        # Map model labels
        label_map = {
            "LABEL_0": "Fake",
            "LABEL_1": "Real"
        }

        readable_label = label_map.get(result['label'], "Unknown")
        confidence = round(result['score'] * 100, 2)
         

        return jsonify({
            'prediction': readable_label,
            'confidence': confidence,
            'extracted_text': extracted_text  # Ensure this is returned
        })
      
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)