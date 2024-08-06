import configparser

def load_credentials(app):
    app.config = configparser.ConfigParser()
    app.config.read('config.ini')

    if 'OpenSearch' in app.config:
        app.host = app.config['OpenSearch'].get('host', '')
        app.port = app.config['OpenSearch'].get('port', '')
        app.user = app.config['OpenSearch'].get('user', '')

        app.host_input.setText(app.host)
        app.port_input.setText(app.port)
        app.user_input.setText(app.user)

def save_credentials(app):
    if 'OpenSearch' not in app.config:
        app.config['OpenSearch'] = {}

    app.config['OpenSearch']['host'] = app.host
    app.config['OpenSearch']['port'] = app.port
    app.config['OpenSearch']['user'] = app.user

    with open('config.ini', 'w') as configfile:
        app.config.write(configfile)
