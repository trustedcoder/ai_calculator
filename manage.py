from flask_script import Manager
from app.main import create_app

import os

config_name = os.getenv("ENV","dev")

app = create_app(config_name)
manager = Manager(app)


@manager.command
def run():
    app.run(host="127.0.0.1", port=7003)


if __name__ == "__main__":
    manager.run()
