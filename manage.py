#!/usr/bin/env python3

import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.settings import get_config
from app.app import create_app
from app.extensions import db

def find_assets():
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in os.scandir(directory):
            if entry.is_file():
                yield entry.path

config = get_config(os.getenv('FLASK_ENV'))

app = create_app(config)
migrate = Migrate(app, db)


server = Server(host='0.0.0.0', extra_files=find_assets(), threaded=True)

manager = Manager(app)
manager.add_command('run', server)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
