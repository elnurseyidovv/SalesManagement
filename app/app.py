from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json

app = Flask(__name__)

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'salesDB'
    }


def favorite_colors() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/addCategory', methods=['POST'])
def add_category():
    data = request.get_json()

    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO CATEGORY (Name) VALUES (' + data.name + ');')
        cursor.close()
        connection.close()
    except Exception as error:
        print(error)
        return {'message': 'DB error'}

    return {'message': 'Success'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')