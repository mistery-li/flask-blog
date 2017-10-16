from flask.ext.script import Manager

from app import crate_app, db

app = crate_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()