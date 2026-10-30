from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.libro import Libro
from flask_app.models.usuario import Usuario

# 1. DASHBOARD: Muestra la pantalla principal con los libros
@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para ver esta página", "inicio_sesion")
        return redirect('/')
    
    usuario_en_sesion = Usuario.get_one({'id': session['usuario_id']})
    libros = Libro.get_all() # Trae los libros ordenados por fecha
    
    return render_template('dashboard.html', usuario=usuario_en_sesion, libros=libros)

# 2. CREAR LIBRO (GET): Muestra el formulario para crear libro
@app.route('/crear_libro')
def crear_libro():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('crear_libro.html')

# 3. CREAR LIBRO (POST): Procesa el formulario de crear libro
@app.route('/crear_libro', methods=['POST'])
def guardar_libro():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Libro.validar_libro(request.form):
        return redirect('/crear_libro')

    datos = {
        'titulo': request.form['titulo'],
        'autor': request.form['autor'],
        'sinopsis': request.form['sinopsis'],
        'usuario_id': session['usuario_id']
    }

    if not Libro.save(datos):
        flash("No se pudo guardar el libro. Inténtalo nuevamente.", "crear_libro")
        return redirect('/crear_libro')

    return redirect('/dashboard')

# 4. VER DETALLE DE LIBRO
@app.route('/ver/<int:id>')
def ver_libro(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    libro = Libro.get_one({'id': id})
    return render_template('ver.html', libro=libro)

# 5. EDITAR LIBRO (GET)
@app.route('/editar/<int:id>')
def editar_libro(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    libro = Libro.get_one({'id': id})
    
    # BONUS: Validar que el usuario sea el creador del libro
    if libro.usuario_id != session['usuario_id']:
        flash("No puedes editar libros de otros usuarios", "dashboard")
        return redirect('/dashboard')

    return render_template('editar.html', libro=libro)

# 6. ACTUALIZAR LIBRO (POST)
@app.route('/actualizar_libro/<int:id>', methods=['POST'])
def actualizar_libro(id):
    if 'usuario_id' not in session:
        return redirect('/')

    if not Libro.validar_libro(request.form):
        return redirect(f'/editar/{id}')

    datos = {
        'id': id,
        'titulo': request.form['titulo'],
        'autor': request.form['autor'],
        'sinopsis': request.form['sinopsis'],
        'usuario_id': session['usuario_id']
    }

    Libro.update(datos)
    return redirect('/dashboard')

# 7. BORRAR LIBRO
@app.route('/borrar/<int:id>')
def borrar_libro(id):
    # CORREGIDO: Se usa 'usuario_id' sin la 's' extra para que coincida con la sesión
    if 'usuario_id' not in session:
        return redirect('/')
    
    libro = Libro.get_one({'id': id})
    
    # Validar que solo el creador pueda borrar
    if libro and libro.usuario_id == session['usuario_id']:
        Libro.delete({'id': id})
        
    return redirect('/dashboard')




    @app.route('/pedir/<int:id>')
    def pedir_prestado(id):
     if 'usuario_id' not in session:
        return redirect('/')

    data = {
        'usuario_id': session['usuario_id'],
    'libro_id': id
    }
    Libro.pedir_prestado(data)
    return redirect('/dashboard')

    @app.route('/devolver/<int:id>')
    def devolver_libro(id):
     if 'usuario_id' not in session:
        return redirect('/')

    data = {
        'usuario_id': session['usuario_id'],
        'libro_id': id
    }
    Libro.devolver(data)
    return redirect('/dashboard')














