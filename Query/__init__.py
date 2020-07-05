import base64
import logging
from os import environ
import pyodbc
import simplejson as json

import azure.functions as func


conn_str = environ.get('SqlConnectionString', '')

def main(req: func.HttpRequest) -> func.HttpResponse:
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Products where VerCol > ?', base64.b64decode('AAAAAAAAB9M='))
    rows = [{
        'Id': row[0],
        'Name': row[1],
        'Price': row[2],
        'VerCol': base64.b64encode(row[3])
    } for row in cursor]
    return func.HttpResponse(json.dumps(rows))
