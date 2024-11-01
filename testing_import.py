


import os
import logging
import python_logger.log_helper as py_log

MY_LOGGER = logging.getLogger("prototip") # or any string. Mind this: same string, same logger.
MY_LOGGER.setLevel(logging.DEBUG)


# python_logger_path = os.path.join(os.path.dirname(__file__), 'python_logger')
# handlers = py_log.file_handler_setup(MY_LOGGER, python_logger_path, add_stdout_stream=False)
# def file_handler_setup(logger, path_to_python_logger_folder, add_stdout_stream: bool = False)


# Add @log(passed_logger=MY_LOGGER) above functions you want to log.
@py_log.log(passed_logger=MY_LOGGER)
def foo(a, b, c):
    pass

# These automatic logs all contain " @autolog " in their printout.

# Add log_locals(MY_LOGGER) above every return.
# These logs contain " @log_locals " in its printout instead.

foo(1, 2, 3)


@py_log.log_for_class(passed_logger=MY_LOGGER)
class tester:
    # @py_log.log(passed_logger=MY_LOGGER)
    def __init__(self):
        print('tester object created')
    
    # @py_log.log(passed_logger=MY_LOGGER)
    def test_me(self):
        print('testing method works')