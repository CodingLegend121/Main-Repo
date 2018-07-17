from PIL import Image

image = '' #image

# Calculates the size of the image
imageSize = Image.open(image, 'r')
width,height = imageSize.size

def imgExtract(imgEx):
    # Opens image
    img = Image.open(imgEx, 'r')
    # Gathers each pixel's RGB data
    pix_val = list(img.getdata())
    return pix_val	
def flattenImg(pix_val):
    # Makes the list of tuples into one long list
    pix_val = [x for sets in pix_val for x in sets]
    return pix_val
def avgList(L):
    # Calculates Average for each tuple in the list
    lens = map(len, L)
    res = [(round(sum(i)/i_len,),)*i_len for i, i_len in zip(L, lens)]
    return res
def createImage(imageData,fileName = 'picture'):
    # Converts lists to bytes
    colors = bytes(imageData)
    # Converts bytes to a full size image
    img = Image.frombytes('RGB', (width, height), colors)
    # Shows image
    img.show()
    # Saves image
    img.save(fileName +'.png')
def subtractRGB(thing):
	# Subtract RGB value with 255
	for i,value in enumerate(thing):
		thing[i] = 255-value
	return thing
	# Grayscale process
def GSfy(image):
    img = imgExtract(image)
    img = flattenImg(avgList(img))
    createImage(img,'grayscale')
	# Inverting process
def invert(image):
	img = imgExtract(image)
	img = subtractRGB(flattenImg(img))
	createImage(img,'inverted')

def contrast(thing):
	for i,value in enumerate(thing):
		if value > 127:
			thing[i] = (152,251,152)
		else:
			thing[i] = (0,0,0)
	return thing

def contrast2(thing):
	for i,value in enumerate(thing):
		if value == 255:
			thing[i] = (255,255,255)
		else:
			thing[i] = (0,0,0)
	return thing


def binaryfy(thing):
	for i,value in enumerate(thing):
		if value < 127:
			thing[i] = 1
		else:
			thing[i] = 0
	return thing	

def unbinaryfy(thing):
	for i,value in enumerate(thing):
		if value == '1':
			thing[i] = 0
		else:
			thing[i] = 255
	return thing	


def compress(thing):
	for i,value in enumerate(thing):
		thing[i] = statistics.mode(thing[i])
	return thing

'''def step1(img):
	imageBin = binaryfy(compress(avgList(imgExtract(img))))
	imageBin = ''.join(map(str,imageBin))
	imageBin = str(int(imageBin,2))
	imageFile = open('dataFile.txt','w+')
	imageFile.write(imageBin)
	imageFile.close()


def step2():
	dataFile = open('dataFile.txt','r')
	imageData = dataFile.read()
	imageData = flattenImg(contrast2(unbinaryfy(list(format(int(imageData),'b')))))

	createImage(imageData,'final2')
'''
