
from setuptools import setup, find_packages

# A clean, standard setup script.
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

