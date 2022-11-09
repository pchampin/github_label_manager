from argparse import Namespace
from glm.common import prepare_headers, prepare_url
import json
import requests
import sys

def run(args: Namespace):
    headers = prepare_headers(args)
    url = prepare_url(args)
    url += f"/{args.label}"
    resp = requests.delete(url, headers=headers)
    resp.raise_for_status()
