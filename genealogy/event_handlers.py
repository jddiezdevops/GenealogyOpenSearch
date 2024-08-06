from PyQt6.QtWidgets import QMessageBox, QListWidgetItem
from opensearchpy.exceptions import AuthenticationException, ConnectionError
from genealogy.opensearch_client import OpenSearchClient
from genealogy.dialogs import display_index_content
from genealogy.index_management import create_index, delete_index

def connect_to_opensearch(app):
    app.host = app.host_input.text()
    app.port = app.port_input.text()
    app.user = app.user_input.text()
    app.password = app.password_input.text()

    try:
        app.client = OpenSearchClient(app.host, app.port, app.user, app.password, use_ssl=False)
        if app.client.client.ping():
            QMessageBox.information(app, "Connection", "Connected to OpenSearch successfully")
            app.status_bar.showMessage("Connected to OpenSearch", 5000)
            app.refresh_indices()
            app.bulk_load_action.setEnabled(True)
            app.save_credentials()
        else:
            raise ConnectionError("Failed to connect to OpenSearch")
    except (AuthenticationException, ConnectionError):
        QMessageBox.critical(app, "Connection Error", "Failed to connect to OpenSearch. Please check your connection details (host, port, username, password).")
        app.status_bar.showMessage("Connection Error", 5000)
    except Exception as e:
        QMessageBox.critical(app, "Error", f"An unexpected error occurred: {str(e)}")
        app.status_bar.showMessage("Error", 5000)

def refresh_indices(app):
    if not app.client:
        QMessageBox.warning(app, "Warning", "Not connected to OpenSearch")
        return

    app.indices_list.clear()
    try:
        indices = app.client.get_indices()
        for index in indices:
            item = QListWidgetItem(index)
            app.indices_list.addItem(item)
        app.status_bar.showMessage("Indices refreshed", 5000)
    except Exception as e:
        QMessageBox.critical(app, "Error", str(e))
        app.status_bar.showMessage("Error refreshing indices", 5000)

def show_index_content(app, item):
    if not isinstance(item, QListWidgetItem):
        item = app.indices_list.currentItem()

    if isinstance(item, QListWidgetItem):
        index_name = item.text()
        try:
            content = app.client.get_index_content(index_name)
            display_index_content(app, index_name, content)
        except Exception as e:
            print(f"DEBUG: show_index_content error: {str(e)}")
            QMessageBox.critical(app, "Error", str(e))
            app.status_bar.showMessage("Error showing index content", 5000)
    else:
        QMessageBox.critical(app, "Error", "Invalid item selected.")
        app.status_bar.showMessage("Error showing index content", 5000)
