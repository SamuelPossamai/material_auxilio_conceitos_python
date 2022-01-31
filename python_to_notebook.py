
from pathlib import Path
import copy
import json

template_all = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.6.4"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

template_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": []
}

paths = {}

cwd = Path.cwd()

for path in cwd.rglob('src/**/*.py'):
    dir_paths = paths.setdefault(path.parent.name, [])
    dir_paths.append(path)

dist_path = cwd.joinpath('dist')

dist_path.mkdir(exist_ok=True)

for directory, files in paths.items():
    content = copy.deepcopy(template_all)
    cells = content['cells']
    files.sort()
    for filepath in files:
        cell = copy.deepcopy(template_cell)
        with open(filepath) as file:
            lines = file.readlines()

            start = 0
            for i, line in enumerate(lines):
                if line != '\n':
                    start = i
                    break

            end = 0
            for i, line in enumerate(reversed(lines)):
                if line != '\n':
                    end = -i
                    break

            if end == 0:
                end = None

            lines = lines[start: end]

        cell['source'] = lines
        cells.append(cell)

    with open(dist_path.joinpath(f'{directory}.ipynb'), 'w') as file:
        json.dump(content, file)
