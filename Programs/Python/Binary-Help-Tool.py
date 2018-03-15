def numMake(maximum):
	x = 1
	y = 0
	z = 1
	_max = maximum
	while z < _max:
		x=x+y
		y = x
		x = y + 1
		z = z + 1
	return x
numbers = [1,2,33,256]
# ^^^       ^^^      Numbers that will create the image (Up to 256)
a=0
while a<len(numbers):
	Num = []
	Num = numMake(numbers[a])
	print(str(Num)+'+')
	a +=1
