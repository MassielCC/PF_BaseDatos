from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerMascota import *
from controller.controllerDueno import *
from controller.controllerMePerdi import *
from conexion.conexionBD import connectionBD

#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

msg  =''
tipo =''

#Creando decorador para el inicio, mascota, dueño, meperdi
@app.route('/')
def index():
    return render_template('public/base.html')

@app.route('/mascota', methods=['GET','POST'])
def inicioMascota():
    return render_template('public/layout.html', miData = listaMascotas())

@app.route('/dueno', methods=['GET','POST'])
def inicioDueno():
    return render_template('public/layoutDueno.html', miData = listaDuenos())

@app.route('/MePerdi', methods=['GET','POST'])
def inicioMePerdi():
    return render_template('public/layoutMePerdi.html', miData = listaPerdidas())

#Páginas de registro
@app.route('/registrar-mascota', methods=['GET','POST'])
def addMascota():
    return render_template('public/acciones/add.html')

@app.route('/registrar-dueno', methods=['GET','POST'])
def addDueno():
    return render_template('public/acciones/addDueno.html')

@app.route('/registrar-MePerdi', methods=['GET','POST'])
def addMePerdi():
    return render_template('public/acciones/addMePerdi.html')

#Formularios para INSERT mascota
@app.route('/mascotaForm', methods=['POST'])
def formAddMascota():
    if request.method == 'POST':
        Nombre= request.form['Nombre']
        Animal= request.form['Animal']
        Raza  = request.form['Raza']
        FechaNac = request.form['FechaNac']
        
        resultData = registrarMascota(Nombre, Animal, Raza, FechaNac)
        if(resultData ==1):
            return render_template('public/layout.html', miData = listaMascotas(), msg='El Registro fue un éxito', tipo=1)
        else:
            return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto', tipo=1)   
            
#Registrando nuevo dueño
@app.route('/duenoForm', methods=['POST'])
def formAddDueno():
    if request.method == 'POST':
        TipoDoc= request.form['TipoDoc']
        NumDoc = request.form['NumDoc']
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        FechaNac = request.form['FechaNac']
        EsBuscador = request.form['EsBuscador']
        
        resultData = registrarDueno(TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador)
        if(resultData ==1):
            return render_template('public/layoutDueno.html', miData = listaDuenos(), msg='El Registro fue un éxito', tipo=1)
        else:
            return render_template('public/layoutDueno.html', msg = 'Metodo HTTP incorrecto', tipo=1)   

@app.route('/MePerdiForm', methods=['POST'])
def formAddMePerdi():
    if request.method == 'POST':
        Direccion = request.form['Direccion']
        Distrito = request.form['Distrito']
        Provincia = request.form['Provincia']
        Fecha = request.form['Fecha']
        Mascota_idMascota1 = request.form['Mascota_idMascota1']
        
        resultData = registrarPerdida(Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1)
        if(resultData ==1):
            return render_template('public/layoutMePerdi.html', miData = listaPerdidas(), msg='El Registro fue un éxito', tipo=1)
        else:
            return render_template('public/layoutMePerdi.html', msg = 'Metodo HTTP incorrecto', tipo=1)   


@app.route('/form-update-mascota/<string:idMascota>', methods=['GET','POST'])
def formViewUpdateMascota(idMascota):
    if request.method == 'GET':
        resultData = updateMascota(idMascota)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            return render_template('public/layout.html', miData = listaMascotas(), msg='No existe la mascota', tipo= 1)
    else:
        return render_template('public/layout.html', miData = listaMascotas(), msg = 'Metodo HTTP incorrecto', tipo=1)

@app.route('/form-update-dueno/<string:idDueno>', methods=['GET','POST'])
def formViewUpdateDueno(idDueno):
    if request.method == 'GET':
        resultData = updateDueno(idDueno)
        if resultData:
            return render_template('public/acciones/updateDueno.html',  dataInfo = resultData)
        else:
            return render_template('public/layoutDueno.html', miData = listaDuenos(), msg='No existe el dueño', tipo= 1)
    else:
        return render_template('public/layoutDueno.html', miData = listaDuenos(), msg = 'Metodo HTTP incorrecto', tipo=1)          

@app.route('/form-update-MePerdi/<string:idMePerdi>', methods=['GET','POST'])
def formViewUpdateMePerdi(idMePerdi):
    if request.method == 'GET':
        resultData = updatePerdida(idMePerdi)
        if resultData:
            return render_template('public/acciones/updateMePerdi.html',  dataInfo = resultData)
        else:
            return render_template('public/layoutMePerdi.html', miData = listaPerdidas(), msg='No existe la perdida', tipo= 1)
    else:
        return render_template('public/layoutMePerdi.html', miData = listaPerdidas(), msg = 'Metodo HTTP incorrecto', tipo=1)

@app.route('/ver-detalles-del-mascota/<int:idMascota>', methods=['GET', 'POST'])
def viewDetalleMascota(idMascota):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelMascota(idMascota) #Funcion que almacena los detalles de la mascota
        
        if resultData:
            return render_template('public/acciones/view.html', infoMascota = resultData, msg='Detalles del mascota', tipo=1)
        else:
            return render_template('public/acciones/layout.html', msg='No existe el mascota', tipo=1)
    return redirect(url_for('inicioMascota'))

