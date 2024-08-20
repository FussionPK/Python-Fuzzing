import requests
import sys

def loops():

    for word in sys.stdin:
        res = requests.get(url="Put your IP here..")
        if res.status_code == 404:
            loops()
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)
loops()
