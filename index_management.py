from PyQt6.QtWidgets import QInputDialog, QMessageBox

def create_index(app):
    if not app.client:
        QMessageBox.warning(app, "Warning", "Not connected to OpenSearch")
        return

    index_name, ok = QInputDialog.getText(app, "Create Index", "Index Name:")
    if ok and index_name:
        items = ("Bautismos", "Matrimonios")
        item, ok = QInputDialog.getItem(app, "Select Index Type", "Index Type:", items, 0, False)
        if ok and item:
            index_type = item
            try:
                app.client.create_index(index_name, index_type)
                QMessageBox.information(app, "Index Creation", f"Index '{index_name}' created successfully")
                app.status_bar.showMessage(f"Index '{index_name}' created", 5000)
                app.refresh_indices()
            except Exception as e:
                QMessageBox.critical(app, "Error", str(e))
                app.status_bar.showMessage("Error creating index", 5000)

def delete_index(app):
    if not app.client:
        QMessageBox.warning(app, "Warning", "Not connected to OpenSearch")
        return

    selected_index = app.indices_list.currentItem()
    if not selected_index:
        QMessageBox.warning(app, "Warning", "Please select an index to delete")
        return

    index_name = selected_index.text()
    reply = QMessageBox.question(app, "Delete Index",
                                 f"Are you sure you want to delete the index '{index_name}'?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if reply == QMessageBox.StandardButton.Yes:
        try:
            app.client.delete_index(index_name)
            QMessageBox.information(app, "Index Deletion", f"Index '{index_name}' deleted successfully")
            app.status_bar.showMessage(f"Index '{index_name}' deleted", 5000)
            app.refresh_indices()
        except Exception as e:
            QMessageBox.critical(app, "Error", str(e))
            app.status_bar.showMessage("Error deleting index", 5000)
