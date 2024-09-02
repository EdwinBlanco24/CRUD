import pymysql.cursors

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="pythoncrud",
    cursorclass=pymysql.cursors.DictCursor
)
'''
cursor = connection.cursor()
sql = "INSERT INTO user (nombre, apellido, telefono, email) VALUES('Elkin', 'Arrieta', '3226664433', 'earrieta@gmail.com')"
cursor.execute(sql)
connection.commit()'''

from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route("/")
def root():
    return "Edwin Blanco"

#Creación de usuario atravez del método "post"
@app.route("/usuario", methods=["POST"])
def crear():
    connection = pymysql.connect()

    with connection.cursor() as read:
        sql = "INSERT INTO user (nombre, apellido, telefono, email) VALUES('Elkin', 'Arrieta', '3226664433', 'earrieta@gmail.com')"
        read.execute(sql)

        result = read.fetchall()
        return jsonify({
            'data': result
        }),200

#Obtención de un usuario por medio del "id"
@app.route("/usuario/<int:id>", methods=["GET"])
def read(id):
    connection = pymysql.connect()

    with connection.cursor() as read:
        sql = "SELECT * FROM user WHERE id=%s"
        read.execute(sql, (id))

        result = read.fetchall()
        return jsonify({
            'data': result
        }),200

#Actualizacion de datos de un usuario por medio del "id"    
@app.route("/usuario/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    telefono = data.get("telefono")
    email = data.get("email")

    connection = pymysql.connect()

    with connection.cursor() as update:
        sql = "SET id=, nombre, apellido, telefono, email FROM user"
        update.execute(sql)

        result = update.fetchall()
        return jsonify({
            "data": result
        }),201
    
#Eliminacion de un usuario por medio del "id"
@app.route("/usuario/<int:id>", methods=["DELETE"])
def delete(id):
    connection = pymysql.connect()

    with connection.cursor() as borrar:
        sql = "DELETE * FROM user WHERE id=%s"
        borrar.execute(sql, (id))

        result = update.fetchall()
        return jsonify({
            "data": result
        }),200

if __name__ == "__main__":
    app.run(debug=True)