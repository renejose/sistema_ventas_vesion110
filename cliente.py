class Cliente:
    def __init__(self, dni, nombre, direccion):
        
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion

    def mostrar_info(self):
        return f"[Cliente] {self.nombre} (DNI: {self.dni}), Dirección: {self.direccion}"

    def mostrar_lista(clientes):
        print("\n Lista de clientes:")
        for c in clientes:
            print(c.mostrar_info())