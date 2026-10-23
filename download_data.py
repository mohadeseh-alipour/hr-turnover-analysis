# ============================================================
# Download IBM HR Analytics Dataset
# Source: GitHub (public CSV mirror of Kaggle dataset)
# ============================================================

import urllib.request
import os

URL = (
    "https://raw.githubusercontent.com/dsrscientist/"
    "dataset1/master/WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

OUTPUT_PATH = "data/hr_data.csv"
os.makedirs("data", exist_ok=True)

print("⬇️  Downloading IBM HR Analytics dataset...")
urllib.request.urlretrieve(URL, OUTPUT_PATH)
print(f"✅ Dataset saved to {OUTPUT_PATH}")
