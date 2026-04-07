from database.queries import execute_query, execute_non_query
from models.Personal import Personal


def get_all_personal():
    """Obtiene todos los empleados."""
    query = "SELECT * FROM Personal"
    rows = execute_query(query)
    return [_row_to_personal(row) for row in rows]


def get_personal_by_id(id_empleado: str):
    """Obtiene un empleado por su ID."""
    query = "SELECT * FROM Personal WHERE id_empleado = ?"
    rows = execute_query(query, (id_empleado,))
    return _row_to_personal(rows[0]) if rows else None


def get_personal_activo():
    """Obtiene solo empleados activos."""
    query = "SELECT * FROM Personal WHERE activo = 1"
    rows = execute_query(query)
    return [_row_to_personal(row) for row in rows]


def insert_personal(p: Personal):
    """Inserta un nuevo empleado."""
    query = """
        INSERT INTO Personal 
        (id_empleado, id_funcion, id_area, app, apm, nombre, activo, 
         [pass], id_area_res, tc, mail, id_areat, id_area_res2, 
         id_area_res3, perm_fsm, tipoPuesto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (
        p.id_empleado, p.id_funcion, p.id_area, p.app, p.apm,
        p.nombre, p.activo, p.password, p.id_area_res, p.tc,
        p.mail, p.id_areat, p.id_area_res2, p.id_area_res3,
        p.perm_fsm, p.tipo_puesto
    )
    return execute_non_query(query, params)


def update_personal(p: Personal):
    """Actualiza los datos de un empleado."""
    query = """
        UPDATE Personal SET
            id_funcion = ?, id_area = ?, app = ?, apm = ?, nombre = ?,
            activo = ?, [pass] = ?, id_area_res = ?, tc = ?, mail = ?,
            id_areat = ?, id_area_res2 = ?, id_area_res3 = ?,
            perm_fsm = ?, tipoPuesto = ?
        WHERE id_empleado = ?
    """
    params = (
        p.id_funcion, p.id_area, p.app, p.apm, p.nombre,
        p.activo, p.password, p.id_area_res, p.tc, p.mail,
        p.id_areat, p.id_area_res2, p.id_area_res3,
        p.perm_fsm, p.tipo_puesto, p.id_empleado
    )
    return execute_non_query(query, params)


def delete_personal(id_empleado: str):
    """Elimina un empleado por su ID."""
    query = "DELETE FROM Personal WHERE id_empleado = ?"
    return execute_non_query(query, (id_empleado,))


def login(id_empleado: str, password: str):
    """Valida credenciales de acceso."""
    query = "SELECT * FROM Personal WHERE id_empleado = ? AND [pass] = ? AND activo = 1"
    rows = execute_query(query, (id_empleado, password))
    return _row_to_personal(rows[0]) if rows else None


def _row_to_personal(row) -> Personal:
    """Convierte una fila de BD en un objeto Personal."""
    return Personal(
        id_empleado=row[0],
        id_funcion=row[1],
        id_area=row[2],
        app=row[3],
        apm=row[4],
        nombre=row[5],
        activo=row[6],
        password=row[7],
        id_area_res=row[8],
        tc=row[9],
        mail=row[10],
        id_areat=row[11],
        id_area_res2=row[12],
        id_area_res3=row[13],
        perm_fsm=row[14],
        tipo_puesto=row[15],
    )