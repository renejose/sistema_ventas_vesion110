from flask import Flask, render_template
from cliente import Cliente
from producto import Producto
from pedido import Pedido

app = Flask(__name__)

# Datos de prueba
cliente1 = Cliente("12345678", "Juan Pérez", "Av. Principal 123")
cliente2 = Cliente("87654321", "María López", "Calle Secundaria 45")

prod1 = Producto("P001", "Laptop", 3500, 5)
prod2 = Producto("P002", "Mouse", 50, 20)
prod3 = Producto("P003", "Teclado", 120, 15)

productos = [prod1, prod2, prod3]

@app.route("/")
def inicio():
    return render_template("catalogo.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)
