
from cliente import Cliente
from producto import Producto
from pedido import Pedido
def main():
    # Crear clientes
    cliente1 = Cliente("12345678", "Juan Pérez", "Av. Principal 123")
    cliente2 = Cliente("87654321", "María López", "Calle Secundaria 45")
    clientes.extend([cliente1, cliente2])
    
    # Buscar cliente
    buscar_cliente("María López")
    buscar_cliente("Luis López")
    
    # Crear productos
    prod1 = Producto("P001", "Laptop", 3500, 5)
    prod2 = Producto("P002", "Mouse", 50, 20)
    prod3 = Producto("P003", "Teclado", 120, 15)

    # Mostrar catálogo
    print("📋 Catálogo de productos:")
    for p in [prod1, prod2, prod3]:
        print(p.mostrar_info())

    # Crear pedidos
    pedido1 = Pedido(cliente1)
    pedido1.agregar_producto(prod1, 1)  # 1 laptop
    pedido1.agregar_producto(prod2, 2)  # 2 mouse

    pedido2 = Pedido(cliente2)
    pedido2.agregar_producto(prod2, 1)  # 1 mouse
    pedido2.agregar_producto(prod3, 1)  # 1 teclado

    # Mostrar pedidos
    pedido1.mostrar_info()
    pedido2.mostrar_info()

    # Mostrar stock actualizado
    print("\n📦 Stock actualizado:")
    for p in [prod1, prod2, prod3]:
        print(p.mostrar_info())

if __name__ == "__main__":
    main()