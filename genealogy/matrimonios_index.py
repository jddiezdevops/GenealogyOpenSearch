matrimonios_index_body = {
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
            'Nombre del contrayente': {'type': 'text'},
            'Apellido del contrayente': {'type': 'text'},
            'Localidad del contrayente': {'type': 'text'},
            'Provincia del contrayente': {'type': 'text'},
            'Parroquia del contrayente': {'type': 'text'},
            'Nombre de la contrayente': {'type': 'text'},
            'Apellido de la contrayente': {'type': 'text'},
            'Localidad de la contrayente': {'type': 'text'},
            'Provincia de la contrayente': {'type': 'text'},
            'Parroquia de la contrayente': {'type': 'text'},
            'FECHA': {
                'type': 'date',
                'format': 'dd/MM/yyyy'
            },
            'Nombre del padre del contrayente': {'type': 'text'},
            'Apellido del padre del contrayente': {'type': 'text'},
            'Localidad del padre del contrayente': {'type': 'text'},
            'Provincia del padre del contrayente': {'type': 'text'},
            'Nombre de la madre del contrayente': {'type': 'text'},
            'Apellido de la madre del contrayente': {'type': 'text'},
            'Localidad de la madre del contrayente': {'type': 'text'},
            'Provincia de la madre del contrayente': {'type': 'text'},
            'Nombre del padre de la contrayente': {'type': 'text'},
            'Apellido del padre de la contrayente': {'type': 'text'},
            'Localidad del padre de la contrayente': {'type': 'text'},
            'Provincia del padre de la contrayente': {'type': 'text'},
            'Nombre de la madre de la contrayente': {'type': 'text'},
            'Apellido de la madre de la contrayente': {'type': 'text'},
            'Localidad de la madre de la contrayente': {'type': 'text'},
            'Provincia de la madre de la contrayente': {'type': 'text'},            
            'OBSERVACIONES': {'type': 'text'}
        }
    }
}
