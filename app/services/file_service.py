import pandas as pd
import uuid
import os

UPLOAD_DIR = "storage/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def save_file(file):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}.csv"

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    df = pd.read_csv(file_path)

    return file_id, df


def load_dataframe(file_id: str):
    file_path = f"{UPLOAD_DIR}/{file_id}.csv"
    return pd.read_csv(file_path)