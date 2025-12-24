from setuptools import setup, find_packages

setup(
    name="speakerlab",          # Your package name
    version="0.1",
    packages=find_packages(),   # Automatically find packages in repo
    install_requires=[
        "torch>=1.10.1",
        "torchaudio>=0.10.1",
        "tqdm>=4.42.0",
        "scipy>=1.7.0",
        "numpy>=1.20.0,<1.24",
        "scikit-learn==1.0.2",
        "soundfile",
        "kaldiio",
        "pyyaml",
        "matplotlib",
        "pandas",
        "openpyxl",
    ],
    python_requires="==3.8",
)
