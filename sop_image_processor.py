import pytesseract
from PIL import Image
import pandas as pd
import cv2
import numpy as np
import io

class ImageProcessor:
    def __init__(self):
        self.image_text = ""
        self.tables = []

    def extract_text_and_tables(self, image_file):
        # Convert uploaded file to image
        image_bytes = io.BytesIO(image_file.read())
        image = Image.open(image_bytes)
        
        # Convert to OpenCV format
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Extract text using Tesseract
        self.image_text = pytesseract.image_to_string(image)
        
        # Extract tables using image_to_data
        tables_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DATAFRAME)
        
        # Process and clean tables
        self.tables = self._process_tables(tables_data)
        
        return {
            'text': self.image_text,
            'tables': self.tables
        }

    def _process_tables(self, df):
        # Filter rows with text
        df = df[df['conf'] != -1]
        df = df.fillna('')
        
        # Group by block number to separate different tables
        tables = []
        for block_num, block_data in df.groupby('block_num'):
            if len(block_data) > 1:  # Only consider blocks with multiple entries
                table = pd.DataFrame({
                    'text': block_data['text'].values,
                    'left': block_data['left'].values,
                    'top': block_data['top'].values
                })
                tables.append(table)
        
        return tables

    def get_formatted_content(self):
        content = f"Extracted Text:\n{self.image_text}\n\n"
        
        if self.tables:
            content += "Tables Found:\n"
            for i, table in enumerate(self.tables, 1):
                content += f"\nTable {i}:\n{table.to_string()}\n"
        
        return content