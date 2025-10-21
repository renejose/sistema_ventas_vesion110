class Cliente:
    def __init__(self, dni, nombre, direccion, email):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.email = email

    def mostrar_info(self):
        return f"[Cliente] {self.nombre} (DNI: {self.dni}), Email: {self.email}, Dirección: {self.direccion}"