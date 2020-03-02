# importing the requests library
import requests


def GET(url, params):

    # sending get request and saving the response as response object
    r = requests.get(url=url, params=params)
    return r.json()
