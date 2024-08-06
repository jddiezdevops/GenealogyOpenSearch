from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QDialogButtonBox

def display_index_content(app, index_name, content):
    try:
        dialog = QDialog(app)
        dialog.setWindowTitle(f"Content of index: {index_name}")

        layout = QVBoxLayout()

        label = QLabel(f"Content of index: {index_name}")
        layout.addWidget(label)

        if 'hits' in content and 'hits' in content['hits']:
            hits = content['hits']['hits']
            
            if hits:
                # Create table
                table = QTableWidget()
                table.setRowCount(len(hits))
                # Set column count based on the first document's fields
                first_doc = hits[0]['_source']
                table.setColumnCount(len(first_doc))
                table.setHorizontalHeaderLabels(first_doc.keys())

                # Populate the table
                for row_idx, hit in enumerate(hits):
                    for col_idx, key in enumerate(first_doc.keys()):
                        value = str(hit['_source'].get(key, ''))
                        table.setItem(row_idx, col_idx, QTableWidgetItem(value))

                layout.addWidget(table)
            else:
                no_data_label = QLabel("No data found.")
                layout.addWidget(no_data_label)
        else:
            no_data_label = QLabel("No data found.")
            layout.addWidget(no_data_label)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(dialog.accept)
        layout.addWidget(buttons)

        dialog.setLayout(layout)
        dialog.exec()
    except Exception as e:
        print(f"DEBUG: display_index_content error: {str(e)}")
        raise
