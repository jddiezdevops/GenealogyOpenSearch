index_body = {
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
            'Nacimiento': {
                'type': 'date',
                'format': 'dd/MM/yyyy'
            },
            'Bautismo': {
                'type': 'date',
                'format': 'dd/MM/yyyy'
            },
            'Nombre': {'type': 'text'},
            'Nombre del padre': {'type': 'text'},
            'Apellido paterno': {'type': 'text'},
            'Localidad del padre': {'type': 'text'},
            'Provincia del padre': {'type': 'text'},
            'Parroquia del padre': {'type': 'text'},
            'Nombre de la madre': {'type': 'text'},
            'Apellido materno': {'type': 'text'},
            'Localidad de la madre': {'type': 'text'},
            'Provincia de la madre': {'type': 'text'},
            'Parroquia de la madre': {'type': 'text'},
            'Nombre Abuelo Paterno': {'type': 'text'},
            'Apellido Abuelo Paterno': {'type': 'text'},
            'Localidad Abuelo Paterno': {'type': 'text'},
            'Provincia Abuelo Paterno': {'type': 'text'},
            'Nombre Abuela Paterna': {'type': 'text'},
            'Apellido Abuela Paterna': {'type': 'text'},
            'Localidad Abuela Paterna': {'type': 'text'},
            'Provincia Abuela Paterna': {'type': 'text'},
            'Nombre Abuelo Materno': {'type': 'text'},
            'Apellido Abuelo Materno': {'type': 'text'},
            'Localidad Abuelo Materno': {'type': 'text'},
            'Provincia Abuelo Materno': {'type': 'text'},
            'Nombre Abuela Materna': {'type': 'text'},
            'Apellido Abuela Materna': {'type': 'text'},
            'Localidad Abuela Materna': {'type': 'text'},
            'Provincia Abuela Materna': {'type': 'text'},
            'OBSERVACIONES': {'type': 'text'}
        }
    }
}