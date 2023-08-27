from flask import Flask
from firebase_admin import db, credentials, initialize_app
import json

app = Flask(__name__)
# Create this using firebase service account
cred = credentials.Certificate('firebase_key.json')
default_app = initialize_app(cred)
database = db.reference(path='/Prototype/Ipone',
                        url='https://ipond1-default-rtdb.asia-southeast1.firebasedatabase.app')  # Not tested


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
    ph = 'data ph'  # Data kumpulan 7 hari
    temperature = 'data temperature'  # Data kumpulan 7 hari
    turbidity = 'data turbidity'  # Data kumpulan 7 hari
    prediction = 'data prediction'  # Data kumpulan 7 hari

    """ Alternatif
    ph = [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
    temperature = [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
    turbidity = [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
    prediction = [senin, selasa, rabu, kamis, jumat, sabtu, minggu]
    overall_prediction = 'hasil kesimpulan machine learning perminggu' # Optional

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction, 'overall':  overall_prediction}
    """

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction}
    return data


@app.get('/monthly')
def monthly():
    ph = 'data ph'  # Data kumpulan 1 bulan
    temperature = 'data temperature'  # Data kumpulan 1 bulan
    turbidity = 'data turbidity'  # Data kumpulan 1 bulan
    prediction = 'data prediction'  # Data kumpulan 1 bulan

    """ Alternatif
    ph = [week1, week2, week3, week4]
    temperature = [week1, week2, week3, week4]
    turbidity = [week1, week2, week3, week4]
    prediction = [week1, week2, week3, week4]
    overall_prediction = 'hasil kesimpulan machine learning perbulan' # Optional

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction, 'overall':  overall_prediction}
    """

    data = {'ph': ph, 'temperature': temperature, 'turbidity': turbidity,
            'predict': prediction}
    return data
