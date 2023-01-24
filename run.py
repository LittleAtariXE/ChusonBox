from app import create_app


app = create_app('test')
from views import *



if __name__ == '__main__':
    app.run()

