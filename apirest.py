from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alimentos.db'
db = SQLAlchemy(app)

# Modelo de la tabla de alimentos
class Alimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

def conectar_base_datos():
    with app.app_context():
        db.create_all()

# Ruta para obtener todos los alimentos (frutas y verduras)
@app.route('/alimentos', methods=['GET'])
def obtener_alimentos():
    alimentos = Alimento.query.all()
    alimentos_list = [{"id": alimento.id, "nombre": alimento.nombre, "tipo": alimento.tipo} for alimento in alimentos]
    return jsonify({"alimentos": alimentos_list})

# Ruta para agregar un nuevo alimento (fruta o verdura)
@app.route('/agregar_alimento/<id>/<nombre>/<tipo>', methods=['GET'])
def agregar_alimento_por_url(id,nombre, tipo):
    nuevo_alimento = Alimento(id=id,nombre=nombre, tipo=tipo)
    db.session.add(nuevo_alimento)
    db.session.commit()
    return jsonify({"mensaje": "Alimento agregado correctamente"})

# Ruta para actualizar un alimento por ID
@app.route('/actualizar_alimento/<string:id>/<string:nombre>/<string:tipo>', methods=['GET'])
def actualizar_alimento(id, nombre, tipo):
    alimento = Alimento.query.get(id)
    if alimento:
        alimento.id = id
        alimento.nombre = nombre
        alimento.tipo = tipo
        db.session.commit()
        return jsonify({"mensaje": "Alimento actualizado correctamente"})
    return jsonify({"mensaje": "Alimento no encontrado"}), 404

# Ruta para eliminar un alimento por ID
@app.route('/eliminar_alimento/<string:id>', methods=['GET'])
def eliminar_alimento(id):
    alimento = Alimento.query.get(id)
    if alimento:
        db.session.delete(alimento)
        db.session.commit()
        return jsonify({"mensaje": "Alimento eliminado correctamente"})
    return jsonify({"mensaje": "Alimento no encontrado"}), 404

if __name__ == '__main__':
    conectar_base_datos()
    app.run(host="0.0.0.0",port=4000,debug=True)
