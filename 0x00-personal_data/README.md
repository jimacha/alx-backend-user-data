Curriculum <br>
**Short Specialization** <br>

# 0x00. Personal data

# Personal Data Management

This project focuses on back-end development and authentication systems, emphasizing the importance of securing personal data. Below are the tasks and their respective requirements.

## Task 0: Personal Data

Implement the `filter_datum` function in `filtered_logger.py`:

```python
def filter_datum(fields, redaction, message, separator):
    """ Returns log message obfuscated """
```

**Arguments:**
- `fields`: A list of strings representing fields to obfuscate.
- `redaction`: A string representing how the field will be obfuscated.
- `message`: A string representing the log line.
- `separator`: A string representing the character separating all fields in the log line.

The function should use a regex to replace occurrences of certain field values.

## Task 1: Log Formatter

Update the `RedactingFormatter` class in `filtered_logger.py`:

```python
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    
    def __init__(self, *args, **kwargs):
        """ Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record):
        """ Format method """
        raise NotImplementedError
```

The class should accept a list of strings `fields` in its constructor and filter values in incoming log records using `filter_datum`.

## Task 2: Create Logger

Implement the `get_logger` function in `filtered_logger.py`:

```python
def get_logger() -> logging.Logger:
    """ Returns a logging.Logger object """
```

The logger should be named "user_data" and only log up to `logging.INFO` level. It should not propagate messages to other loggers. It should have a `StreamHandler` with `RedactingFormatter` as the formatter. Use the `PII_FIELDS` constant to parameterize the formatter.

## Task 3: Connect to Secure Database

Implement the `get_db` function in `filtered_logger.py`:

```python
def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to the database """
```

The function should use the `os` module to obtain credentials from the environment and connect to the MySQL database using the `mysql-connector-python` package.

## Task 4: Read and Filter Data

Implement the `main` function in `filtered_logger.py`:

```python
def main() -> None:
    """ Main function """
```

The function should obtain a database connection, retrieve all rows in the `users` table, and display each row under a filtered format.

## Task 5: Encrypting Passwords

Implement the `hash_password` function in `encrypt_password.py`:

```python
def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password """
```

The function should use the `bcrypt` package to hash the password.

## Task 6: Check Valid Password

Implement the `is_valid` function in `encrypt_password.py`:

```python
def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates if a provided password matches the hashed password """
```

The function should use `bcrypt` to validate that the provided password matches the hashed password.

---

**Note:** The provided code snippets serve as a guideline for the implementation. Ensure that your solution adheres to the specified requirements and functionality for each task.