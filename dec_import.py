from decor1 import logger

@logger
def get_employees(*args, **kwargs):
	print('***dec_import***')
	return args, kwargs

get_employees('Well', 'Done', name='Steak')
