from setuptools import setup, find_packages
setup(
    name="videocapture",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy', 'pillow', 'scipy']
)

# FIXME: Compile decklink-capture script automatically
