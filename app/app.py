from typing import List, Dict
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'salesDB'
}


@app.route('/addCategory', methods=['POST'])
def add_category():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CATEGORY (Name) VALUES ('" + data.name + "')")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/addClient', methods=['POST'])
def add_client():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CLIENT (Name, Phone) VALUES ('" + data.name + "', '" + data.phone + "')")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/addProduct', methods=['POST'])
def add_product():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO PRODUCT (CategoryId, Name, Description, Quantity, Price) " +
                       "VALUES (" + data.categoryId + ", '" + data.name + "', '" + data.description + "', " + data.quantity + ", " + data.price + ")")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/addInterest', methods=['POST'])
def add_interest():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO INTEREST (ClientId, ProductId, Active, InterestDate) " +
                       "VALUES (" + data.clientId + ", " + data.productId + ", " + data.active + ", " + data.interestDate + ")")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/addPurchase', methods=['POST'])
def add_purchase():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO INTEREST (ClientId, ProductId, Price, PurchaseDate) " +
                       "VALUES (" + data.clientId + ", " + data.productId + ", " + data.price + ", " + data.purchaseDate + ")")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/updateCategory', methods=['POST'])
def update_category():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/updateClient', methods=['POST'])
def update_client():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/updateProduct', methods=['POST'])
def update_product():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/updateInterest', methods=['POST'])
def update_interest():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/updatePurchase', methods=['POST'])
def update_purchase():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/getCategory', methods=['GET'])
def get_category():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("select * from CATEGORY")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/getClient', methods=['GET'])
def get_client():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("select * from CLIENT")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/getProduct', methods=['GET'])
def get_product():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("select * from PRODUCT")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/getInterest', methods=['GET'])
def get_interest():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("select * from INTEREST")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


@app.route('/getPurchase', methods=['GET'])
def get_purchase():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute("select * from PURCHASE")
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
