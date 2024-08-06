from PyQt6.QtWidgets import QMainWindow
from ui_components import create_menu, create_main_layout, create_status_bar
from event_handlers import connect_to_opensearch, refresh_indices, show_index_content
from config_handler import load_credentials, save_credentials

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
        connect_to_opensearch(self)

    def refresh_indices(self):
        refresh_indices(self)

    def show_index_content(self, item):
        show_index_content(self, item)

    def save_credentials(self):
        save_credentials(self)
