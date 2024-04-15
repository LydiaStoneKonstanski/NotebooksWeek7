import sys
import pandas as pd
sys.path.append('DataAcqusitionLab/api_key.py')
from DataAcqusitionLab.api_key import api_token
import requests
import json

def save_json(filepath, json_content):
    with open(filepath, 'w') as outfile:
        json.dump(json_content, outfile)
    print(f'Successfully saved {filepath}')

def api_request():
    headers = {
        'Content-Type' : 'app/json',
         'token' : api_token
    }
    base_url = " https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset="
    print(f"Getting data from: {base_url}")

    data_list = []
    for i in range(0, 2):
        print (f"Iteration {i}")
        url = f'{base_url}{i*1000}'
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            content = response.content
            data = json.loads(content)["results"]
            print(f"This iteration found {len(data)} entries.")
            data_list.extend(data)
        else:
            print(f"Sorry, this call failed. Response code {response.status_code}")
            print(f"URL: {base_url}")

    print (f"Results has {len(data_list)} entries.")
    save_json('Combined.json', data_list)


if __name__=='__main__':
    #api_request()
