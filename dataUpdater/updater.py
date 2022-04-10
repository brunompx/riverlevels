from datetime import datetime
import json
import os
import sys
from levels.models import Level
import warnings
from dataUpdater import api_client


def update_data():
    if Level.objects.exists():
        print("-----------DELETE--------------")
        Level.objects.all().delete()

    json_content = read_forecast_models()
    data = json_content['data']
    for i in data:
        response = api_client.call_api(i['seriesId'], i['siteCode'], i['calId'])
        resp_json = response.json()

        resp_header = resp_json['responseHeader']
        resp_data = resp_json['data']
        
        #Keep only one value per date while removing all hourly values and using a Set.
        clean_data = {}
        for o in resp_data:
            clean_data[o['timeend'][:-9]] = o['valor']
        
        print(clean_data)

        for k, v in clean_data.items():
            level = build_level(resp_header, k, v)
            level.save()
            # print('----------: ' + k)
            # ddddddd = convert_date(k)
            # print(ddddddd.strftime("%Y-%m-%d"))


def convert_date(strD: str) -> datetime:
    return datetime.strptime(str(strD), "%Y-%m-%d")

def read_forecast_models():
    with open(os.path.join(sys.path[0]+'/dataUpdater', 'models.json'), 'r') as f:
        return json.load(f)

def build_level(header, value_date, value):
    level = Level()
    level.cal_name = header['cal_name']
    level.calid = header['calid']
    level.corid = header['corid']
    level.estacion_id = header['estacion_id']
    level.model_name = header['model_name']
    level.label = str(header['corid']) + "-" + header['cal_name']
    level.forecast_date = convert_date(header['forecastdate'][:-9])
    level.value_date = convert_date(value_date)
    level.value = value
    return level


def main():
    if not sys.warnoptions:
        warnings.simplefilter("ignore")
    update_data()

if __name__ == '__main__':
    main()