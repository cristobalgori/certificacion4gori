#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Libro:

    #metodo constructor
    def __init__(self, data):
        self.id = data.get('id')
        self.titulo = data.get('titulo')
        self.autor = data.get('autor')
        self.sinopsis = data.get('sinopsis')

        self.created_at = data.get('created_at')
        self.usuario_id = data.get('usuarios_id', data.get('usuario_id'))
        self.updated_at = data.get('updated_at')

    #para guardar 1 registro
    @classmethod
    def save(cls, data):
        query = "INSERT INTO libros (titulo, autor, sinopsis, created_at, updated_at, usuarios_id) VALUES (%(titulo)s, %(autor)s, %(sinopsis)s, NOW(), NOW(), %(usuario_id)s)"

        return connectToMySQL('certificacion4').query_db(query, data)

    #metodo para ver todos los registros
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM libros"

        libros_en_db = connectToMySQL('certificacion4').query_db(query)
    
        libros = []
        for libro in libros_en_db:
            libros.append(cls(libro))

        return libros


    #metodo para ver 1 registro
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM libros WHERE id = %(id)s;"
        libro_en_db = connectToMySQL('certificacion4').query_db(query,datos)

        return cls(libro_en_db[0])

    #metodo para editar registro
    @classmethod
    def update(cls, datos):
        query = "UPDATE libros SET titulo=%(titulo)s, autor=%(autor)s, sinopsis=%(sinopsis)s, updated_at=NOW(), usuarios_id=%(usuario_id)s WHERE id = %(id)s;"

        return connectToMySQL('certificacion4').query_db(query, datos)
    

    #metodo para eliminar registro
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM libros WHERE id = %(id)s;"
        return connectToMySQL('certificacion4').query_db(query, datos)

    #es staticmethod porque no necesita la clase ni una instancia, solo el formulario
    @staticmethod
    def validar_libro(formulario):
        es_valido = True

        if len(formulario['titulo']) < 2:
            flash("El título debe tener al menos 2 caracteres", "crear_libro")
            es_valido = False

        if len(formulario['autor']) < 2:
            flash("El autor debe tener al menos 2 caracteres", "crear_libro")
            es_valido = False

        if len(formulario['sinopsis']) < 10:
            flash("La sinopsis debe tener al menos 10 caracteres", "crear_libro")
            es_valido = False

        return es_valido        
    @classmethod
        
    def pedir_prestado(cls, data):

        query = "INSERT INTO usuarios_libros (usuario_id, libro_id) VALUES (%(usuario_id)s, %(libro_id)s);"
        return connectToMySQL('certificacion4').query_db(query, data)

@classmethod
def devolver(cls, data):
    query = "DELETE FROM usuarios_libros WHERE usuario_id = %(usuario_id)s AND libro_id = %(libro_id)s;"
    return connectToMySQL('certificacion4').query_db(query, data)
        