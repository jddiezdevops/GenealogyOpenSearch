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
            'Nombre': {'type': 'text'},
            'Apellido': {'type': 'text'},
            'Localidad': {'type': 'text'},
            'Provincia': {'type': 'text'},
            'Parroquia': {'type': 'text'},
            'FECHA': {
                'type': 'date',
                'format': 'dd/MM/yyyy'
            },
            'N. Padre': {'type': 'text'},
            'A. Padre': {'type': 'text'},
            'Localidad Padre': {'type': 'text'},
            'Provincia Padre': {'type': 'text'},
            'N. Madre': {'type': 'text'},
            'A. Madre': {'type': 'text'},
            'Localidad Madre': {'type': 'text'},
            'Provincia Madre': {'type': 'text'},
            'N. Padre': {'type': 'text'},
            'A. Padre': {'type': 'text'},
            'Localidad Padre': {'type': 'text'},
            'Provincia Padre': {'type': 'text'},
            'N. Madre': {'type': 'text'},
            'A. Madre': {'type': 'text'},
            'Localidad Madre': {'type': 'text'},
            'Provincia Madre': {'type': 'text'},
            'OBSERVACIONES': {'type': 'text'}
        }
    }
}
