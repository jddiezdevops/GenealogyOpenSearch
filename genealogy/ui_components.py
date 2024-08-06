from PyQt6.QtWidgets import (
    QVBoxLayout, QWidget, QHBoxLayout, QLineEdit, QLabel, QPushButton, 
    QListWidget, QGroupBox, QStatusBar, QMenuBar
)
from PyQt6.QtGui import QIcon, QAction
from genealogy.index_management import create_index, delete_index
from genealogy.bulk_load import cargar_datos_bulk
from genealogy.file_conversion import convertir_a_json

def create_menu(app):
    def _create_menu():
        menubar = app.menuBar()
        file_menu = menubar.addMenu("File")

        connect_action = QAction("Connect", app)
        connect_action.triggered.connect(app.connect_to_opensearch)
        file_menu.addAction(connect_action)

        export_json_action = QAction("Export to JSON", app)
        export_json_action.triggered.connect(lambda: convertir_a_json(app))
        file_menu.addAction(export_json_action)

        bulk_load_action = QAction("Load Bulk JSON", app)
        bulk_load_action.triggered.connect(lambda: cargar_datos_bulk(app))
        bulk_load_action.setEnabled(False)
        file_menu.addAction(bulk_load_action)

        exit_action = QAction("Exit", app)
        exit_action.triggered.connect(app.close)
        file_menu.addAction(exit_action)

        app.bulk_load_action = bulk_load_action

    _create_menu()

def create_main_layout(app):
    def _create_main_layout():
        app.central_widget = QWidget()
        app.layout = QVBoxLayout(app.central_widget)

        connection_group = QGroupBox("Connection Settings")
        connection_layout = QHBoxLayout()

        app.host_input = QLineEdit(app)
        app.host_input.setPlaceholderText("Host (e.g., localhost)")
        app.port_input = QLineEdit(app)
        app.port_input.setPlaceholderText("Port (e.g., 9200)")

        app.user_input = QLineEdit(app)
        app.user_input.setPlaceholderText("User (optional)")
        app.password_input = QLineEdit(app)
        app.password_input.setPlaceholderText("Password (optional)")
        app.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        app.connect_button = QPushButton("Connect", app)
        app.connect_button.clicked.connect(app.connect_to_opensearch)

        connection_layout.addWidget(QLabel("Host:"))
        connection_layout.addWidget(app.host_input)
        connection_layout.addWidget(QLabel("Port:"))
        connection_layout.addWidget(app.port_input)
        connection_layout.addWidget(QLabel("User:"))
        connection_layout.addWidget(app.user_input)
        connection_layout.addWidget(QLabel("Password:"))
        connection_layout.addWidget(app.password_input)
        connection_layout.addWidget(app.connect_button)

        connection_group.setLayout(connection_layout)
        app.layout.addWidget(connection_group)

        index_group = QGroupBox("Index Management")
        index_layout = QVBoxLayout()

        app.indices_list = QListWidget(app)
        app.indices_list.itemDoubleClicked.connect(app.show_index_content)
        app.refresh_button = QPushButton("Refresh Indices", app)
        app.refresh_button.clicked.connect(app.refresh_indices)
        app.create_index_button = QPushButton("Create Index", app)
        app.create_index_button.clicked.connect(lambda: create_index(app))
        app.delete_index_button = QPushButton("Delete Index", app)
        app.delete_index_button.clicked.connect(lambda: delete_index(app))

        index_layout.addWidget(app.indices_list)
        index_layout.addWidget(app.refresh_button)
        index_layout.addWidget(app.create_index_button)
        index_layout.addWidget(app.delete_index_button)

        index_group.setLayout(index_layout)
        app.layout.addWidget(index_group)

        app.setCentralWidget(app.central_widget)

    _create_main_layout()

def create_status_bar(app):
    def _create_status_bar():
        app.status_bar = QStatusBar()
        app.setStatusBar(app.status_bar)

    _create_status_bar()
