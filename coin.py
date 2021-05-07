import requests
import json
import pprint
import random
import re
import pickle
r = requests.get('https://store.steampowered.com/app/1238840/Battlefield_1/')
w = re.findall(r'''¥ [0-9]{2,3}(?=\s{5,})''',r.text,re.DOTALL)
print(w[0])