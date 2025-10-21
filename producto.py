class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError(f"No hay suficiente stock de {self.nombre}")

    def mostrar_info(self):
        return f"[Producto] {self.nombre} (Código: {self.codigo}), Precio: {self.precio}, Stock: {self.stock}"
    
    #Validar que el stock no sea negativo