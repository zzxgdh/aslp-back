from flask import Flask
from .model.model import db
from .controller.home import home_bp


HOSTNAME='127.0.0.1'
PORT=3306
USERNAME='root'
PASSWORD='123456'
DATABASE='pydatabase'

class App():
    def __init__(self):
        # app初始化
        self.app = Flask(__name__)
        # 连接数据库的字符串
        self.app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
        # 初始化数据库连接
        db.init_app(self.app)
        # 注册路由
        self.app.register_blueprint(home_bp)


    def run(self):
        self.app.run(host='0.0.0.0', port=8888, debug=True)


aslp_app = App()



