import configparser, os
class GetData:
    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = dir + "/url_data.ini"
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding='utf-8')
    url = cf.get("url", "test_url")

class GetDBDate:
    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = dir + "/db_mysql.ini"
    cf = configparser.ConfigParser()
    cf.read(file_path, encoding='utf-8')
    host = cf.get("mysql", "host")
    port = cf.get("mysql", "port")
    user = cf.get("mysql", "user")
    password = cf.get("mysql", "password")
    db_name = cf.get("mysql", "db_name")

