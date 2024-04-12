from api_key import api_token
import pandas as pd
import requests
import json

def writefile(filename, content):
    file = open(filename, "w")
    file.writelines(str(content))
    file.close()

if __name__=='__main__':
    headers = {
        'Content-Type' : 'app/json',
         'token' : api_token
    }
    base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=ST&limit=1000&offset="
    for i in range(1, 39):
        url = f'{base_url}{i*1000}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.content
            response_dict = json.loads(content)
            output = json.dumps(response_dict, indent=4)
            writefile(f'JSONfiles/locations_{i}.json', output)
        else:
            print(f"Sorry, this call failed. Response code {response.status_code}")
            print(f"URL: {base_url}")

    print("success")
