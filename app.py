from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
