from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from libs.orm import db

app = Flask(__name__)
app.secret_key = r'askkdhsjkfbdndhcufdsncncsfksdsncsdbf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://WANGZONGR:WZR199632@localhost/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

db.init_app(app)
migrate = Migrate(app.db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
