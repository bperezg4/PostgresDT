from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/ventas/')
def projects():
    return 'pagina de ventas'

@app.route('/ventas/', methods=['POST']) 
def foo():
    data = request.json
    return jsonify(data)

@app.route('/inventario')
def about():
    return 'pagina de inventarios'

@app.route('/')
def hello():
    return 'Hello, World'
