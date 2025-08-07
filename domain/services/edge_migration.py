def migrate_edge(source_client, dest_client, edge_id):
    config = source_client.get_edge_config(edge_id)
    if not config:
        raise Exception("Edge no encontrado")
    return dest_client.create_edge(config)
