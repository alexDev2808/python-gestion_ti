import sys  
import os  
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pyodbc
from config import DB_CONFIG

def get_connection():
    """Establece y retorna una conexión a SQL Server."""
    try:
        if DB_CONFIG["trusted_connection"] == "yes":
            conn_str = (
                f"DRIVER={{{DB_CONFIG['driver']}}};"
                f"SERVER={DB_CONFIG['server']};"
                f"DATABASE={DB_CONFIG['database']};"
                f"Trusted_Connection=yes;"
            )
        else:
            conn_str = (  
                f"DRIVER={{{DB_CONFIG['driver']}}};"  
                f"SERVER={DB_CONFIG['server']};"  
                f"DATABASE={DB_CONFIG['database']};"  
                f"UID={DB_CONFIG['username']};"  
                f"PWD={DB_CONFIG['password']};"  
            )
        
        conn = pyodbc.connect(conn_str)
        return conn

    except pyodbc.Error as e:
        print(f"[ERROR] No se pudo conectar a la base de datos: {e}")  
        return None


def test_connection():  
    """Prueba la conexión a la base de datos."""  
    conn = get_connection()  
    if conn:  
        print("[OK] Conexión exitosa a SQL Server.")  
        conn.close()  
    else:  
        print("[FAIL] Falló la conexión.")  
  
  
if __name__ == "__main__":  
    test_connection()