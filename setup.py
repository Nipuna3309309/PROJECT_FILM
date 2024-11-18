from setuptools import setup, find_packages

# Read the content of the README.md file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define necessary variables
AUTHOR_NAME = 'NIPUNA ABEYSEKARA'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

# Set up the project
setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='nipuna3309309@gmail.com',
    description='A simple Streamlit app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds all packages
    python_requires='>=3.7',
    url=f'https://github.com/nipuna3309309/{SRC_REPO}',
    install_requires=LIST_OF_REQUIREMENTS,
)
