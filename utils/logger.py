# utils/logger.py
import logging
from logging.handlers import RotatingFileHandler

def configure_logger(name="ApplicationLogger", log_file="application.log"):
    """
    Configures and returns a logger with a specified name and log file.

    Args:
    name (str): The name of the logger.
    log_file (str): The file path for the log file.

    Returns:
    Logger: A configured logger instance.

    This function sets up a logger with both console and file handlers,
    ensuring that logs are written to stdout and to a rotating log file.
    """
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set to the lowest level to capture all messages

    # Create handlers
    c_handler = logging.StreamHandler()  # Console handler
    f_handler = RotatingFileHandler(log_file, maxBytes=1048576, backupCount=5)  # File handler

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Set levels for each handler
    c_handler.setLevel(logging.WARNING)  # Console logs only warnings and above
    f_handler.setLevel(logging.DEBUG)  # File logs everything

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

if __name__ == '__main__':
    # Example usage
    logger = configure_logger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
