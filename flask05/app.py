from flask import Flask, render_template
from flask import request
from flask import Response
from flask import redirect, url_for
import sqlite3
#from producto import Producto

app = Flask(__name__)

#productos = [Producto("computadora", 200), Producto("impresora", 50)]

@app.route('/')
def index():
    #productos = [Producto("computadora", 200), Producto("impresora", 50)]
    con = conexion()
    productos =  con.execute('SELECT * FROM productos').fetchall() #recupera todos los registros
    print(productos)
    con.close()
    return render_template('Productos.html', productos=productos)

#@app.route('/editar/<producto>/<precio>')
@app.route('/editar/<id>')
def editar(id):
    #recuperar producto
    con = conexion()
    producto = con.execute('SELECT * FROM productos WHERE id = ?', (id)).fetchone()
    con.close()
    print(producto)
    return render_template('EditarProducto.html', producto = producto)

@app.route('/guardar', methods=['POST'])
def guardar():
    #guardar producto
    n=request.form.get('nombre')
    p=request.form.get('precio')
    id=request.form.get('id')
    print(n, p)
    con = conexion()
    con.execute('UPDATE productos SET nombre = ?, precio = ? WHERE id = ?', (n, p, id))
    con.commit()
    con.close()
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<id>')
def eliminar(id):
    #eliminar producto
    con = conexion()
    con.execute('DELETE FROM productos WHERE id = ?', (id))
    con.commit()
    con.close()
    return Response("eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    #crear producto
    n = request.form.get('nombre')
    p = request.form.get('precio')
    #productos.append(Producto(n, p))
    con = conexion()
    con.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (n, p))
    con.commit()
    con.close()
    return redirect(url_for('index'))

def conexion():
    con = sqlite3.connect('productos.db')
    #row_facotry:
    #hace que las consultas se vuelvan diccionarios pudiendo
    #seleccionar valores mediante ['nombre_columna']
    con.row_factory = sqlite3.Row
    return con  

def iniciar_db():
    con = conexion()
    #se crea la tabla en caso de que no exista
    con.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    con.commit() #guarda los cambios
    con.close()

if __name__ == '__main__':
    iniciar_db()
    app.run(host='0.0.0.0', debug=True)