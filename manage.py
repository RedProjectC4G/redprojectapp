#!/usr/bin/env python3

import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
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
migrate = Migrate(app, db)


server = Server(host='0.0.0.0', extra_files=find_assets(), threaded=True)

manager = Manager(app)
manager.add_command('run', server)


if __name__ == '__main__':
    manager.run()
