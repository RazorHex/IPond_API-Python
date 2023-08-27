from flask import Flask
from firebase_admin import db, credentials, initialize_app
import json

app = Flask(__name__)
cred = credentials.Certificate('firebase_key.json')
default_app = initialize_app(cred)
database = db.reference(path='/Prototype/Ipone',
                        url='https://ipond1-default-rtdb.asia-southeast1.firebasedatabase.app')


@app.get('/')
def help():
    data = {'endpoints': ['/dailt', '/weekly', '/monthly']}

    return data


@app.get('/daily')
def daily():
    ph = 'data ph'
    temperature = 'data temperature'
    turbidity = 'data turbidity'
    prediction = 'data prediction'

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction}
    return data


@app.get('/weekly')
def weekly():
    ph = 'data ph'
    temperature = 'data temperature'
    turbidity = 'data turbidity'
    prediction = 'data prediction'

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction}
    return data


@app.get('/monthly')
def monthly():
    ph = 'data ph'
    temperature = 'data temperature'
    turbidity = 'data turbidity'
    prediction = 'data prediction'

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction}
    return data
