import json
import logging

from kafka import KafkaProducer


class KafkaHandler(logging.Handler):
    """Class to instantiate the kafka logging facility."""

    def __init__(self, brokers, topic, user, password):
        """Initialize an instance of the kafka handler."""
        logging.Handler.__init__(self)
        self.topic = topic
        self.producer = KafkaProducer(
                                      sasl_plain_username=user,
                                      sasl_plain_password=password,
                                      security_protocol="SASL_PLAINTEXT",
                                      sasl_mechanism="SCRAM-SHA-256",
                                      bootstrap_servers=brokers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      api_version=(0, 10, 1),
                                      linger_ms=10
                                      )


    def emit(self, record):
        """Emit the provided record to the kafka_client producer."""
        # drop kafka logging to avoid infinite recursion
        if 'kafka.' in record.name:
            return

        try:
            # apply the logger formatter
            msg = self.format(record)
            self.producer.send(self.topic, {'message': msg})
            self.flush()
        except Exception:
            logging.Handler.handleError(self, record)

    def flush(self, timeout=None):
        """Flush the objects."""
        self.producer.flush(timeout=timeout)

    def close(self):
        """Close the producer and clean up."""
        self.acquire()
        try:
            if self.producer:
                self.producer.close()

            logging.Handler.close(self)
        finally:
            self.release()
