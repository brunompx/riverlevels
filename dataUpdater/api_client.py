import requests
from datetime import datetime, timedelta

now = datetime.now()
timeStart = (now + timedelta(-10)).strftime("%Y-%m-%d")
timeEnd = (now + timedelta(40)).strftime("%Y-%m-%d")
varId = '2'
format ='json'
all ='false'
base_api = 'https://alerta.ina.gob.ar/pub/datos/datosProno'

def call_api(seriesId, siteCode, calId):
    return requests.get(base_api + build_params(seriesId, siteCode, calId))

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



