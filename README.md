# Image Analysis Chatbot

An interactive Streamlit application that combines OCR (Optical Character Recognition) with LLM capabilities to analyze images and engage in conversations about their content.

##Output
![Alt Text](Image-analysis-chatbot/Output.gif)

## Features

- Image upload and processing
- Text extraction from images using Tesseract OCR
- Table detection and extraction
- Interactive chat interface
- Integration with Groq's LLM API (llama-3.3-70b-versatile)
- Chat history tracking
- PDF processing capabilities
- Database storage for content

## Prerequisites

- Python 3.8+
- Tesseract OCR installed on your system
- Groq API key

### Installing Tesseract OCR

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### macOS
```bash
brew install tesseract
```

#### Windows
1. Download the installer from [GitHub Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer
3. Add Tesseract to your system PATH

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd OCR
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your Groq API key:
   - The API key is already configured in `llm_client.py`
   - Model: llama-3.3-70b-versatile

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Use the interface to:
   - Upload images
   - View extracted content
   - Chat with the AI about the image content
   - Review chat history

## Project Structure

```
timepass/
├── app.py                 # Main Streamlit application
├── image_processor.py     # Image processing and OCR
├── llm_client.py         # LLM API integration
└── requirements.txt      # Project dependencies
```

## Components

- **Image Processor**: Handles image processing and OCR using Tesseract
- **LLM Client**: Manages communication with Groq's API

## Error Handling

The application includes comprehensive error handling for:
- Image processing failures
- API communication issues
- File upload problems

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 🧠 Author

**Varshini Vaddepalli**    
📍 Hyderabad, India

---
