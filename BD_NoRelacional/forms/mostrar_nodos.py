from conexion.no_relacional import Neo4jConnection

# Mostrar nodos, relaciones y nodos a los que esta conectado
def mostrar_todo(etiqueta):
    resp_formateada = []
    conn = Neo4jConnection()
    query = f'MATCH (node:{etiqueta})-[rel]-(connectedNode) RETURN node, rel, connectedNode'
    result = conn.execute_query(query)

    for elem in result:
        resp_formateada.append({"Nodo": elem["node"]._properties, "Relationships": elem["rel"].type,
                                "ConnectedNode": elem["connectedNode"]._properties})

    conn.close()
    return resp_formateada