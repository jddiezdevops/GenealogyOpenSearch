from opensearchpy import OpenSearch

class OpenSearchClient:
    def __init__(self, host, port, user, password, use_ssl=False):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.use_ssl = use_ssl

        self.client = OpenSearch(
            hosts=[{'host': self.host, 'port': self.port}],
            http_auth=(self.user, self.password),
            use_ssl=self.use_ssl,
            verify_certs=self.use_ssl,
            ssl_show_warn=self.use_ssl
        )

    def get_indices(self):
        indices = self.client.indices.get_alias("*").keys()
        # Exclude indices that start with a dot (.)
        filtered_indices = [index for index in indices if not index.startswith('.')]
        return filtered_indices

    def get_index_content(self, index_name):
        try:
            response = self.client.search(index=index_name, size=10000)
            return response
        except Exception as e:
            raise
    
    def create_index(self, index_name, index_body):
        try:
            response = self.client.indices.create(index=index_name, body=index_body)
            return response
        except Exception as e:
            raise

    def delete_index(self, index_name):
        try:
            response = self.client.indices.delete(index=index_name)
            return response
        except Exception as e:
            raise
