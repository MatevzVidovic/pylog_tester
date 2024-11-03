


import os
import logging
import python_logger.log_helper as py_log

MY_LOGGER = logging.getLogger("prototip") # or any string. Mind this: same string, same logger.
MY_LOGGER.setLevel(logging.DEBUG)


# python_logger_path = os.path.join(os.path.dirname(__file__), 'python_logger')
# handlers = py_log.file_handler_setup(MY_LOGGER, python_logger_path, add_stdout_stream=False)
# def file_handler_setup(logger, path_to_python_logger_folder, add_stdout_stream: bool = False)





@py_log.log(passed_logger=MY_LOGGER)
def foo(a, b, c):
    pass

foo(1, 2, 3)


from my_lucky_numbers import MyLuckyNumbers, show_lucky_numbers


@py_log.log_for_class(passed_logger=MY_LOGGER)
class tester:
    # @py_log.log(passed_logger=MY_LOGGER)
    def __init__(self):
        print('tester object created')
    
    # @py_log.log(passed_logger=MY_LOGGER)
    def test_me(self):
        
        try:
            1 / 0
        except ZeroDivisionError as e:
            list_of_info_dicts = py_log.log_stack(MY_LOGGER)

            print(len(list_of_info_dicts))


            # test_me() is used twice in our code.
            # In one call, the stack size is 4, in another it is 6.
            # We know the example_of_object variable is located in the outermost function.
            # The info_dict of the outermost function is at the last index.
            # So we set the levet to -1 so that the index resolves correctly.
            level_where_MyLuckyNumbers_was_created = -1

            # We could also use the filename and function name to find the correct level.
            # So we would iterate over the list of info_dicts and find the one where the filename is tester.py and the function name is <module>.
            # (We know this from looking at the stack lof in the log viewer.)
            # (We could iterrate up or down the list and stop at first correct match. Just depends on what works for our specific case.)

            # But for us, we know it is always the last index, so we just use -1.
            
            relevant_info_dict = list_of_info_dicts[level_where_MyLuckyNumbers_was_created]
            relevant_local_vars = relevant_info_dict['local_vars']

            the_lucky_numbers_obj = relevant_local_vars["example_of_object"]
            show_lucky_numbers(the_lucky_numbers_obj)

        print('testing method works')