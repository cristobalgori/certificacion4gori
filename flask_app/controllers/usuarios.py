from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def inicio(): 
    return render_template('index.html')

# Registro / Crear usuario
@app.route('/crear_usuario', methods=["POST"])
def crear_usuario():
    if not Usuario.validar_registro(request.form):
        flash("Datos de registro inválidos", "registro")
        return redirect('/')

    # Hasheamos la contraseña
    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])

    datos_usuario_registro = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': pass_hasheado
    }

    nuevo_id = Usuario.save(datos_usuario_registro)
    
    # Guardamos la sesión del usuario
    session['usuario_id'] = nuevo_id
    session['nombre'] = request.form['nombre']

    return redirect('/dashboard')  

# Inicio de sesión 
@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    if not Usuario.validar_inicio_sesion(request.form):
        flash("Datos de inicio de sesión inválidos", "inicio_sesion")
        return redirect('/')

    usuario = Usuario.get_by_email({'email': request.form.get('email')})
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form.get('password')):
        flash("E-mail o contraseña incorrectos", "inicio_sesion")
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['nombre'] = usuario.nombre
    return redirect('/dashboard')  

# Cerrar sesión
@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect('/')


