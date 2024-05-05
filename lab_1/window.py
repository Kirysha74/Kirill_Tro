from utils import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.key_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.json")
        self.text_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.txt")

        self.setWindowTitle('Приложение')
        self.setGeometry(800, 800, 800, 600)

        self.select_new_key = QPushButton('Выбрать новый ключ', self)
        self.select_new_key.clicked.connect(self.select_key)
        
        self.select_new_text = QPushButton('Выбрать новый текст', self)
        self.select_new_text.clicked.connect(self.select_text)
        
        self.btn_save_dataset = QPushButton('Дешифровать', self)
        self.btn_save_dataset.clicked.connect(self.descryption_text)

        self.btn_split_by_weeks = QPushButton('Зашифровать', self)
        self.btn_split_by_weeks.clicked.connect(self.encryption_text)
        
        self.label1 = QLabel('Исходный текст', self)
        self.label2 = QLabel('Преобразованный текст', self)

        self.textEdit1 = QTextEdit(read_text(self.text_path[0]), self)
        self.textEdit2 = QTextEdit("", self)
        
        vbox = QGridLayout()
        
        vbox.addWidget(self.select_new_key, 0, 0)
        vbox.addWidget(self.select_new_text, 0, 1)
        vbox.addWidget(self.textEdit1, 1, 0)
        vbox.addWidget(self.textEdit2, 1, 1)
        vbox.addWidget(self.label1, 2, 0)
        vbox.addWidget(self.label2, 2, 1)
        vbox.addWidget(self.btn_save_dataset, 3, 0)
        vbox.addWidget(self.btn_split_by_weeks, 3, 1)
        self.setLayout(vbox)

    def descryption_text(self):
        self.textEdit2.setText(descryption(self.textEdit1.toPlainText(), read_key(self.key_path[0])))

    def encryption_text(self):
        self.textEdit2.setText(encryption(self.textEdit1.toPlainText(), read_key(self.key_path[0])))

    def select_text(self):
        self.text_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.txt")
        self.textEdit1.setText(read_text(self.text_path[0]))

    def select_key(self):
        self.key_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.json")

    


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())