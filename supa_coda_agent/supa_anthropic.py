import anthropic
import base64
import magic

anthropic_client = anthropic.Anthropic()

def send_message_with_image(local_path: str, message: str):
    mime_type = magic.Magic(mime=True).from_file(local_path)
    with open(local_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")
        return anthropic_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2048,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": mime_type,
                                "data": image_data
                            }
                        },
                        {
                            "type": "text",
                            "text": "What is in the image?"
                        }
                    ]
                }
            ]
        )