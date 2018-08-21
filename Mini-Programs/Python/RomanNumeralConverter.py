num = input()

ones = {
	0:'',
	1:'I',
	2:'II',
	3:'III',
	4:'IV',
	5:'V',
	6:'VI',
	7:'VII',
	8:'VIII',
	9:'IX',
}
tens = {
	0:'',
	1:'X',
	2:'XX',
	3:'XXX',
	4:'XL',
	5:'L',
	6:'LX',
	7:'LXX',
	8:'LXXX',
	9:'XC',
}
hundreds = {
	0:'',
	1:'C',
	2:'CC',
	3:'CCC',
	4:'CD',
	5:'D',
	6:'DC',
	7:'DCC',
	8:'DCCC',
	9:'CM',
}
thousands = {
	0:'',
	1:'M',
	2:'MM',
	3:'MMM',
	4:'M(V)',
	5:'(V)',
	6:'(V)M',
	7:'(V)MM',
	8:'(V)MMM',
	9:'M(X)',
}
if len(num) == 1:
	print(ones[int(num)])
elif len(num) == 2:
	print(str(tens[int(num[0])]) + str(ones[int(num[1])]))
elif len(num) == 3:
	print(str(hundreds[int(num[0])]) + str(tens[int(num[1])]) + str(ones[int(num[2])]))
elif len(num) == 4:
	print(str(thousands[int(num[0])]) + str(hundreds[int(num[1])]) + str(tens[int(num[2])]) + str(ones[int(num[3])]))
	
	
	
	
	
	
	
