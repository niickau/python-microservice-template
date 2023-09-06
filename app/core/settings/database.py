import yaml


db_creds = yaml.load(open('./credentials.yml')).get("database")

DATABASE_SETTINGS = {
    'host': db_creds.get("hostname"),
    'port': db_creds.get("port"),
    'user': db_creds.get("username"),
    'password': db_creds.get("password"),
    'database': db_creds.get("database")
}
