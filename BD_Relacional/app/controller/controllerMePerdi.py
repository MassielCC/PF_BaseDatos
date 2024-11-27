from conexion.conexionBD import connectionBD 

#Creando una funcion para obtener la lista de mascotas perdidas
def listaPerdidas():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM MePerdi ORDER BY idMePerdi DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def updatePerdida(idMePerdi=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM MePerdi WHERE idMePerdi = %s LIMIT 1", [idMePerdi])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
def registrarPerdida(Direccion='', Distrito='', Provincia='', Fecha='', Mascota_idMascota1=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO MePerdi(Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1) VALUES (%s, %s, %s, %s, %s)")
        valores     = (Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  
def detallesdelPerdida(idMePerdi):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM MePerdi WHERE idMePerdi ='%s'" % (idMePerdi,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    

def  recibeActualizarMePerdi(Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1, idMePerdi):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE MePerdi
            SET 
                Direccion   = %s,
                Distrito  = %s,
                Provincia    = %s,
                Fecha   = %s, 
                Mascota_idMascota1   = %s    
            WHERE idMePerdi=%s
            """, (Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1, idMePerdi))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update