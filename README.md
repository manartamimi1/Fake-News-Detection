# Fake News Detection - TruthLens

A machine learning-powered web application that detects fake news using BERT (Bidirectional Encoder Representations from Transformers) and Optical Character Recognition (OCR). The application allows users to analyze text directly or extract text from images for fake news classification.

## Features

✨ **Text Analysis** - Enter any news headline or text to detect if it's fake or real  
📸 **Image OCR** - Upload images containing text and get fake news predictions  
🎯 **High Accuracy** - Uses pre-trained BERT model for reliable classification  
⚡ **Real-time Results** - Get instant predictions with confidence scores  
🎨 **User-Friendly Interface** - Clean and intuitive web interface  

## Project Structure

```
OCR/
├── backend/
│   ├── app.py              # Flask API server with ML model
│   └── .env               # Environment variables (API tokens)
├── frontend/
│   ├── index.html         # Main web interface
│   ├── style.css          # Styling
│   └── images/            # Asset images
├── .venv/                 # Python virtual environment
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Tesseract OCR (for image text extraction)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/manartamimi1/Fake-News-Detection.git
cd Fake-News-Detection
```

### 2. Create Virtual Environment
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
pip install flask flask-cors transformers huggingface-hub pytesseract pillow torch python-dotenv
```

**For CPU-only (recommended for most users):**
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### 4. Install Tesseract OCR
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

Follow the installer instructions and remember the installation path (usually `C:\Program Files\Tesseract-OCR`).

### 5. Configure Environment Variables
Create a `.env` file in the `backend/` folder:
```
HUGGINGFACE_TOKEN=your_huggingface_token_here
```

Get your token from: https://huggingface.co/settings/tokens

## Running the Application

### Terminal 1: Start Backend Server
```powershell
cd backend
python app.py
```
The backend will run on `http://localhost:5000`

### Terminal 2: Start Frontend Server
```powershell
cd frontend
python -m http.server 8000
```
The frontend will run on `http://localhost:8000`

### Open in Browser
Navigate to: **http://localhost:8000**

## Usage

### Text Analysis
1. Enter a news headline or text in the input field
2. Click "Detect" button
3. View the prediction (Fake/Real) with confidence percentage

### Image Analysis
1. Click "Upload Image" or drag an image file
2. The app extracts text from the image using OCR
3. The extracted text is analyzed for fake news
4. View results with the extracted text displayed

## API Endpoints

### `/detect` (POST)
Detect fake news from text input

**Request:**
```json
{
  "text": "Your news text here"
}
```

**Response:**
```json
{
  "prediction": "Real",
  "confidence": 95.23
}
```

### `/predict_from_image` (POST)
Detect fake news from uploaded image

**Request:** Multipart form with image file

**Response:**
```json
{
  "prediction": "Fake",
  "confidence": 78.45,
  "extracted_text": "The extracted text from image"
}
```

## Model Information

- **Model Name:** ManarTami/Bert
- **Type:** Text Classification
- **Task:** Fake News Detection
- **Labels:** Real, Fake
- **Framework:** PyTorch with Hugging Face Transformers

## Technologies Used

- **Backend:** Flask, Python
- **Frontend:** HTML5, CSS3, JavaScript
- **ML Framework:** PyTorch, Hugging Face Transformers
- **OCR:** Tesseract, pytesseract
- **API:** REST API with CORS support

## Troubleshooting

### Backend won't start
- Ensure virtual environment is activated (`(.venv)` should show in prompt)
- Check all dependencies are installed: `pip list`
- Verify Tesseract is installed and path is correct in `app.py`

### Model downloading takes too long
- First run downloads the BERT model (~500MB)
- This is normal and happens only once
- Make sure you have stable internet connection

### Image OCR not working
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Update the path in `backend/app.py` if installed in different location
- Try with simple, clear images first

### CORS errors
- Ensure backend is running on port 5000
- Check that `CORS(app)` is enabled in `app.py`

## Security Notes

- **Never** commit your Hugging Face token to GitHub
- Always use `.env` file for sensitive information
- The `.env` file is in `.gitignore` for security

## Future Improvements

- [ ] Add model confidence threshold settings
- [ ] Support for multiple languages
- [ ] Batch processing for multiple articles
- [ ] Database to store analysis history
- [ ] Docker containerization
- [ ] Deploy to cloud (Azure, AWS, Heroku)

## License

This project is open source and available under the MIT License.

## Author

Created by Manar Tamimi

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Happy Fact-Checking! 🔍**
