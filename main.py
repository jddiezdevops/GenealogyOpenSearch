import sys
from PyQt6.QtWidgets import QApplication
from genealogy_app import GenealogyApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GenealogyApp()
    window.show()
    sys.exit(app.exec())
