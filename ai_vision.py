import google.generativeai as genai
import os
import json
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_warehouse_image(image_file):
    model = genai.GenerativeModel('gemini-flash-latest')
    
    img = Image.open(image_file)
    
    prompt = """
    Analyze this warehouse image. Return ONLY raw JSON.
    Extract:
    1. "sku_name": Text on label/box
    2. "quantity": Count visible items
    3. "expiry": Expiry date if visible (YYYY-MM-DD) or null
    4. "damage": boolean (is it damaged?)
    5. "damage_score": 0.0 to 1.0
    6. "explanation": Short summary of what you see.
    """
    
    response = model.generate_content([prompt, img])
    try:
        # Strip markdown if Gemini adds it
        clean_text = response.text.replace('```json', '').replace('```', '')
        return json.loads(clean_text)
    except:
        return {"error": "Failed to parse AI response", "raw": response.text}