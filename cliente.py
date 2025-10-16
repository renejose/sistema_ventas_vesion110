class Cliente:
    def __init__(self, dni, nombre, direccion):
        if not (isinstance(dni, str) and dni.isdigit() and len(dni) == 8):
            raise ValueError("El DNI debe contener exactamente 8 dígitos numéricos.")
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion

    def mostrar_info(self):
        return f"[Cliente] {self.nombre} (DNI: {self.dni}), Dirección: {self.direccion}"