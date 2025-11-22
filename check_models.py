# backend/check_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in environment variables.")
else:
    genai.configure(api_key=api_key)
    print(f"Checking models for API Key: {api_key[:5]}...{api_key[-4:]}\n")
    
    try:
        print("Available Models:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
    except Exception as e:
        print(f"❌ Error listing models: {e}")