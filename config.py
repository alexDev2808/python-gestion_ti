from dotenv import load_dotenv
import os
# Configuracion global de la app

load_dotenv()

DB_CONFIG = {
    "driver": os.getenv("DB_DRIVER", "SQL Server"),
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_DATABASE"),
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "trusted_connection": os.getenv("DB_TRUSTED_CONNECTION", "no"),
}

APP_TITLE = os.getenv("APP_TITLE", "Gestión Personal")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")