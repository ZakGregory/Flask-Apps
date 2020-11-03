from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123@34.105.173.40/testdatabase"

db = SQLAlchemy(app)

from application import routes
