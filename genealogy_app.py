from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QHBoxLayout,
    QLineEdit, QLabel, QPushButton, QMessageBox, QListWidget, QInputDialog, QGroupBox, QStatusBar, QScrollArea, QDialog, QFileDialog
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
from opensearch_client import OpenSearchClient
from dialogs import display_index_content
from index_management import create_index, delete_index
from bulk_load import cargar_datos_bulk
from file_conversion import convertir_a_json

class GenealogyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genealogy OpenSearch Interface")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))  # Agrega un ícono a la ventana
        self.client = None

        self.host = None
        self.port = None
        self.user = None
        self.password = None

        self.create_menu()
        self.create_main_layout()
        self.create_status_bar()
        self.setCentralWidget(self.central_widget)

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        connect_action = QAction("Connect", self)
        connect_action.triggered.connect(self.connect_to_opensearch)
        file_menu.addAction(connect_action)

        export_json_action = QAction("Export to JSON", self)
        export_json_action.triggered.connect(lambda: convertir_a_json(self))
        file_menu.addAction(export_json_action)

        bulk_load_action = QAction("Load Bulk JSON", self)
        bulk_load_action.triggered.connect(lambda: cargar_datos_bulk(self))
        bulk_load_action.setEnabled(False)  # Deshabilitar inicialmente
        file_menu.addAction(bulk_load_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.bulk_load_action = bulk_load_action  # Guardar referencia para habilitar/deshabilitar más tarde

    def create_main_layout(self):
        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Connection Group
        connection_group = QGroupBox("Connection Settings")
        connection_layout = QHBoxLayout()

        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Host (e.g., localhost)")
        self.port_input = QLineEdit(self)
        self.port_input.setPlaceholderText("Port (e.g., 9200)")

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("User (optional)")
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password (optional)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.connect_button = QPushButton("Connect", self)
        self.connect_button.clicked.connect(self.connect_to_opensearch)

        connection_layout.addWidget(QLabel("Host:"))
        connection_layout.addWidget(self.host_input)
        connection_layout.addWidget(QLabel("Port:"))
        connection_layout.addWidget(self.port_input)
        connection_layout.addWidget(QLabel("User:"))
        connection_layout.addWidget(self.user_input)
        connection_layout.addWidget(QLabel("Password:"))
        connection_layout.addWidget(self.password_input)
        connection_layout.addWidget(self.connect_button)

        connection_group.setLayout(connection_layout)
        self.layout.addWidget(connection_group)

        # Index Group
        index_group = QGroupBox("Index Management")
        index_layout = QVBoxLayout()

        self.indices_list = QListWidget(self)
        self.indices_list.itemDoubleClicked.connect(self.show_index_content)
        self.refresh_button = QPushButton("Refresh Indices", self)
        self.refresh_button.clicked.connect(self.refresh_indices)
        self.create_index_button = QPushButton("Create Index", self)
        self.create_index_button.clicked.connect(lambda: create_index(self))
        self.delete_index_button = QPushButton("Delete Index", self)
        self.delete_index_button.clicked.connect(lambda: delete_index(self))

        index_layout.addWidget(self.indices_list)
        index_layout.addWidget(self.refresh_button)
        index_layout.addWidget(self.create_index_button)
        index_layout.addWidget(self.delete_index_button)

        index_group.setLayout(index_layout)
        self.layout.addWidget(index_group)

    def create_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

    def connect_to_opensearch(self):
        self.host = self.host_input.text()
        self.port = self.port_input.text()
        self.user = self.user_input.text()
        self.password = self.password_input.text()

        try:
            self.client = OpenSearchClient(self.host, self.port, self.user, self.password)
            QMessageBox.information(self, "Connection", "Connected to OpenSearch successfully")
            self.status_bar.showMessage("Connected to OpenSearch", 5000)
            self.refresh_indices()
            self.bulk_load_action.setEnabled(True)  # Habilitar la opción de carga en bulk después de conectarse
        except ConnectionError as e:
            QMessageBox.critical(self, "Connection Error", str(e))
            self.status_bar.showMessage("Connection Error", 5000)

    def refresh_indices(self):
        if not self.client:
            QMessageBox.warning(self, "Warning", "Not connected to OpenSearch")
            return

        self.indices_list.clear()
        try:
            indices = self.client.get_indices()
            self.indices_list.addItems(indices)
            self.status_bar.showMessage("Indices refreshed", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.status_bar.showMessage("Error refreshing indices", 5000)

    def show_index_content(self, item):
        index_name = item.text()
        try:
            content = self.client.get_index_content(index_name)
            display_index_content(self, index_name, content)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.status_bar.showMessage("Error showing index content", 5000)
