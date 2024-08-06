from opensearchpy import OpenSearch, ConnectionError
import bautismos_index
import matrimonios_index

class OpenSearchClient:
    def __init__(self, host, port, user=None, password=None):
        if user and password:
            self.client = OpenSearch(
                hosts=[{'host': host, 'port': port}],
                http_auth=(user, password),
                use_ssl=False,
                verify_certs=False,
                ssl_show_warn=False
            )
        else:
            self.client = OpenSearch(
                hosts=[{'host': host, 'port': port}],
                use_ssl=False,
                verify_certs=False,
                ssl_show_warn=False
            )

    def get_indices(self):
        all_indices = self.client.indices.get_alias("*").keys()
        # Filtrar índices que no comienzan con un punto
        user_indices = [index for index in all_indices if not index.startswith('.')]
        return user_indices

    def create_index(self, index_name, index_type):
        if index_type == "Bautismos":
            index_body = bautismos_index.index_body
        elif index_type == "Matrimonios":
            index_body = matrimonios_index.index_body
        response = self.client.indices.create(index=index_name, body=index_body, ignore=400)
        return response

    def delete_index(self, index_name):
        self.client.indices.delete(index=index_name)

    def get_index_content(self, index_name):
        response = self.client.search(index=index_name, body={"query": {"match_all": {}}}, size=10000)
        hits = response['hits']['hits']
        return [hit['_source'] for hit in hits]
