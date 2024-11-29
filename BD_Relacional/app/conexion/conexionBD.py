import mysql.connector
from mysql.connector import Error

def connectionBD():
    host = "autorack.proxy.rlwy.net"
    database = "mydb"
    user = "root"
    password = "##"
    port = 26440

    try:
        # Intentar la conexión
        conexion = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            # Retornar conexión si es exitosa
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None