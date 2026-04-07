from dataclasses import dataclass

@dataclass
class Personal:
    id_empleado: str = ""
    id_funcion: int = None
    id_area: int = None
    app: str = ""          # Apellido paterno
    apm: str = ""          # Apellido materno
    nombre: str = ""
    activo: int = 1
    password: str = ""     # campo 'pass' en BD (pass es palabra reservada en Python)
    id_area_res: int = None
    tc: int = None
    mail: str = ""
    id_areat: int = None
    id_area_res2: int = None
    id_area_res3: int = None
    perm_fsm: int = None
    tipo_puesto: int = None

    def nombre_completo(self):
        return f"{self.nombre} {self.app} {self.apm}"