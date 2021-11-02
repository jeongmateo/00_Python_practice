import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/"

res = requests.get(url)
print(res.raise_for_status())