from flask import Flask
from extension import admin, db
import config
# from flask_admin import AdminIndexView
from flask_admin.contrib.sqlamodel import ModelView
from models import User


app = Flask(__name__)

app.config['SECRET_KEY'] = '123456790'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # 부트스트랩 테마

db.init_app(app)  # flask와 sqlalchemy 연동
admin.init_app(app)  # flask와 admin 연동


class ModelView2(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = False
    can_export = False
    create_modal = True


admin.add_view(ModelView2(User, db.session)) # model view

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_FILE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# adminindexview = AdminIndexView(name='admin2')
# admin.add_view(adminindexview)


@app.before_first_request
def initial():
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
