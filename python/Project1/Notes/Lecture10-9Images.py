import pygame

def main():
	image=setUpImage()
	#drawColor(image,makeColor(255,255,0))
	readImageFromFile(image,"enginctr.jpg")
	#modifyImage(image)
	#saveImageToFile(image,"enginctrgreen.jpg")
	raw_input() #keeps program from ending, so can see image
	pygame.display.quit()
main()
