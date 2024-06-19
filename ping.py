import requests
import time

url = 'https://save-restricted-content-bot-repo-372y.onrender.com/'

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"lmao online: {response.status_code}")
        else:
            print(f"Bakchodi level 1: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"bkchodi level 2 {e}")
    time.sleep(60)
