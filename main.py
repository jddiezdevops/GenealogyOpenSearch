from PyQt6.QtWidgets import QApplication
from genealogy.genealogy_app import GenealogyApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GenealogyApp()
    window.show()
    sys.exit(app.exec())