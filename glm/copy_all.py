from argparse import Namespace
from glm.common import prepare_headers, prepare_url
from glm.list import get_list
import json
import requests
import sys

def run(args: Namespace):
    headers = prepare_headers(args)
    url_src = prepare_url(args, repo_attr='src')
    url_dest = prepare_url(args, repo_attr='dest')

    if args.replace:
        for label in get_list(url_dest, headers):
            url_del = url_dest + f"/{label['name']}"
            print(f"deleting {label['name']} from {args.dest}")
            requests.delete(url_del, headers=headers).raise_for_status()
        dest_labels = set()
    else:
        dest_labels = { label['name'] for label in get_list(url_dest, headers) }

    for label in get_list(url_src, headers):
        if label['name'] not in dest_labels:
            new_label = {
                'name': label['name'],
                'color': label['color'],
                'description': label['description'],
            }
            print(f"adding {label['name']} to {args.dest}")
            requests.post(url_dest, json=new_label, headers=headers).raise_for_status()
        else:
            print(f"skipping {label['name']} (already present in {args.dest})")
