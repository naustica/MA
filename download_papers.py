import requests
import urllib
import json
import os

api_key = os.environ['s2_key']

release = requests.get('http://api.semanticscholar.org/datasets/v1/release/2023-05-23').json()

papers = requests.get('http://api.semanticscholar.org/datasets/v1/release/2023-05-23/dataset/papers',
                      headers={'x-api-key': api_key}).json()

for n, file in enumerate(papers['files'], start=1):
    urllib.request.urlretrieve(file, 'papers-part{}.jsonl.gz'.format(n))
