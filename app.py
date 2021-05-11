from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin1234@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class InventarioModel(db.Model):
    __tablename__ = 'inventario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    precio = db.Column(db.String())
    cantidad = db.Column(db.Integer())

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"<Producto {self.nombre}>"

class VentasModel(db.Model):
    __tablename__ = 'ProductoVentas'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String())
    precio = db.Column(db.String())
    cantidad = db.Column(db.Integer())

    def __init__(self, descripcion, precio, cantidad):
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        return f"<Venta {self.descripcion}>"


@app.route('/')
def hello():
	return {"Bienvenidos": "A todos"}


@app.route('/api/v1/productos', methods=['POST', 'GET'])
def inventario():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_producto = InventarioModel(nombre=data['nombre'], precio=data['precio'], cantidad=data['cantidad'])

            db.session.add(new_producto)
            db.session.commit()

            return {"message": f"producto {new_producto.nombre} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        productos = InventarioModel.query.all()
        results = [
            {
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": producto.cantidad
            } for producto in productos]

        return {"count": len(results), "productos": results, "message": "success"}

@app.route('/api/v1/venta', methods=['POST', 'GET'])
def ventas():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_venta = VentasModel(descripcion=data['descripcion'], precio=data['precio'], cantidad=data['cantidad'])

            db.session.add(new_venta)
            db.session.commit()

            return {"message": f"venta {new_venta.descripcion} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        ventas = VentasModel.query.all()
        results = [
            {
                "descripcion": venta.descripcion,
                "precio": venta.precio,
                "cantidad": venta.cantidad
            } for venta in ventas]

        return {"count": len(results), "ventas": results, "message": "success"}

    
    app.run(debug = True)