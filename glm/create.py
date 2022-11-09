from argparse import Namespace
from glm.common import prepare_headers, prepare_url
import json
import requests
import sys

def run(args: Namespace):
    headers = prepare_headers(args)
    url = prepare_url(args)
    body = {
        "name": args.label,
    }
    if args.color:
        body['color'] = args.color
    if args.description:
        body['description'] = args.description
    resp = requests.post(url, json=body, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    json.dump(data, sys.stdout, indent="  ")