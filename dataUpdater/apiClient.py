import requests
from datetime import datetime, timedelta
import json
import os
import sys

now = datetime.now()
timeStart = (now + timedelta(-10)).strftime("%Y-%m-%d")
timeEnd = (now + timedelta(40)).strftime("%Y-%m-%d")
varId = '2'
format ='json'
all ='false'
base_api = 'https://alerta.ina.gob.ar/pub/datos/datosProno'

def call_api(param_str):
    return requests.get(base_api + param_str)

def build_params(seriesId, siteCode, calId):
    parameters = {'timeStart':timeStart,
    'timeEnd':timeEnd,
    'seriesId':seriesId,
    'calId':calId,
    'all':all,
    'siteCode':siteCode,
    'varId':varId,
    'format':format}
    param_str = ''
    for k, v in parameters.items():
        param_str += '&'
        param_str += k
        param_str += '='
        param_str += v
    return param_str

def read_models():
    with open(os.path.join(sys.path[0] + '\dataUpdater', 'models.json'), 'r') as f:
        return json.load(f)

def update_data():
    json_content = read_models()
    data = json_content['data']

    for i in data:
        seriesId = i['seriesId']
        siteCode = i['siteCode']
        calId = i['calId']
        
        params = build_params(seriesId, siteCode, calId)
        response = call_api(params)
        resp_json = response.json()

        calid = resp_json['responseHeader']['calid']
        corid = resp_json['responseHeader']['corid']
        estacion_id = resp_json['responseHeader']['estacion_id']
        model_name = resp_json['responseHeader']['model_name']
        cal_name = resp_json['responseHeader']['cal_name']
        label = str(corid) + "-" + cal_name
        forecast_date = resp_json['responseHeader']['forecastdate'][:-9]
        create_date = now
        #value_date = models.DateField
        #value = models.DecimalField(max_digits=5, decimal_places=4)

        resp_data = resp_json['data']
        clean_data = {}
        for o in resp_data:
            clean_data[o['timeend'][:-9]] = o['valor']
        
        print(clean_data)

        #save to file
        