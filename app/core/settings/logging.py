import yaml


kafka_creds = yaml.load(open('./credentials.yml')).get("kafka")

LOGGING_ON = True
LOGGING_KAFKA_BROKERS = kafka_creds.get("brokers")
LOGGING_KAFKA_TOPIC = kafka_creds.get("topic_name")
LOGGING_KAFKA_USER = kafka_creds.get("user_name")
LOGGING_KAFKA_PASSWORD = kafka_creds.get("user_password")
