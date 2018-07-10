from PIL import Image

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

def createImage(colors):
    # Converts lists to bytes
    colors = bytes(colors)
    # Converts bytes to a full size image
    img = Image.frombytes('RGB', (width, height), colors)
    # Shows image
    img.show()
    # Saves image
    img.save('hues.png')

def GSfy(image):
    img = imgExtract(image)
    img = avgList(img)
    img = flattenImg(img)
    createImage(img)
