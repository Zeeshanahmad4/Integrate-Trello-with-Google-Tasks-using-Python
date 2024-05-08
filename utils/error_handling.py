# utils/error_handling.py
import logging

def handle_error(e, message="An error occurred", exit_on_failure=False):
    """
    Handles errors by logging them and optionally exiting the program.

    Args:
    e (Exception): The exception object caught from an error.
    message (str): A custom message to log alongside the error information.
    exit_on_failure (bool): Whether to exit the program after logging the error.

    This function logs detailed information about the exception and the state of the application
    at the time of the error. It can also halt the program execution if needed.
    """
    logging.error(f"{message}: {str(e)}")
    # Optionally provide more detailed logging here, such as stack trace
    logging.error("Exception occurred", exc_info=True)
    
    if exit_on_failure:
        # Optionally, you could also perform cleanup here if necessary before exiting
        exit(1)  # Exit code 1 typically indicates an error condition

if __name__ == '__main__':
    # Example usage: This is just for demonstration and testing the function.
    try:
        # Simulate an error condition
        raise ValueError("This is a test error.")
    except Exception as ex:
        handle_error(ex, "Error during test execution", exit_on_failure=True)
