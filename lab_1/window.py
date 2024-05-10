from functions import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.key_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.json")
        self.text_path = QFileDialog.getOpenFileName(self, 'Выберите файл с текстом', filter = "*.txt")

        self.setWindowTitle('Приложение')
        self.setGeometry(800, 800, 800, 600)

        self.select_new_key_button = QPushButton('Выбрать новый ключ', self)
        self.select_new_key_button.clicked.connect(self.select_key)
        
        self.select_new_text_button = QPushButton('Выбрать новый текст', self)
        self.select_new_text_button.clicked.connect(self.select_text)
        
        self.descryption_button = QPushButton('Дешифровать', self)
        self.descryption_button.clicked.connect(self.descryption_text)

        self.encryption_button = QPushButton('Зашифровать', self)
        self.encryption_button.clicked.connect(self.encryption_text)
        
        self.label1 = QLabel('Исходный текст', self)
        self.label2 = QLabel('Преобразованный текст', self)

        self.text_edit1 = QTextEdit(read_text(self.text_path[0]), self)
        self.text_edit2 = QTextEdit("", self)

        self.swap_button = QPushButton('Преобразованный -> Исходный', self)
        self.swap_button.clicked.connect(self.swap_texts)

        self.save_button = QPushButton('Сохранить преобразованный текст', self)
        self.save_button.clicked.connect(self.save_file)

        self.analysis1_button = QPushButton('Сохранить частоту символов исходного текста', self)
        self.analysis1_button.clicked.connect(self.frequency_analysis1)

        self.analysis2_button = QPushButton('Сохранить частоту символов преобразованного текста', self)
        self.analysis2_button.clicked.connect(self.frequency_analysis2)
        
        vbox = QGridLayout()
        
        vbox.addWidget(self.select_new_key_button, 0, 0)
        vbox.addWidget(self.select_new_text_button, 0, 1)
        vbox.addWidget(self.text_edit1, 1, 0)
        vbox.addWidget(self.text_edit2, 1, 1)
        vbox.addWidget(self.label1, 2, 0)
        vbox.addWidget(self.label2, 2, 1)
        vbox.addWidget(self.descryption_button, 3, 0)
        vbox.addWidget(self.encryption_button, 3, 1)
        vbox.addWidget(self.swap_button, 4, 0)
        vbox.addWidget(self.save_button, 4, 1)
        vbox.addWidget(self.analysis1_button, 5, 0)
        vbox.addWidget(self.analysis2_button, 5, 1)
        self.setLayout(vbox)

    def descryption_text(self):
        self.text_edit2.setText(descryption(self.text_edit1.toPlainText(), read_key(self.key_path[0])))

    def encryption_text(self):
        self.text_edit2.setText(encryption(self.text_edit1.toPlainText(), read_key(self.key_path[0])))

    def select_text(self):
        self.text_path = QFileDialog.getOpenFileName(self, 'Выберите файл с текстом', filter = "*.txt")
        self.text_edit1.setText(read_text(self.text_path[0]))

    def select_key(self):
        self.key_path = QFileDialog.getOpenFileName(self, 'Выберите файл с ключом', filter = "*.json")

    def swap_texts(self):
        self.text_edit1.setText(self.text_edit2.toPlainText())
        self.text_edit2.setText("")

    def save_file(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить преобразованный текст')
        with open(Path(fname[0]), 'w', encoding = "utf-8") as file:
            file.write(self.text_edit2.toPlainText())

    def frequency_analysis1(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить частоту символов исходного текста')
        save_frequency_analysis(fname[0], self.text_edit2.toPlainText())

    def frequency_analysis2(self):
        fname = QFileDialog.getSaveFileName(self, 'Сохранить частоту символов преобразованного текста')
        save_frequency_analysis(fname[0], self.text_edit2.toPlainText())

    
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())