@app.route('/ver-detalles-del-dueno/<int:idDueno>', methods=['GET', 'POST'])
def viewDetalleDueno(idDueno):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelDueno(idDueno) #Funcion que almacena los detalles de la mascota
        
        if resultData:
            return render_template('public/acciones/viewDueno.html', infoDueno = resultData, msg='Detalles del dueño', tipo=1)
        else:
            return render_template('public/acciones/layoutDueno.html', msg='No existe el dueño', tipo=1)
    return redirect(url_for('inicioDueno'))

@app.route('/ver-detalles-del-MePerdi/<int:idMePerdi>', methods=['GET', 'POST'])
def viewDetalleMePerdi(idMePerdi):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelPerdida(idMePerdi) #Funcion que almacena los detalles de la mascota
        
        if resultData:
            return render_template('public/acciones/viewMePerdi.html', infoMePerdi = resultData, msg='Detalles del me perdi', tipo=1)
        else:
            return render_template('public/acciones/layoutMePerdi.html', msg='No existe la perdida', tipo=1)
    return redirect(url_for('inicioMePerdi'))
    
@app.route('/actualizar-mascota/<string:idMascota>', methods=['POST'])
def  formActualizarMascota(idMascota):
    if request.form['_method'] == 'PUT':
        Nombre = request.form['Nombre']
        Animal = request.form['Animal']
        Raza = request.form['Raza']
        FechaNac = request.form['FechaNac']
        
        resultData = recibeActualizarMascota(Nombre, Animal, Raza, FechaNac, idMascota)

        if(resultData ==1):
            return render_template('public/layout.html', miData = listaMascotas(), msg='Datos del mascota actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layout.html', miData = listaMascotas(), msg='No se pudo actualizar', tipo=1)

@app.route('/actualizar-dueno/<string:idDueno>', methods=['POST'])
def  formActualizarDueno(idDueno):
    if request.form['_method'] == 'PUT':
        TipoDoc = request.form['TipoDoc']
        NumDoc = request.form['NumDoc']
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        FechaNac = request.form['FechaNac']
        EsBuscador= request.form['EsBuscador']
        
        resultData = recibeActualizarDueno(TipoDoc, NumDoc, Nombre, Apellido, FechaNac, EsBuscador, idDueno)

        if(resultData ==1):
            return render_template('public/layoutDueno.html', miData = listaDuenos(), msg='Datos del dueño actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layoutDueno.html', miData = listaDuenos(), msg='No se pudo actualizar', tipo=1)

@app.route('/actualizar-MePerdi/<string:idMePerdi>', methods=['POST'])
def  formActualizarMePerdi(idMePerdi):
    if request.form['_method'] == 'PUT':
        Direccion = request.form['Direccion']
        Distrito = request.form['Distrito']
        Provincia = request.form['Provincia']
        Fecha= request.form['Fecha']
        Mascota_idMascota1= request.form['Mascota_idMascota1']
        
        resultData = recibeActualizarMePerdi(Direccion, Distrito, Provincia, Fecha, Mascota_idMascota1, idMePerdi)

        if(resultData ==1):
            return render_template('public/layoutMePerdi.html', miData = listaPerdidas(), msg='Datos del me perdi actualizados', tipo=1)
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layoutMePerdi.html', miData = listaPerdidas(), msg='No se pudo actualizar', tipo=1)

@app.route('/borrar-mascota', methods=['GET', 'POST'])
def formViewBorrarMascota():
    if request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            idMascota = request.form['idMascota']
            resultData = eliminarMascota(idMascota)

            if resultData ==1:#Nota: retorno solo un json y no una vista para evitar refescar la vista
                return jsonify([1])
            #return jsonify(["respuesta", 1])
            else: 
                return jsonify([0])
    else: 
        return jsonify([0])
#Eliminar dueno
@app.route('/borrar-dueno', methods=['GET', 'POST'])
def formViewBorrarDueno():
    if request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            idDueno= request.form['idDueno']
            resultData= eliminarDueno(idDueno)

            if resultData ==1:#Nota: retorno solo un json y no una vista para evitar refescar la vista
                return jsonify([1])
            #return jsonify(["respuesta", 1])
            else: 
                return jsonify([0])
    else: 
        return jsonify([0])

@app.route('/borrar-MePerdi', methods=['GET', 'POST'])
def formViewBorrarMePerdi():
    if request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            idMePerdi = request.form['idMePerdi']
            resultData = eliminarMePerdi(idMePerdi)

            if resultData ==1:#Nota: retorno solo un json y no una vista para evitar refescar la vista
                return jsonify([1])
            #return jsonify(["respuesta", 1])
            else: 
                return jsonify([0])
        else: 
            return jsonify([0])

def eliminarMascota(idMascota=''):
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur= conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM Mascota WHERE idMascota=%s', (idMascota,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    return resultado_eliminar

def eliminarDueno(idDueno=''):
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur = conexion_MySQLdb.cursor(dictionary=True)

    cur.execute('DELETE FROM Dueño WHERE idDueno=%s', (idDueno,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    return resultado_eliminar

def eliminarMePerdi(idMePerdi=''):
    conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
    cur = conexion_MySQLdb.cursor(dictionary=True)
    
    cur.execute('DELETE FROM MePerdi WHERE idMePerdi=%s', (idMePerdi,))
    conexion_MySQLdb.commit()
    resultado_eliminar = cur.rowcount #retorna 1 o 0
    #print(resultado_eliminar)
    #os.unlink(url_File) #Otra forma de borrar archivos en una carpeta
    return resultado_eliminar

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicioMePerdi'))
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)