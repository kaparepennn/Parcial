from flask import Flask
from controllers.libros_controllers import libros_bp

app = Flask(__name__)

# Registrar el blueprint de bandas
app.register_blueprint(libros_bp)

if __name__ == "__main__":
    app.run(debug=True)