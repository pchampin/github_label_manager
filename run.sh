#!/bin/bash
export PYTHONPATH="$(dirname "$0")":$PYTHONPATH
exec python -m glm "$@"
