from argparse import ArgumentParser
from glm.common import repo_name, label_name, color_code
import sys

parser = ArgumentParser("glm")
subparsers = parser.add_subparsers(dest="subcommand", required=True)

list = subparsers.add_parser("list")
list.add_argument("repo", type=repo_name)
list.add_argument("-t", "--token", help="github authorization token (only required for private repos)")

list = subparsers.add_parser("create")
list.add_argument("repo", type=repo_name)
list.add_argument("label", type=label_name)
list.add_argument("-c", "--color", type=color_code)
list.add_argument("-d", "--description")
list.add_argument("-t", "--token", help="github authorization token", required=True)

list = subparsers.add_parser("delete")
list.add_argument("repo", type=repo_name)
list.add_argument("label", type=label_name)
list.add_argument("-t", "--token", help="github authorization token", required=True)

list = subparsers.add_parser("copy-all")
list.add_argument("src", type=repo_name, help="source repo")
list.add_argument("dest", type=repo_name, help="desrination repo")
list.add_argument("-r", "--replace", help="replace existing labels", action='store_true')
list.add_argument("-t", "--token", help="github authorization token", required=True)

args = parser.parse_args()
match args.subcommand:
    case 'list':
        import glm.list
        glm.list.run(args)
    case 'create':
        import glm.create
        glm.create.run(args)
    case 'delete':
        import glm.delete
        glm.delete.run(args)
    case 'copy-all':
        import glm.copy_all
        glm.copy_all.run(args)
