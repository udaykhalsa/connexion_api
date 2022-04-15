from models import db
from config import application


if __name__ == '__main__':
 db.init_app(application)
 application.run(port=8080)