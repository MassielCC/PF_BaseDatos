from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri="##", user="##", password="##"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
      try:
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]
      except Exception as e:
        print(f"Error: {e}")
        return []

    def execute_query2(self, query, parameters=None):
        try:
            with self.driver.session() as session:
                result = session.run(query, parameters)
                return [record.data() for record in result]
        except Exception as e:
            print(f"Error: {e}")
            return []
