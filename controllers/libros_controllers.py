<<<<<<< HEAD
from flask import Blueprint, request, jsonify
from services.libros_service import LibrosService
#Importar la sesión de la base de datos
from config.database import get_db_session

libros_bp = Blueprint("libros_bp", __name__)
#Instancia global de servicio
service = LibrosService(get_db_session)

#READ (R): Leer todos los libros
#Método: GET Obtener (solicita datos al servidor ) 

@libros_bp.route("/libros", methods=["GET"])
def get_libros():
    libros = service.listar_libros()
    return jsonify([{"id": l.id, "name": l.name} for l in libros]), 200 #JsoniFy convierte el diccionario de libros en una respuesta JSON
=======
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from flask import Blueprint, request, jsonify
from services.libros_service import libroService
from flask_jwt_extended import jwt_required
libro_bp =Blueprint('libro_bp',__name__)

# Importar la sesión de la base de datos desde config/database.py
from config.database import get_db_session

# Instancia global de servicio (en producción usar contexto de app o request)
service = libroService(get_db_session())

libro_bp =Blueprint('libro_bp',__name__)


@libro_bp.route('/libros', methods=['GET'])
@jwt_required()
def get_libros():
	logger.info("Consulta de todas las libros")
	libros = service.listar_libros()
	return jsonify([{'id': b.id, 'name': b.name} for b in libros]), 200, {'Content-Type': 'application/json; charset=utf-8'}

>>>>>>> dev


<<<<<<< HEAD
@libros_bp.route("/libros/<int:id>", methods=["GET"]) #Variable dinámica que indica que la parte <...> es una variable
def obtener_libro_por_ID(libro_id):
    libro = service.obtener_libro(libro_id)
    if libro:
        return jsonify({"id": libro.id, "name": libro.name}), 200 
    return jsonify({"error": "Libro no encontrado"}), 404 
=======
@libro_bp.route('/libros/<int:libro_id>', methods=['GET'])
def get_libro(libro_id):
	libro = service.obtener_libro(libro_id)
	if libro:
		logger.info(f"Consulta de libro por ID: {libro_id}")
		return jsonify({'id': libro.id, 'name': libro.name}), 200, {'Content-Type': 'application/json; charset=utf-8'}
	logger.warning(f"libro no encontrada: {libro_id}")
	return jsonify({'error': 'libro no encontrada'}), 404, {'Content-Type': 'application/json; charset=utf-8'}

>>>>>>> dev


<<<<<<< HEAD
@libros_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "El nombre es obligatorio"}), 400 
    libro = service.crear_libro(name)
    return jsonify({"id": libro.id, "name": libro.name}), 201 
=======
@libro_bp.route('/libros', methods=['POST'])
def create_libro():
	data = request.get_json()
	name = data.get('name')
	if not name:
		logger.warning("Intento de crear libro sin nombre")
		return jsonify({'error': 'El nombre es obligatorio'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
	libro = service.crear_libro(name)
	logger.info(f"libro creado: {name}")
	return jsonify({'id': libro.id, 'name': libro.name}), 201, {'Content-Type': 'application/json; charset=utf-8'}
>>>>>>> dev


<<<<<<< HEAD
@libros_bp.route("/libros/<int:id>", methods=["PUT"])
def actualizar_libro(libro_id):
    data = request.get_json()
    name = data.get("name")
    libro = service.actualizar_libro(libro_id, name)
=======

@libro_bp.route('/libros/<int:libro_id>', methods=['PUT'])
def update_libro(libro_id):
	data = request.get_json()
	name = data.get('name')
	libro = service.actualizar_libro(libro_id, name)
	if libro:
		logger.info(f"libro actualizado: {libro_id}")
		return jsonify({'id': libro.id, 'name': libro.name}), 200, {'Content-Type': 'application/json; charset=utf-8'}
	logger.warning(f"libro no encontrado para actualizar: {libro_id}")
	return jsonify({'error': 'libro no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}
>>>>>>> dev



<<<<<<< HEAD
@libros_bp.route("/libros/<int:id>", methods=["DELETE"])
def eliminar_libro(libro_id):
    libro = service.eliminar_libro(libro_id)
    if libro:
        return jsonify({"message": "Libro eliminado"}), 200
    return jsonify({"error": "Libro no encontrado"}), 404
=======
@libro_bp.route('/libros/<int:libro_id>', methods=['DELETE'])
def delete_libro(libro_id):
	libro = service.eliminar_libro(libro_id)
	if libro:
		logger.info(f"libro eliminada: {libro_id}")
		return jsonify({'message': 'libro eliminado'}), 200, {'Content-Type': 'application/json; charset=utf-8'}
	logger.warning(f"libro no encontrado para eliminar: {libro_id}")
	return jsonify({'error': 'libro no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}
>>>>>>> dev
