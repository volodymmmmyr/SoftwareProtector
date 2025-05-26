import hashlib

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_integrity(file_path, expected_hash):
    return calculate_hash(file_path) == expected_hash