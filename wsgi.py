import os

from app.settings import get_config
from app.app import create_app

def find_assets():
    """Yield paths for all static files and templates."""
    for name in ['static', 'templates']:
        directory = os.path.join(app.config['PATH'], name)
        for entry in os.scandir(directory):
            if entry.is_file():
                yield entry.path

config = get_config(os.getenv('FLASK_ENV'))

app = create_app(config)

if __name__ == '__main__':
  app.run()
