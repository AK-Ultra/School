import pygame
import time
def playSound(filename):
	pygame.init()
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
	time.sleep(2)
playSound("correct.wav")
