class DetallePedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = self.producto.precio * cantidad

    def mostrar_info(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.subtotal}"