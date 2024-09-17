from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Estructuras de datos
catalogo_productos = []  # Array de productos en inventario
pila_perecederos = []  # Pila para productos perecederos
cola_no_perecederos = []  # Cola para productos no perecederos
ordenes_completadas = []  # Lista de órdenes completadas

# Función para agregar productos al inventario
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    tipo = request.form['tipo']

    if tipo == 'perecedero':
        pila_perecederos.append(nombre)
    else:
        cola_no_perecederos.append(nombre)
    
    catalogo_productos.append(nombre)
    return redirect(url_for('index'))

# Función para despachar productos
@app.route('/despachar')
def despachar_producto():
    if pila_perecederos:
        producto = pila_perecederos.pop()  # Despachar de la pila de perecederos
    elif cola_no_perecederos:
        producto = cola_no_perecederos.pop(0)  # Despachar de la cola de no perecederos
    else:
        producto = None

    if producto:
        ordenes_completadas.append(producto)
    return redirect(url_for('index'))

# Página principal que muestra el inventario y las órdenes
@app.route('/')
def index():
    return render_template('index.html', 
                           catalogo=catalogo_productos, 
                           pila=pila_perecederos, 
                           cola=cola_no_perecederos, 
                           ordenes=ordenes_completadas)

if __name__ == '__main__':
    app.run(debug=True)
