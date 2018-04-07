def read(_list_,divider):
	reader = divider.join(map(str,_list_))
	print(reader)
def write(_list_):
	while 1:
		values = input('>>>  ')
		if values.isdigit():
			values = int(values)
		_list_.append(values)
		if values == '':
			_list_.remove('')
			break
		
def mean(_list_):
	avg = ''
	try:
		avg = sum(_list_)/len(_list_)
		if str(avg)[-2::] == '.0':
			avg = int(avg)
	except TypeError as Te:
		print('TypeError: ',Te,'\nCan\'t have a letter or a special character to calculate the average.')
	return avg
#def strConvert(_list_):
#	while 1:
#		_list_[index]=str(_list_[index])
			
