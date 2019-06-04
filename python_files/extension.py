from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy


admin = Admin(name="Admin Page", template_mode='bootstrap3')
db = SQLAlchemy()

