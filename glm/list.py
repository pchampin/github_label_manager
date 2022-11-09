from argparse import Namespace
from glm.common import prepare_headers, prepare_url
import json
import requests
import sys

def run(args: Namespace):
    headers = prepare_headers(args)
    url = prepare_url(args)
    data = get_list(url, headers)
    json.dump(data, sys.stdout, indent="  ")

def get_list(url, headers):
    params = { 'per_page': '100' }
    resp = requests.get(url, params=params, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    while 'next' in resp.links:
        resp = requests.get(resp.links['next']['url'], headers=headers)
        resp.raise_for_status()
        data += resp.json()

    return data
