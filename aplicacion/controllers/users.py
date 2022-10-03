from flask import render_template, request, redirect
from aplicacion import app
from aplicacion.models.user import Usuario

@app.route("/users/new")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("crear.html", usuarios=usuarios)

@app.route('/crear_usuario', methods=["POST"])
def crear_usuario():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "nombre": request.form["nombre"],
        "apellido" : request.form["apellido"],
        "correo" : request.form["correo"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Usuario.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users')

@app.route('/users')
def mostrar_usuarios():
    usuarios = Usuario.get_all()
    return render_template("todos.html", usuarios=usuarios)

@app.route('/agregar', methods=["POST"])
def agregar():
    return redirect('/users/new')

@app.route('/volver', methods=["POST"])
def volver():
    return redirect('/users')