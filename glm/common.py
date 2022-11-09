from argparse import Namespace
import re

RE_REPO_NAME = re.compile("^[a-zA-Z0-9_\-]+/[a-zA-Z0-9_\-]+$")
RE_LABEL_NAME = re.compile("^[a-zA-Z0-9_\-:]+$")
RE_COLOR_CODE = re.compile("^[a-fA-F0-9]{6}$")

"""
Return arg if it is a valid repo name,
otherwise raise a ValueError
"""
def repo_name(arg: str) -> str:
    if RE_REPO_NAME.match(arg):
        return arg
    else:
        raise ValueError(f"Invalid repo name {arg!r}")

"""
Return arg if it is a valid label name,
otherwise raise a ValueError
"""
def label_name(arg: str) -> str:
    if RE_LABEL_NAME.match(arg):
        return arg
    else:
        raise ValueError(f"Invalid label name {arg!r}")

"""
Return arg if it is a valid label name,
otherwise raise a ValueError
"""
def color_code(arg: str) -> str:
    if RE_COLOR_CODE.match(arg):
        return arg
    else:
        raise ValueError(f"Invalid color code {arg!r}")

def prepare_headers(args: Namespace):
    headers = {
        'accept': 'application/vnd.github+json'
    }
    if args.token:
        headers['authorization'] = f'Bearer {args.token}'
    return headers

def prepare_url(args: Namespace, *, repo_attr='repo'):
    repo = getattr(args, repo_attr)
    return f"https://api.github.com/repos/{repo}/labels"
