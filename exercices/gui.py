import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window Title")
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        self.setWindowIcon(QIcon("bro_code.jpg"))
        
        self.hello = QLabel("Hello", self)
        self.image = QLabel(self)
        self.pixmap = QPixmap("bro_code.jpg")
        self.button = QPushButton("Click me!", self)
        self.text = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.hello.setFont(QFont("Verdana", 20))
        self.hello.setGeometry(0, 0, 500, 100)
        self.hello.setStyleSheet("color: #fff;"
                            "background-color: #003366;")
        self.hello.setAlignment(Qt.AlignCenter)

        self.image.setGeometry(10, 10, 80, 80)
        self.image.setStyleSheet("border: 2px solid #fff;")
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)

        self.button.setFont(QFont("Verdana", 12))
        self.button.setGeometry(50, 150, 100, 50)
        self.button.clicked.connect(self.on_click)

        self.text.setGeometry(80, 190, 80, 80)
        self.text.setFont(QFont("Verdana", 12))

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)
        self.text.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()