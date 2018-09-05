import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds133601.mlab.com:33601/cms-app

host = "ds133601.mlab.com"
port = 33601
db_name = "cms-app"
user_name = "htrieu"
password = "prototype101"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
