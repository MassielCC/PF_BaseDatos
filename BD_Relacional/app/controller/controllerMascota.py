from conexion.conexionBD import connectionBD 

#Creando una funcion para obtener la lista de carros.
def listaMascotas():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Mascota ORDER BY idMascota DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def updateMascota(idMascota=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Mascota WHERE idMascota = %s LIMIT 1", [idMascota])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData

def registrarMascota(Nombre='', Animal='', Raza='', FechaNac=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO Mascota(Nombre, Animal, Raza, FechaNac) VALUES (%s, %s, %s, %s)")
        valores     = (Nombre, Animal, Raza, FechaNac)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  
def detallesdelMascota(idMascota):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Mascota WHERE idMascota ='%s'" % (idMascota,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    

def  recibeActualizarMascota(Nombre, Animal, Raza, FechaNac, idMascota):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE Mascota
            SET 
                Nombre   = %s,
                Animal  = %s,
                Raza    = %s,
                FechaNac   = %s
            WHERE idMascota=%s
            """, (Nombre, Animal, Raza, FechaNac, idMascota))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update