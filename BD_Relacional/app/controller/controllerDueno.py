from conexion.conexionBD import connectionBD  #Importando conexion BD

#Creando una funcion para obtener la lista de carros.
def listaDuenos():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur= conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Dueño ORDER BY idDueno DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda

def updateDueno(idDueno=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Dueño WHERE idDueno = %s LIMIT 1", [idDueno])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
def registrarDueno(TipoDoc='', NumDoc='', Nombre='', Apellido='', FechaNac='', EsBuscador=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO Dueño(TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador) VALUES (%s, %s, %s, %s, %s, %s)")
        valores     = (TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  
def detallesdelDueno(idDueno):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM Dueño WHERE idDueno ='%s'" % (idDueno,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    

def  recibeActualizarDueno(TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador, idDueno):
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE Dueño
            SET 
                TipoDoc   = %s,
                NumDoc  = %s,
                Nombre    = %s,
                Apellido   = %s, 
                FechaNac   = %s,
                EsBuscador   = %s        
            WHERE idDueno=%s
            """, (TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador, idDueno))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update