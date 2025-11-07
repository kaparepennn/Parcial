import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env si existe
load_dotenv()

# Clave secreta para JWT (usa JWT_SECRET_KEY en .env). Si no está, intenta SECRET_KEY
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or os.getenv('SECRET_KEY')

# Ubicación del token y expiración (segundos)
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hora

JWT_HEADER_NAME = "Authorization"
JWT_HEADER_TYPE = "Bearer"