# importar la función que devolverá una instancia de una conexión
from aplicacion.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.correo = data['correo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuarios_schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        usuarios = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , apellido , correo , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(correo)s , NOW() , NOW() );"
        #esta sintaxis de %()s es para evitar inyecciones y maltrato de datos. muy importante
        
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuarios_schema').query_db( query, data )