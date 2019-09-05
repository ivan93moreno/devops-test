# coding=utf-8
import os

from src import create_app

if "SETTINGS_PATH" not in os.environ:
    path = os.path.abspath(__file__).split("/")
    name = path[-1].split(".")[0]
    path = "./redis-monitoring.ini".format(name)
else:
    path = os.environ["SETTINGS_PATH"]

app = create_app(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
else:
    os.chdir(os.path.dirname(__file__))
    application = app