import mongoengine

#mongodb://htrieu93:prototype101@ds125912.mlab.com:25912/mua_dong_khong_lanh

host = "ds125912.mlab.com"
port = 25912
db_name = "mua_dong_khong_lanh"
user_name = "htrieu93"
password = "prototype101"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
