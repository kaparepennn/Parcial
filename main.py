from flask import Flask
from controllers.libros_controllers import libros_bp
from controllers.users_controllers import user_bp
from config.jwt import * #Importar jwt de la carpeta config

app = Flask(__name__)

#Agregar el jwt de la carpeta config
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES #Configurar el tiempo en el que se debe volver a autenticar a la aplicación
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME 
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

# Registrar el blueprint de bandas. Realizar un registro del controlador dentro del main para poder crear un nuevo registro
app.register_blueprint(libros_bp)
app.register_blueprint(user_bp)


if __name__ == "__main__":
    app.run(debug=True)