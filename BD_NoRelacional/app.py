from flask import Flask, render_template, redirect, url_for, jsonify, request, abort
from forms.mostrar_nodos import mostrar_todo
from conexion.no_relacional import *

# Crear instancia de Flask
app = Flask(__name__)

# Configuración (puedes agregar más configuraciones aquí)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fee'

# Ruta principal
@app.route('/')
def index():
    return render_template('base.html')

# Rutas
@app.route('/owner', methods=['GET', 'POST'])
def owner():
    return render_template('show_owner.html', datos=mostrar_todo("Owner"))

@app.route('/mascota', methods=['GET', 'POST'])
def mascota():
    return render_template('show_mascota.html', datos=mostrar_todo("Pet"))

@app.route('/cita')
def cita():
    return render_template('show_cita.html', datos=mostrar_todo("Cita"))

@app.route('/veterinario')
def veterinario():
    return render_template('show_veterinario.html', datos=mostrar_todo("Veterinario"))

@app.route('/nuevo_owner', methods=['GET'])
def new_Owner():
    return render_template('nuevo_owner.html')

@app.route('/nuevo_mascota', methods=['GET'])
def new_Pet():
    return render_template('nuevo_mascota.html')

@app.route('/nuevo_cita', methods=['GET'])
def new_Cita():
    return render_template('nuevo_cita.html')

@app.route('/nuevo_veterinario', methods=['GET'])
def new_Vet():
    return render_template('nuevo_veterinario.html')

@app.route('/editar_owner', methods=['GET'])
def edit_Owner():
    return render_template('editar_owner.html')

@app.route('/editar_mascota', methods=['GET'])
def edit_Pet():
    return render_template('editar_mascota.html')

@app.route('/editar_cita', methods=['GET'])
def edit_Cita():
    return render_template('editar_cita.html')

@app.route('/editar_veterinario', methods=['GET'])
def edit_Vet():
    return render_template('editar_veterinario.html')

@app.route('/eliminar_owner', methods=['GET'])
def eliminar_Owner():
    return render_template('eliminar_owner.html')

@app.route('/eliminar_mascota', methods=['GET'])
def eliminar_Pet():
    return render_template('eliminar_mascota.html')

@app.route('/eliminar_cita', methods=['GET'])
def eliminar_Cita():
    return render_template('eliminar_cita.html')

@app.route('/eliminar_veterinario', methods=['GET'])
def eliminar_Vet():
    return render_template('eliminar_veterinario.html')

@app.route('/create_owner', methods=['POST'])
def create_owner():
    conn = Neo4jConnection()
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    dni = request.form.get('dni')

    if name and lastname and dni:
        query=f'CREATE (a:Owner {{nombre:"{name}", apellido: "{lastname}", dni: "{dni}"}}) RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/create_mascota', methods=['POST'])
def create_mascota():
    conn = Neo4jConnection()
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    raza = request.form.get('raza')

    if nombre and especie and raza:
        query=f'CREATE (a:Pet {{nombre:"{nombre}", especie: "{especie}", raza: "{raza}"}}) RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/create_cita', methods=['POST'])
def create_cita():
    conn = Neo4jConnection()
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    id = request.form.get('id')

    if fecha and hora and id:
        query=f'CREATE (a:Cita {{fecha:"{fecha}", hora: "{hora}", id: "{id}"}}) RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/create_vet', methods=['POST'])
def create_vet():
    conn = Neo4jConnection()
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    especialidad = request.form.get('especialidad')

    if name and lastname and especialidad:
        query=f'CREATE (a:Veterinario {{nombre:"{name}", apellido: "{lastname}", especialidad: "{especialidad}"}}) RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/update_owner', methods=['POST'])
def update_owner():
    conn = Neo4jConnection()
    dni = request.form.get('dni')
    name = request.form.get('name')
    lastname = request.form.get('lastname')

    if dni and name and lastname:
        query=f'MATCH (a:Owner {{dni: "{dni}"}}) SET a.nombre="{name}", a.apellido="{lastname}" RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/update_pet', methods=['PUT'])
def update_pet():
    conn = Neo4jConnection()
    name = request.form.get('nombre')
    condicion = request.form.get('condicion')

    if name and condicion:
        query=f'MATCH (a:Pet {{nombre: "{name}"}}) SET a.condicion="{condicion}" RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/update_cita', methods=['PUT'])
def update_cita():
    conn = Neo4jConnection()
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    id = request.form.get('id')

    if fecha and hora and id:
        query=f'MATCH (a:Cita {{id: "{id}"}}) SET a.fecha="{fecha}", a.hora="{hora}"  RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/update_vet', methods=['PUT'])
def update_vet():
    conn = Neo4jConnection()
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    especialidad = request.form.get('especialidad')

    if name and lastname and especialidad:
        query = f'CREATE (a:Veterinario {{nombre:"{name}"}}) SET a.apellido="{lastname}", a.especialidad="{especialidad}" RETURN a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/delete_owner', methods=['POST'])
def delete_owner():
    conn = Neo4jConnection()
    dni = request.form.get('dni')

    if dni:
        query=f'MATCH (a:Owner {{dni: "{dni}"}}) DETACH DELETE a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/delete_pet', methods=['DELETE'])
def delete_pet():
    conn = Neo4jConnection()
    name = request.form.get('nombre')

    if name:
        query=f'MATCH (a:Pet {{nombre: "{name}"}}) DETACH DELETE a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/delete_cita', methods=['DELETE'])
def delete_cita():
    conn = Neo4jConnection()
    id = request.form.get('id')

    if id:
        query=f'MATCH (a:Cita {{id: "{id}"}}) DETACH DELETE a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

@app.route('/delete_vet', methods=['DELETE'])
def delete_vet():
    conn = Neo4jConnection()
    name = request.form.get('name')

    if name:
        query = f'MATCH (a:Veterinario {{nombre:"{name}"}}) DETACH DELETE a'
        result = conn.execute_query2(query)
        #print(result)
        return jsonify(result),201
    else:
        return abort(400)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
