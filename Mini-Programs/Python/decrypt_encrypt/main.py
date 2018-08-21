

binfile = open('bin.txt','r')
bin_key = binfile.read().split('\n')
charfile = open('chars.txt','r')
char_key = charfile.read().split('\n')

key = dict(zip(char_key,bin_key))
key2 = dict(zip(bin_key,char_key))

name = '1'

def encode(name):
	nameList = []

	for char in name:
		char = key[char]
		nameList.append(char)

	name = ''.join(nameList)

	return (int(name,2))

def decode(code):
	codeList = []
	code = format(int(code),'b')
	code = list(str(code))
	length = len(code)
	x = 0
	while x < (8000-length):
		code.insert(0,'0')
		x = x + 1
	code = ''.join(code)
	code = [code[i:i+8] for i in range(0, len(code), 8)]
	for val in code:
		val = key2[val]
		codeList.append(val)
	code = ''.join(codeList)
	return code

for x in range(1000):
	try:
		print(x,'     ',decode(x))
	except:
		pass