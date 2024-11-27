from conexion.no_relacional import Neo4jConnection

# Operacion con la base no relacional
def mostrar_nodos(etiqueta):
  resp_formateada = []
  conn = Neo4jConnection()
  query = f"MATCH (a:{etiqueta}) RETURN a"
  result = conn.execute_query(query)

  for elem in result:
      resp_formateada.append(elem["a"]._properties)

  conn.close()
  return resp_formateada

# Consulta para crear nodo y relacion
def crear_nodo_mascota(nombre, especie, raza, birth, condicion):
    conn = Neo4jConnection()
    query = f'CREATE (a:Pet {{nombre: "{nombre}", especie: "{especie}", raza: "{raza}", birth:"{birth}", condicion:"{condicion}" }}) RETURN a'
    result = conn.execute_query(query)

    conn.close()
    return result[0].data()

# Crear relaciones de mascota
def crear_relaciones_mascota(nombre_owner, nombre_pet, relacion, fecha):
  conn = Neo4jConnection()
  query = f'MATCH (a:Owner {{nombre: "{nombre_owner}"}}) WITH a MATCH (l:Pet {{nombre: "{nombre_pet}"}}) MERGE (a)-[:{relacion} {{fecha: {fecha}}}]->(l) RETURN a'
  result = conn.execute_query(query)

  conn.close()
  return result[0].data()