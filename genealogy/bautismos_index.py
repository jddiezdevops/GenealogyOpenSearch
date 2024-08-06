# bautismos_index.py

bautismos_index_body = {
    'settings': {
        'index': {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
    },
    'mappings': {
        'properties': {
            'LIBRO': {'type': 'text'},
            'FOLIO': {'type': 'text'},
            'Nacimiento': {'type': 'date', 'format': 'dd/MM/yyyy'},
            'Bautismo': {'type': 'date', 'format': 'dd/MM/yyyy'},
            'Nombre': {'type': 'text'},
            'Nombre del padre': {'type': 'text'},
            'Apellido del padre': {'type': 'text'},
            'Localidad del padre': {'type': 'text'},
            'Provincia del padre': {'type': 'text'},
            'Parroquia del padre': {'type': 'text'},
            'Nombre de la madre': {'type': 'text'},
            'Apellido de la madre': {'type': 'text'},
            'Localidad de la madre': {'type': 'text'},
            'Provincia de la madre': {'type': 'text'},
            'Parroquia de la madre': {'type': 'text'},
            'Nombre del abuelo paterno': {'type': 'text'},
            'Apellido del abuelo paterno': {'type': 'text'},
            'Localidad del abuelo paterno': {'type': 'text'},
            'Provincia del abuelo paterno': {'type': 'text'},
            'Nombre de la abuela paterna': {'type': 'text'},
            'Apellido de la abuela paterna': {'type': 'text'},
            'Localidad de la abuela paterna': {'type': 'text'},
            'Provincia de la abuela paterna': {'type': 'text'},
            'Nombre del abuelo materno': {'type': 'text'},
            'Apellido del abuelo materno': {'type': 'text'},
            'Localidad del abuelo materno': {'type': 'text'},
            'Provincia del abuelo materno': {'type': 'text'},
            'Nombre de la abuela materna': {'type': 'text'},
            'Apellido de la abuela materna': {'type': 'text'},
            'Localidad de la abuela materna': {'type': 'text'},
            'Provincia de la abuela materna': {'type': 'text'},
            'OBSERVACIONES': {'type': 'text'}
        }
    }
}
