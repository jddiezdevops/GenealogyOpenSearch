import subprocess
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QInputDialog, QLineEdit

def cargar_datos_bulk(parent):
    try:
        if not parent.client:
            QMessageBox.warning(parent, "Error", "No estás conectado a OpenSearch.")
            return
        
        archivo_json, _ = QFileDialog.getOpenFileName(parent, "Seleccionar archivo JSON", "", "Archivos JSON (*.json)")
        if not archivo_json:
            QMessageBox.warning(parent, "Error", "Debes seleccionar un archivo JSON.")
            return

        url_opensearch = f"http://{parent.host}:{parent.port}"
        nombre_indice, ok = QInputDialog.getText(parent, "Nombre del índice", "Introduce el nombre del índice para Elasticsearch:")
        if not ok or not nombre_indice:
            QMessageBox.warning(parent, "Error", "Debes introducir el nombre del índice.")
            return

        usuario = parent.user
        password = parent.password

        comando_curl = [
            "curl",
            "-k",
            "-u", f"{usuario}:{password}" if usuario and password else "",
            "-X", "POST",
            f"{url_opensearch}/_bulk",
            "-H", "Content-Type: application/x-ndjson",
            "--data-binary", f"@{archivo_json}"
        ]
        resultado = subprocess.run(comando_curl, capture_output=True, text=True)
        print(resultado.stdout)  # Imprime la salida de curl

        if resultado.returncode == 0:
            QMessageBox.information(parent, "Información", "Datos enviados a OpenSearch correctamente.")
        else:
            QMessageBox.critical(parent, "Error", resultado.stderr)
    except Exception as e:
        QMessageBox.critical(parent, "Error", str(e))

