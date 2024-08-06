# GenealogyOpenSearch

GenealogyOpenSearch es una aplicación de escritorio desarrollada en Python utilizando PyQt6 para gestionar registros genealógicos (bautismos y matrimonios) y almacenarlos en OpenSearch.

## Requisitos

- Python 3.6 o superior
- Las siguientes bibliotecas de Python:
  - opensearch-py
  - PyQt6
  - pandas

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/genealogy-opensearch.git
   cd genealogy-opensearch
   ```

2. Instala las dependencias

    ```bash
    pip install -r requirements.txt
    ```

##Uso

1. Ejecuta la aplicación:

    ```bash
    python main.py
    ```

2. Configura la conexión a OpenSearch proporcionando el host, puerto, usuario y contraseña.

3. Gestiona los índices de bautismos y matrimonios:
   - Crear, eliminar y visualizar índices.
   - Cargar datos en formato bulk desde un archivo JSON.
   - Convertir archivos Excel a JSON para carga bulk.

## Estructura del Proyecto

GenealogyOpenSearch/
├── .gitignore
├── bautismos_index.py
├── bulk_load.py
├── config.ini
├── config_handler.py
├── dialogs.py
├── event_handlers.py
├── file_conversion.py
├── genealogy_app.py
├── index_management.py
├── LICENSE
├── main.py
├── matrimonios_index.py
├── opensearch_client.py
├── README.md
└── ui_components.py

- `main.py`: Punto de entrada principal de la aplicación.
- `genealogy_app.py`: Contiene la lógica principal de la aplicación.
- `opensearch_client.py`: Maneja las conexiones y operaciones con OpenSearch.
- `config_handler.py`: Maneja la carga y guardado de configuraciones.
- `ui_components.py`: Contiene la creación y gestión de los componentes de la interfaz de usuario.
- `event_handlers.py`: Maneja los eventos de la aplicación.
- `dialogs.py`: Contiene los diálogos utilizados en la aplicación.
- `bulk_load.py`: Maneja la carga bulk de datos en OpenSearch.
- `file_conversion.py`: Contiene funciones para convertir archivos.
- `bautismos_index.py`: Define el mapeo del índice de bautismos.
- `matrimonios_index.py`: Define el mapeo del índice de matrimonios.

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (feature/nueva-funcionalidad).
3. Realiza los cambios necesarios y realiza commits.
4. Envía un pull request.
