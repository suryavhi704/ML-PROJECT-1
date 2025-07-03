import sys # to ignore the exception in tests
from src.logger import logging # to log the error message
# custom exception class for handling exceptions in the pipeline
def error_message_details(error,error_details:sys):
    _, _, exc_tb = error_details.exc_info() #on which line the error occurred the variable exc_tb is used to get the traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"Error occurred in script: [{0}] at line number: [{1}] with message: [{2}]".format()
    file_name, exc_tb.tb_lineno, str(error)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details)

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return CustomException.__name__.str()
    