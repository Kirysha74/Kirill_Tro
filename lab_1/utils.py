import json 
from pathlib import Path


def read_key(file_path: str) -> dict:
    try:
        key = Path(file_path)
        with open(key, "r", encoding = "utf-8") as file:
            data = json.load(file)
            return data
    except:
        return None

def read_text(file_path: str) -> str:
    try:
        text = Path(file_path)
        with open(text, "r", encoding = "utf-8") as file:
            src = file.read()
            return src
    except: 
        return None

def descryption(a: str, slovar: dict) -> str:
    if a == None or slovar == None:
        print("Отсутствует текст либо ключ дешифрования!")
        return None
    try: 
        for k, v in slovar.items():
            a = a.replace(k, v)
    except: 
        return None
    return a
