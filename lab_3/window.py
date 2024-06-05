import sys

from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QPushButton, QGridLayout, QLabel, QTextEdit, QInputDialog

from algorithms import Symmetric, Assymetric
from functions import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Приложение')
        self.setGeometry(800, 800, 800, 600)

        self.generate_keys = QPushButton('Сгенерировать ключи', self)
        self.generate_keys.clicked.connect(self.gen_keys)
        
        self.encryption_text = QPushButton('Зашифровать текст', self)
        self.encryption_text.clicked.connect(self.encrypt_text)
        
        self.decryption_text = QPushButton('Дешифровать текст', self)
        self.decryption_text.clicked.connect(self.decrypt_text)
        
        vbox = QGridLayout()
        
        vbox.addWidget(self.generate_keys)
        vbox.addWidget(self.encryption_text)
        vbox.addWidget(self.decryption_text)
        self.setLayout(vbox)

    def get_key_length(self) -> int:
        """This method determines the key size"""
        key_lenght, okPressed = QInputDialog.getItem(self, "Выбор размера ключа","Размер:", ("64", "128", "192"), 0, False)

        if not okPressed or not key_lenght:
            key_lenght = 8
        return int(key_lenght) // 8

    def gen_keys(self) -> None:
        """This method generate key"""
        symmetric = Symmetric.generate_key(self.get_key_length())
        private, public = Assymetric.generate_keys()
        enc_symmetric = Assymetric.encrypt_key(symmetric, public)
        write_bin_text(QFileDialog.getSaveFileName(self, 'Сохранить зашифрованный симметричный ключ')[0], enc_symmetric)
        write_public_key(QFileDialog.getSaveFileName(self, 'Сохранить открытый ключ')[0], public)
        write_private_key(QFileDialog.getSaveFileName(self, 'Сохранить закрытый ключ')[0], private)
        print("Key generation and saving completed successfully")

    def encrypt_text(self) -> None:
        """This method encrypts the text"""
        text = read_text(QFileDialog.getOpenFileName(self, 'Выберите файл с текстом', filter = "*.txt")[0])
        private = read_private_key(QFileDialog.getOpenFileName(self, 'Прочитать закрытый ключ', filter = "*.pem")[0])
        print(private)
        enc_symmetric = read_bin_text(QFileDialog.getOpenFileName(self, 'Прочитать зашифрованный симметричный ключ', filter = "*.bin")[0])
        dec_symmetric = Assymetric.decrypt_key(enc_symmetric, private)
        encrypted_text = Symmetric.encrypt_text(text, dec_symmetric)
        write_bin_text(QFileDialog.getSaveFileName(self, 'Сохранить зашифрованный текст')[0], encrypted_text)
        print('The encryption and saving of the text were completed successfully')

    def decrypt_text(self) -> None:
        """This method decrypts the text"""
        encrypted_text = read_bin_text(QFileDialog.getOpenFileName(self, 'Выберите файл с зашифрованным текстом', filter = "*.bin")[0])
        private = read_private_key(QFileDialog.getOpenFileName(self, 'Прочитать закрытый ключ', filter = "*.pem")[0])
        enc_symmetric = read_bin_text(QFileDialog.getOpenFileName(self, 'Прочитать зашифрованный симметричный ключ', filter = "*.bin")[0])
        dec_symmetric = Assymetric.decrypt_key(enc_symmetric, private)
        decrypted_text = Symmetric.decrypt_text(
            encrypted_text, dec_symmetric)
        write_text(QFileDialog.getSaveFileName(self, 'Сохранить расшифрованный текст')[0], decrypted_text)
        print('Decryption and saving were completed successfully')

    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())