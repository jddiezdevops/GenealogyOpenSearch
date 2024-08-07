import pandas as pd
import json
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QInputDialog

def generate_excel_template(index_name, index_body):
    # Extract column names from index body
    columns = list(index_body['mappings']['properties'].keys())
    # Create a DataFrame with these columns
    df = pd.DataFrame(columns=columns)
    # Save DataFrame to Excel file
    excel_file_name = f"{index_name}_template.xlsx"
    df.to_excel(excel_file_name, index=False)
    print(f"Excel template '{excel_file_name}' generated successfully.")
    QMessageBox.information(None, "Excel Template", f"Excel template '{excel_file_name}' generated successfully.")

def convertir_a_json(parent):
    try:
        archivo_excel, _ = QFileDialog.getOpenFileName(parent, "Seleccionar archivo Excel", "", "Archivos Excel (*.xlsx)")
        if archivo_excel:
            nombre_indice, ok = QInputDialog.getText(parent, "Nombre del índice", "Introduce el nombre del índice para Elasticsearch:")
            if ok and nombre_indice:
                data = pd.read_excel(archivo_excel)
                archivo_json, _ = QFileDialog.getSaveFileName(parent, "Guardar archivo JSON", "", "Archivos JSON (*.json)")
                if archivo_json:
                    with open(archivo_json, 'w', encoding='utf-8') as f:
                        for _, row in data.iterrows():
                            meta_dict = {"index": {"_index": nombre_indice}}
                            f.write(json.dumps(meta_dict) + '\n')
                            f.write(row.to_json(force_ascii=False, date_format='iso') + '\n')
                        f.write('\n')
                    QMessageBox.information(parent, "Éxito", f'Se ha convertido {archivo_excel} a {archivo_json} en formato Bulk')
            else:
                QMessageBox.warning(parent, "Error", "No se ingresó un nombre de índice.")
    except Exception as e:
        QMessageBox.critical(parent, "Error", str(e))
