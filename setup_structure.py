import os

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models",
    "reports"
]

files = [
    "src/data_preprocessing.py",
    "src/feature_engineering.py",
    "src/train.py",
    "src/evaluate.py",
    "src/utils.py",
    "README.md",
    "requirements.txt",
    ".gitignore"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Professional ML project structure created successfully!")
