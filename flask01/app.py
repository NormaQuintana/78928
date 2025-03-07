from flask import Flask 

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'Bienvenido a la pagina de inicio!'

@app.route('/saludar')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/hola')
def hola_html():
    return '<h1 style="color:red";>Hola!</h1> '

@app.route('/adios')
def adios_mundo():
    return 'Adios Mundo!'

@app.route('/json')
def algo():
    return '{"nombre":"John"}'

@app.route('/xml')
def xml():
    return '<?xml version="1.0"?><nombre>John</nombre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)