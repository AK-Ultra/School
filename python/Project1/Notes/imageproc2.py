
import pygame

def main():
	image=setUpImage()
	#drawColor(image,makeColor(255,255,0))
	readImageFromFile(image,"enginctr.jpg")
	#modifyImage(image)
	#saveImageToFile(image,"enginctrbw.jpg")
	raw_input() #keeps program from ending, so can see image
	pygame.display.quit()
	
def bright(pixel):
	sum=getR(pixel)+getG(pixel)+getB(pixel)
	ave=sum/3
	return ave


def makeColor(r,g,b):
	color=256*256*r+256*g+b
	return color
	
def getB(color):
	return color%256
	
def getG(color):
	return (color-256*256*getR(color))/256
	
def getR(color):
	return color/(256*256)
	
def setUpImage():
	pygame.init()
	window = pygame.display.set_mode((300, 300), 0, 32)
	return window
	
def drawColor(image,color):
	pixArray = pygame.PixelArray(image)
	for x in range(300):
		for y in range(300):
			pixArray[x][y]=color
	del pixArray
	pygame.display.update()
	
def modifyImage(image):
	pixArray = pygame.PixelArray(image)
	for x in range(300):
		for y in range(300):
			#pixArray[x][y]=makeColor(0,getG(pixArray[x][y]),0)
			val=bright(pixelArray[x][y])
			pixArray[x][y]=makeColor(val,val,val)
	del pixArray
	pygame.display.update()
	
def readImageFromFile(image,filename):
	newImage=pygame.image.load(filename)
	image.blit(newImage,(0,0))
	pygame.display.update()
	
def saveImageToFile(image,filename):
	pygame.image.save(image,filename)
	
main()
	
	





