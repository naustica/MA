import requests
import urllib
import json
import os

api_key = os.environ['s2_key']

release = requests.get('http://api.semanticscholar.org/datasets/v1/release/2023-05-23').json()

venues = requests.get('http://api.semanticscholar.org/datasets/v1/release/2023-05-23/dataset/publication-venues',
                      headers={'x-api-key': api_key}).json()

for n, file in enumerate(venues['files'], start=1):
    urllib.request.urlretrieve(file, 'venues-part{}.jsonl.gz'.format(n))
