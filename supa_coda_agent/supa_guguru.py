import os
from google import genai

google_client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def send_message_with_image(local_path: str, message: str):
    myfile = google_client.files.upload(file=local_path)
    
    return google_client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[myfile, message]
    )