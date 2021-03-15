from datetime import datetime
from inspect import signature

def logger(some_func):
    def wrapped(*args, **kwargs):
        now = datetime.now()
        function_name = some_func.__name__ #имя с которым определена функция

        sig = signature(some_func)
        b = sig.bind(*args, **kwargs)
        args = b.args
        kwargs = b.kwargs

        result = some_func(*args, **kwargs)

        f = open ('log.txt', 'w')
        f.write(str(now) + '\t' + str(function_name) + '\t' +
                str(args) + str(kwargs) + '\t' +
                str(result) + '\t' + '\n')
        f.close()
        return

    return wrapped



#@logger
#def hello_decor(*args, **kwargs):
    #return 'return_values'

#hello_decor('Here', 'we will pass ', 'many', name='arguments' )
