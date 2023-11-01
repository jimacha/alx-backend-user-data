#!/usr/bin/env python3
"""
Module for filtering sensitive information from log messages.
"""

import logging
import re
from typing import List

PII_FIELDS: List[str] = ["name", "email", "phone", "ssn", "password"]

class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for logging.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.
        """
        msg = super().format(record)
        for field in self.fields:
            msg = re.sub(rf'{field}=(.*?){self.SEPARATOR}', f'{field}={self.REDACTION}{self.SEPARATOR}', msg)
        return msg

def get_logger() -> logging.Logger:
    """
    Returns a logger object named 'user_data'.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(PII_FIELDS)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

def get_db() -> Any:
    """
    Connects to the database and returns a connection object.
    """
    # Your database connection logic here
    pass

if __name__ == "__main__":
    logger = get_logger()
    logger.info("This is a sample log message.")
