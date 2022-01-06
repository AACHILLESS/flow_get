import requests
from requests.auth import HTTPBasicAuth
import time
from bs4 import BeautifulSoup

url="https://lichen.mutualism.zone/user"

res=requests.get(url)

print(res)
