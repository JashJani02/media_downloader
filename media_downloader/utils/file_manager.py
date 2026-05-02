import os
import uuid

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def generate_filename(ext: str = "jpg") -> str:
    return f"{uuid.uuid4()}.{ext}"


def save_file(data: bytes, directory: str, ext: str = "jpg") -> str:
    ensure_dir(directory)

    filename = generate_filename(ext)
    path = os.path.join(directory, filename)

    with open(path, "wb") as f:
        f.write(data)

    return path