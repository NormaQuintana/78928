from flask import Flask, render_template
from flask import request
from flask import Response
from flask import redirect, url_for
from producto import Producto

app = Flask(__name__)

productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/')
def index():
    #productos = [Producto("computadora", 200), Producto("impresora", 50)]
    return render_template('Productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto, precio):
    #recuperar producto
    print(producto)
    return render_template('EditarProducto.html', producto = producto, precio = precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    #guardar producto
    n=request.form.get('nombre')
    p=request.form.get('precio')
    print(n, p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n, p)
        i += 1
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<producto>')
def eliminar(producto):
    #eliminar producto
    i = 0
    for e in productos:
        if e.nombre == producto:
            productos.pop(i)
        i += 1
    return Response("eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    #crear producto
    n = request.form.get('nombre')
    p = request.form.get('precio')
    productos.append(Producto(n, p))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)