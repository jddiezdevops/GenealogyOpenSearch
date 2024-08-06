from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QScrollArea, QWidget

def display_index_content(parent, index_name, content):
    dialog = QDialog(parent)
    dialog.setWindowTitle(f"Contents of Index: {index_name}")
    layout = QVBoxLayout()

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    container = QWidget()
    container_layout = QVBoxLayout(container)

    table = QTableWidget()
    if content:
        headers = content[0].keys()
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        table.setRowCount(len(content))
        for row_idx, row_data in enumerate(content):
            for col_idx, (col_name, col_value) in enumerate(row_data.items()):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_value)))

    container_layout.addWidget(table)
    container.setLayout(container_layout)
    scroll.setWidget(container)

    layout.addWidget(scroll)
    dialog.setLayout(layout)
    dialog.setGeometry(100, 100, 800, 600)
    dialog.exec()
