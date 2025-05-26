import json
import requests

def check_license(user_key, license_file='config.json'):
    try:
        response = requests.get(f"https://your-license-server.com/validate?key={user_key}")
        if response.status_code == 200 and response.json().get("status") == "valid":
            return True
    except:
        pass

    with open(license_file, 'r') as file:
        data = json.load(file)
        return user_key in data['valid_keys']
