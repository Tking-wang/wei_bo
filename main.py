#!/usr/bin/env python
from flask import Flask,render_template,request,redirect,url_for,flash,sessions
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from libs.orm import db
from user.views import user_bp
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.secret_key = r'askkdhsjkfbdndhcufdsncncsfksdsncsdbf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://WANGZONGR:WZR199632@49.234.218.143:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

db.init_app(app)
migrate = Migrate(app.db)
manager.add_command('db', MigrateCommand)

app.register_blueprint(user_bp)







if __name__ == '__main__':
    manager.run()
