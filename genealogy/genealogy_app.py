from PyQt6.QtWidgets import QMainWindow, QMessageBox
from genealogy.ui_components import create_menu, create_main_layout, create_status_bar
from genealogy.config_handler import load_credentials, save_credentials
from genealogy.event_handlers import connect_to_opensearch, show_index_content

class GenealogyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genealogy OpenSearch Interface")
        self.setGeometry(100, 100, 800, 600)
        self.client = None

        self.host = None
        self.port = None
        self.user = None
        self.password = None

        create_main_layout(self)
        load_credentials(self)
        create_menu(self)
        create_status_bar(self)

    def connect_to_opensearch(self):
        try:
            connect_to_opensearch(self)
            self.bulk_load_action.setEnabled(True)
            self.refresh_indices()
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", f"Failed to connect to OpenSearch. Please, check your connection details.\n{str(e)}")

    def refresh_indices(self):
        try:
            indices = self.client.get_indices()
            self.indices_list.clear()
            self.indices_list.addItems(indices)
            self.status_bar.showMessage(f"Loaded {len(indices)} indices", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to refresh indices: {str(e)}")

    def show_index_content(self, item):
        try:
            index_name = item.text()
            content = self.client.get_index_content(index_name)
            show_index_content(self, content)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load index content: {str(e)}")

    def save_credentials(self):
        save_credentials(self)
