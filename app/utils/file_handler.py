import os
import shutil
from datetime import datetime

TEMP_DIR = "data/temp"

os.makedirs(TEMP_DIR, exist_ok=True)

def save_uploaded_file(uploaded_file):
    """
    Saves uploaded file to temp directory
    and returns saved file path.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{timestamp}_{os.path.basename(uploaded_file.name)}"

    save_path = os.path.join(TEMP_DIR, filename)

    shutil.copy(uploaded_file.name, save_path)

    return save_path
