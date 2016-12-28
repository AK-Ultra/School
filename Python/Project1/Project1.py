import pygame
import time
ascore=0
lscore=0
x=1
def main():
	while x:
		print"----------------------------"
		print"-= Art & Landmark Trivia! =-"
		print"----------------------------"
		print "1. Artwork"
		print "2. Landmarks"
		print "3. Exit"
		choice=input("Pick a category: ")
		if choice == 1:
			artwork()
		if choice == 2:
			landmarks()
		if choice == 3:
			print "Goodbye!"
			break
		print""
		print"You have earned:"
		print ascore,"Art points"
		print lscore,"Landmark points"

def artwork():
	global ascore
	while x:
		print ""
		print"Choose a year of art: "
		print"1517"
		print"1889"
		print"1893"
		print"1902"
		print"'3' to Exit"
		num=input()
		if num == 1517:
			answer = displayArt("./Art/MonaLisa.jpg")
			while answer != "a":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayArt("./Art/MonaLisa.jpg")
			playSound("./Sounds/correct.wav")
			ascore+=1
			print"Correct!"
			
		if num == 1889:
			answer = displayArt("./Art/StarryNight.jpg")
			while answer != "c":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayArt("./Art/StarryNight.jpg")
			playSound("./Sounds/correct.wav")
			ascore+=1
			print"Correct!"
					
		if num == 1893:
			answer = displayArt("./Art/TheScream.jpg")
			while answer != "d":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayArt("./Art/TheScream.jpg")
			playSound("./Sounds/correct.wav")
			ascore+=1
			print"Correct!"
				
		if num == 1902:
			answer = displayArt("./Art/TheThinker.jpg")
			while answer != "b":
				playSound("./Sounds/buzz.wav")
				print"Sorry, that answer is incorrect"
				print""
				answer = displayArt("./Art/TheThinker.jpg")
			playSound("./Sounds/correct.wav")
			ascore+=1
			print"Correct!"
				
		if num == 3:
			break

def landmarks():
	global lscore
	while x:
		print ""
		print"Choose a year in which a landmark was constructed: "
		print"a. 2500 BC"
		print"b. 220 BC"
		print"c. 1450 AD"
		print"d. 1922 AD"
		print"'3' to Exit"
		num=raw_input()
		if num == "c":
			answer = displayLandmark("./Landmarks/MachuPicchu.jpg")
			while answer != "c":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayLandmark("./Landmarks/MachuPicchu.jpg")
			playSound("./Sounds/correct.wav")
			lscore+=1
			print"Correct!"
			
		if num == "a":
			answer = displayLandmark("./Landmarks/StoneHenge.jpg")
			while answer != "d":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayLandmark("./Landmarks/StoneHenge.jpg")
			playSound("./Sounds/correct.wav")
			lscore+=1
			print"Correct!"
					
		if num == "b":
			answer = displayLandmark("./Landmarks/GreatWallChina.jpg")
			while answer != "b":
				playSound("./Sounds/buzz.wav")
				print "Sorry, that answer is incorrect"
				print""
				answer = displayLandmark("./Landmarks/GreatWallChina.jpg")
			playSound("./Sounds/correct.wav")
			lscore+=1
			print"Correct!"
				
		if num == "d":
			answer = displayLandmark("./Landmarks/ChristTheRedeemer.jpg")
			while answer != "a":
				playSound("./Sounds/buzz.wav")
				print"Sorry, that answer is incorrect"
				print""
				answer = displayLandmark("./Landmarks/ChristTheRedeemer.jpg")
			playSound("./Sounds/correct.wav")
			lscore+=1
			print"Correct!"
				
		if num == "3":
			break

def displayArt(picture):
	image=setUpImage()
	readImageFromFile(image,picture)
	print ""
	print "What is the name of this artwork?"
	print "a. The Mona Lisa"
	print "b. The Thinker"
	print "c. The Starry Night"
	print "d. The Scream"
	answer = raw_input()
	pygame.display.quit()
	return answer

def displayLandmark(picture):
	image=setUpImage()
	readImageFromFile(image,picture)
	print ""
	print "What is the name of this landmark?"
	print "a. Christ the Redeemer"
	print "b. Great Wall of China"
	print "c. Machu Picchu"
	print "d. Stonehenge"
	answer = raw_input()
	pygame.display.quit()
	return answer

def setUpImage():
	pygame.init()
	window = pygame.display.set_mode((300, 300), 0, 32)
	return window
	
def readImageFromFile(image,filename):
	newImage=pygame.image.load(filename)
	image.blit(newImage,(0,0))
	pygame.display.update()
	
def playSound(filename):
	pygame.init()
	pygame.mixer.music.load(filename)
	pygame.mixer.music.play()
	time.sleep(1)
main()
