import pygame
#img = pygame.image.load('monalisa.jpg')

#white = (255, 255, 255)
#w = 300
#h = 300
#screen = pygame.display.set_mode((w, h))
#screen.fill((white))
#running = 1


#screen.blit(img,(0,0))
#pygame.display.flip()


def main():
	image=setUpImage()
	readImageFromFile(image,"monalisa.jpg")
	raw_input("Was ist das?")
	pygame.display.quit()

def setUpImage():
	pygame.init()
	window = pygame.display.set_mode((300, 300), 0, 32)
	return window
	
def readImageFromFile(image,filename):
	newImage=pygame.image.load(filename)
	image.blit(newImage,(0,0))
	pygame.display.update()
	
main()
