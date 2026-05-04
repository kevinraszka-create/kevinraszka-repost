
from py_compile import main
import sys
from PySide6 import QtWidgets, QtCore

class ColorSwatch(QtWidgets.QPushButton):
    def __init__(self, color_hex, parent=None):
        super().__init__(parent)
        self.color_hex = color_hex
        self.setFixedSize(24, 24) # Nastavení velikosti tlačítka
        self.setStyleSheet(f"background-color: {self.color_hex}; border: none;") # Nastavení barvy tlačítka
        self.clicked.connect(self.on_click)

    def on_click(self):
        print(f"Kliknuto na barvu: {self.color_hex}")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Klikací hra")
        self.resize(500, 400) # Nastavení velikosti okna

        central_widget = QtWidgets.QWidget() # Vytvoření centrálního widgetu
        self.setCentralWidget(central_widget)

        main_layout = QtWidgets.QVBoxLayout(central_widget) # Vytvoření vertikálního layoutu pro centrální widget
        label = QtWidgets.QLabel("Skóre: 0")
        label.setAlignment(QtCore.Qt.AlignCenter)

        main_layout.addWidget(label) # Přidání labelu do layoutu

        

        red_Swatch = QtWidgets.QPushButton("#FF0000") # Tlačítko pro červenou barvu
        main_layout.addWidget(red_Swatch, alignment=QtCore.Qt.AlignLeft)



if __name__ == "__main__": # Spuštění aplikace
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())