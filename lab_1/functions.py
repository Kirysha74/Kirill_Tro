import json 
from pathlib import Path


def read_key(file_path: str) -> dict[str, str]:
    """Reads the file with the decryption key"""

    try:
        file_path = Path(file_path)
        with open(file_path, "r", encoding = "utf-8") as file:
            data = json.load(file)
            return data
    except:
        return None
        

def read_text(file_path: str) -> str:
    """Reads the text from the file"""

    try:
        file_path = Path(file_path)
        with open(file_path, "r", encoding = "utf-8") as file:
            src = file.read()
            return src
    except:
        return None


def descryption(text: str, key: dict[str, str]) -> str:
    """Decrypts text by key"""

    src = ""
    if text == None or key == None:
        return "Отсутствует текст либо ключ шифрования!"
    try:
        for symbol in text:
            if symbol in key.keys():
                src += key[symbol]
            else:
                src += symbol
    except:
        return "При попытке расшифровать текст произошла ошибка!"
    return src


def encryption(text: str, key: dict[str, str]) -> str:
    """Encrypts text by key"""

    src = ""
    if text == None or key == None:
        return "Отсутствует текст либо ключ шифрования!"
    text = text.upper()
    keys = list(key.keys())
    values = list(key.values())
    try: 
        for symbol in text:
            if symbol in values:
                src += keys[values.index(symbol)]
            else:
                src += symbol
    except: 
        return "При попытке зашифровать текст возникла ошибка!"
    return src


def freq_analysis(text: str) -> dict:
    """Do frequency analysis"""

    dic = dict()
    
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k in dic.keys():
        dic[k] = dic[k] / len(text)

    return dic


def save_frequency_analysis(file_path: str, text: str) -> None:
    """Saves the character frequency in a json file"""

    file_path = Path(file_path)

    with open(file_path, 'w', encoding = "utf-8") as file:
        json.dump(freq_analysis(text), file)
