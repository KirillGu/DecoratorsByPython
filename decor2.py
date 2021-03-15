from datetime import datetime
from inspect import signature
import os


def parameterized_logger(path):
    logs_file_name = os.path.join(path, 'log.txt')

    def logger(some_function):
        def log_function(*args, **kwargs):

            now = datetime.now()
            function_name = some_function.__name__

            sig = signature(some_function)
            b = sig.bind(*args, **kwargs)
            args = b.args
            kwargs = b.kwargs

            function_return = some_function(*args, **kwargs)

            f = open(logs_file_name, 'w')
            f.write(str(now) + '\t' + str(function_name) + '\t' +
                    str(args) + str(kwargs) + '\t' +
                    str(function_return) + '\t' + '\n')
            f.close()
            return
        return log_function

    return logger


#@parameterized_logger("/Users/kirillgusev/Desktop/")
#def say_something(*args, **kwargs):
    #return 'func_results'

#say_something('Here', 'we will pass ', 'many', name='arguments' )
