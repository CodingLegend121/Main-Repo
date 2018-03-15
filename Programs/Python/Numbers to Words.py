'''

NumWord v2.9.0


'''



print('This is an amazing 5 digit Number to Word Converter\nIt was a 3-day challenge\nHere you go!!\n')
num = input(' Number (0 - 99999): ')

def Num(Number):
	Number = str(Number)
	digit1 = {
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine',
	0:''
}
	digit2 = {
	0:'ten',
	1:'eleven',
	2:'twelve',
	3:'thirteen',
	4:'fourteen',
	5:'fifteen',
	6:'sixteen',
	7:'seventeen',
	8:'eighteen',
	9:'nineteen',
}
	tenth = {
	2:'twenty',
	3:'thirty',
	4:'fourty',
	5:'fifty',
	6:'sixty',
	7:'seventy',
	8:'eighty',
	9:'ninety'
}
	print('\n______________________________________________\n')
	if int(Number) == 0:
		print('zero')
	Number = Number.lstrip('0')
	if len(Number) == 1:
		print(digit1[int(Number)])
	elif len(Number) == 2:
		list(str(Number))
		if int(Number) <= 19:
			print(digit2[int(Number[1])])
		elif int(Number) > 19:
			if int(Number[1]) == 0:
				print(tenth[int(Number[0])])
			else:
				print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])])
	elif len(Number) == 3:
		list(str(Number))
		if int(Number[1]) == 0:
			if int(Number[2]) == 0:
				print(digit1[int(Number[0])] + ' hundred ' )
			else:
				print(digit1[int(Number[0])] + ' hundred and ' + digit1[int(Number[2])])
		elif int(Number[1]) == 1:
			print(digit1[int(Number[0])] + ' hundred and ' + digit2[int(Number[2])])
		else:
			print(digit1[int(Number[0])] + ' hundred and ' + tenth[int(Number[1])] + ' ' + digit1[int(Number[2])])
	elif len(Number) == 4:
		list(str(Number))
		if int(Number[1]) == 0 and int(Number[2]) == 0 and int(Number[3]) == 0:
			print(digit1[int(Number[0])] + ' thousand ' )
		elif int(Number[1]) == 0 and int(Number[2]) == 0:
			print(digit1[int(Number[0])] + ' thousand and ' + digit1[int(Number[3])])
		elif int(Number[1]) == 0:
			if int(Number[2]) == 1:
				print(digit1[int(Number[0])] + ' thousand and '+ digit2[int(Number[3])])
			else:
				print(digit1[int(Number[0])] + ' thousand and '+ tenth[int(Number[2])] + ' ' + digit1[int(Number[3])])
		elif int(Number[2]) == 1:
			print(digit1[int(Number[0])] + ' thousand ' + digit1[int(Number[1])] + ' hundred and ' + digit2[int(Number[3])])
		elif int(Number[2]) == 0:
			print(digit1[int(Number[0])] + ' thousand ' + digit1[int(Number[1])] + ' hundred and ' + digit1[int(Number[3])])
		else:
			print(digit1[int(Number[0])] + ' thousand ' + digit1[int(Number[1])] + ' hundred and ' + tenth[int(Number[2])] + ' ' + digit1[int(Number[3])])
	elif len(Number) == 5:
		list(str(Number))
		if int(Number[2]) == 0 and int(Number[3]) == 0 and int(Number[4]) == 0:
			if int(Number[0]) == 1:
				print(digit2[int(Number[1])] + ' thousand ')
			elif int(Number[0]) != 1:
				if int(Number[1]) == 0:
					print(tenth[int(Number[0])] + ' thousand')
				elif int(Number[1]) != 0:
					print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])]+ ' thousand')
		elif int(Number[2]) == 0 and int(Number[3]) == 0:
			if int(Number[0]) == 1:
				print(digit2[int(Number[1])] + ' thousand and ' + digit1[int(Number[4])])
			elif int(Number[0]) != 1:
				print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])] + ' thousand and ' + digit1[int(Number[4])])
		elif int(Number[3]) == 0 and int(Number[4]) == 0:
			if int(Number[0]) == 1:
				print(digit2[int(Number[1])] + ' thousand and ' + digit1[int(Number[2])] + ' hundred')
			elif int(Number[0]) != 1:
				print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])] + ' thousand and ' + digit1[int(Number[2])] + ' hundred')
		elif int(Number[2]) == 0:
			if int(Number[0]) == 1:
				if int(Number[3]) == 1:
					print(digit2[int(Number[1])] + ' thousand and '+ digit2[int(Number[4])])
				else:
					print(digit2[int(Number[1])] + ' thousand and '+ tenth[int(Number[3])] + ' ' + digit1[int(Number[4])])
			else:
				if int(Number[3]) == 1:
					print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])] + ' thousand and ' +digit2[int(Number[4])])
				else:
					print(tenth[int(Number[0])] + ' ' +  digit1[int(Number[1])] + ' thousand and '+ tenth[int(Number[3])] + ' ' + digit1[int(Number[4])])
		else:
			if int(Number[0]) == 1:
				if int(Number[3]) == 1:
					print(digit2[int(Number[1])] + ' thousand ' + digit1[int(Number[2])] + ' hundred and ' + digit2[int(Number[4])])
				elif int(Number[3]) == 0:
					print(digit2[int(Number[1])] + ' thousand ' + digit1[int(Number[2])] + ' hundred and ' + digit1[int(Number[4])])
				else:
					print(digit2[int(Number[1])] + ' thousand ' + digit1[int(Number[2])] + ' hundred and ' + tenth[int(Number[3])] + ' ' + digit1[int(Number[4])])
			else:
				if int(Number[3]) == 1:
					print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])] + ' thousand ' + digit1[int	(Number[2])] + ' hundred and '+digit2[int(Number[4])])
				elif int(Number[3]) == 0:
					print(tenth[int(Number[0])] + ' ' + digit1[int(Number[1])] + ' thousand ' + digit1[int(Number[2])] + ' hundred and ' + digit1[int(Number[4])])
				else:
					print(tenth[int(Number[0])] + ' ' +  digit1[int(Number[1])] + ' thousand ' + digit1[int(Number[2])] + ' hundred and ' + tenth[int(Number[3])] + ' ' + digit1[int(Number[4])])
	print('______________________________________________')

Num(num)
