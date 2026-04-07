from database.connection import get_connection

def execute_query(query: str, params: tuple = ()):
    """Ejecuta una consulta SELECT y retorna los resultados."""
    conn = get_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except Exception as e:
        print(f"[ERROR] execute_query: {e}")
        return []
    finally:
        conn.close()


def execute_non_query(query: str, params: tuple = ()):
    """Ejecuta INSERT, UPDATE o DELETE. Retorna True si fue exitoso."""
    conn = get_connection()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return True
    except Exception as e:
        print(f"[ERROR] execute_non_query: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()