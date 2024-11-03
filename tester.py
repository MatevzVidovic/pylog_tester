import os
import logging
import python_logger.log_helper as py_log


MY_LOGGER = logging.getLogger("prototip") # or any string. Mind this: same string, same logger.
MY_LOGGER.setLevel(logging.DEBUG)


python_logger_path = os.path.join(os.path.dirname(__file__), 'python_logger')
handlers = py_log.file_handler_setup(MY_LOGGER, python_logger_path, add_stdout_stream=False)
# def file_handler_setup(logger, path_to_python_logger_folder, add_stdout_stream: bool = False)




@py_log.log(passed_logger=MY_LOGGER)
def forereo(a, b, c):
    pass

forereo(1, 2, 3)






from testing_import import tester




"""
What is happening with MyLuckyNumbers is meant to show how we could use a visualization of an object that is out of scope.

This is a great use of 
list_of_info_dicts = py_log.log_stack(MY_LOGGER)


Imagine MyLuckyNumbers is a machine learning model object.

show_lucky_numbers is a visualization of the model in matplotlib.
It visualizes the state of the model - how many and which neurons have been pruned.

We get an error in the test_me method in the tester class in testing_import.py.
We want to see the state of the model when the error occurred. So in the except block, we want this visualization to be shown.

But we don't have access to the model object in the test_me method.
We can do some MacGyver stuff.
We can use py_log.log_stack(MY_LOGGER) to get a list of info dictionaries.
At each ix is the info_dict of the function at that level in the stack.
The info dict contains the local variables of that function at that time.
We can pull out the model object from these local variables.
And thus we have done what wasn't possible before.

To be able to use show_lucky_numbers both in this file and testing_import.py, we need to have it in a third file my_lucky_numbers.py.
We then import it into both files. This way we don't get circular imports.
"""
from my_lucky_numbers import MyLuckyNumbers, show_lucky_numbers

example_of_object = MyLuckyNumbers([1, 2, 3])

show_lucky_numbers(example_of_object)
    





t = tester()

t.test_me()

@py_log.log(passed_logger=MY_LOGGER)
def test():
    print('test function works')
    vrba = "vas domaca"
    t.test_me()
    py_log.log_locals(MY_LOGGER)
    py_log.log_stack(MY_LOGGER)
    py_log.manual_log(MY_LOGGER, "rocni string", vrba, vrbica_moja=vrba)
    return

test()







forereo(1, 2, 3)