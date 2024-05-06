import json 
from pathlib import Path
import sys

from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QGridLayout, QLabel, QTextEdit


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
            try:
                src += key[symbol]
            except:
                src += symbol
    except:
        return "Oh no!"
    return src

def encryption(text: str, key: dict[str, str]) -> str:
    """Encrypts text by key"""
    src = ""
    if text == None or key == None:
        return "Отсутствует текст либо ключ шифрования!"
    text = text.upper()
    key = list(key.keys())
    value = list(key.values())
    try: 
        for symbol in text:
            try:
                src += key[value.index(symbol)]
            except:
                src += symbol
    except: 
        return "Oh no!"
    return src

def save_frequency_analysis(file_path: str, text: str) -> None:
    """Saves the character frequency in a json file"""
    file_path = Path(file_path)
    dic = dict()
    
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for k in dic.keys():
        dic[k] = dic[k] / len(text)

    with open(file_path, 'w', encoding = "utf-8") as file:
        json.dump(dic, file)
