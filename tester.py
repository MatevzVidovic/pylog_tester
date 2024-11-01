import os
import logging
import python_logger.log_helper as py_log


MY_LOGGER = logging.getLogger("prototip") # or any string. Mind this: same string, same logger.
MY_LOGGER.setLevel(logging.DEBUG)


python_logger_path = os.path.join(os.path.dirname(__file__), 'python_logger')
handlers = py_log.file_handler_setup(MY_LOGGER, python_logger_path, add_stdout_stream=False)
# def file_handler_setup(logger, path_to_python_logger_folder, add_stdout_stream: bool = False)




from testing_import import tester





# Add @log(passed_logger=MY_LOGGER) above functions you want to log.
@py_log.log(passed_logger=MY_LOGGER)
def forereo(a, b, c):
    pass

# These automatic logs all contain " @autolog " in their printout.

# Add log_locals(MY_LOGGER) above every return.
# These logs contain " @log_locals " in its printout instead.

forereo(1, 2, 3)


t = tester()

t.test_me()

@py_log.log(passed_logger=MY_LOGGER)
def test():
    print('test function works')
    t.test_me()

test()


forereo(1, 2, 3)