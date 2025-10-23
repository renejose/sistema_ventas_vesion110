from detalle_pedido import DetallePedido
<<<<<<< HEAD
=======

>>>>>>> f2fca99833b0057a20b441f47dd9d53c29452342
class Pedido:
    contador = 1  # contador estático de pedidos

    def __init__(self, cliente):
        self.id_pedido = Pedido.contador
        Pedido.contador += 1
        self.cliente = cliente
        self.detalles = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        try:
            producto.actualizar_stock(cantidad)
            detalle = DetallePedido(producto, cantidad)
            self.detalles.append(detalle)
            self.total += detalle.subtotal
        except ValueError as e:
            print(f"⚠️ Error: {e}")

    def mostrar_info(self):
        print(f"\n📦 Pedido N° {self.id_pedido}")
        print(f"Cliente: {self.cliente.nombre}")
        print("Detalles:")
        for d in self.detalles:
            print(f"   - {d.mostrar_info()}")
        print(f"Total a pagar: {self.total}")