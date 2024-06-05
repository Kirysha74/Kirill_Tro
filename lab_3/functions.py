import json
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def read_json(file_path: str) -> dict | None:
    """Reads the json file"""
    try:
        file_path = Path(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None


def read_bin_text(file_path: str) -> dict | None:
    """Reads the text file in binary format"""
    try:
        file_path = Path(file_path)
        with open(file_path, "rb") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None


def read_text(file_path: str) -> dict | None:
    """Reads the text file"""
    try:
        file_path = Path(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return None


def write_json(file_path: str, dic: dict) -> bool:
    """Writes the json file"""
    try:
        file_path = Path(file_path)
        with open(file_path, "w", encoding="utf-8") as file:
            data = json.dump(dic)
            return True
    except:
        return False


def write_bin_text(file_path: str, text: str) -> bool:
    """Writes the binary file"""
    try:
        file_path = Path(file_path)
        with open(file_path, "wb") as file:
            file.write(text)
            return True
    except:
        return False


def write_text(file_path: str, text: str) -> bool:
    """Writes the text file"""
    try:
        file_path = Path(file_path)
        with open(file_path, "w") as file:
            file.write(text)
            return True
    except:
        return False


def write_public_key(file_path: str, public_key: rsa.RSAPublicKey) -> bool:
    """Writes the public key in binary file"""
    with open(file_path, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))


def write_private_key(file_path: str, private_key: rsa.RSAPrivateKey) -> bool:
    """Writes the private key in binary file"""
    with open(file_path, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))


def read_public_key(file_path: str) -> rsa.RSAPublicKey | None:
    """Reads the public key in binary file"""
    try:
        with open(file_path, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
        print(d_public_key)
        return d_public_key
    except FileNotFoundError:
        return None


def read_private_key(file_path: str) -> rsa.RSAPrivateKey | None:
    """Reads the public key in binary file"""
    try:
        with open(file_path, 'rb') as pem_in:
            private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key
    except FileNotFoundError:
        return None