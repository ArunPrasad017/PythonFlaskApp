import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask_project.app import app, db
from flask_project import models

manager = Manager(app)

manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()
