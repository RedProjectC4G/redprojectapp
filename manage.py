#!/usr/bin/env python3

import os

from flask import url_for
from flask_script import Manager, Server
from redproject.settings import get_config
from redproject.app import create_app

"""3.4 is crippled"""
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


def find_assets():
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in scandir(directory):
            if entry.is_file():
                yield entry.path

config = get_config(os.getenv('FLASK_ENV'))

app = create_app(config)


server = Server(host='0.0.0.0', extra_files=find_assets(), threaded=True)

manager = Manager(app)
manager.add_command('run', server)

@manager.command
def list_routes():
    from urllib.parse import unquote
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

@manager.command
def list_paths():
    print('static_folder: {}'.format(app.static_folder))

if __name__ == '__main__':
    manager.run()
