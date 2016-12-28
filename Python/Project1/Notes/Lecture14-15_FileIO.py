'''
Lecture14-15.py
Author: Rhonda Hoenigman
University of Colorado, Boulder
Fall, 2015
'''
'''
Programs often need data as part of the functionality of the program.
For example, in our lecture on strings, we typed a long string in
Geany to declare a string variable. For example, DNA = "ATGATCGGGCAGT".
When doing that, it's very easy to make a mistake, and it's also tedious
to have to type that, especially if you're working with multiple DNA
sequences, or multiple instances of any kind of data for that matter.
Another approach is to store the DNA sequence in a file and then read the
data into your program by accessing that file in your program, opening
it, reading in the data and storing it in variables, and then closing 
the file. This is really useful when you have lots of data that 
you're working with, or when you need to do something more than once. 
You can do that using what's called File I/O, these are commands in 
Python that allow you to read in data from files and also write data 
out to files for storage.

'''
'''
Lets say we have a file called textToEnglish.txt that has a bunch of 
texting slang and the english equivalents in it. There are 4000+ rows in
the file. You certainly would not want to type all of this data or ask
the user to enter it. But, since it's in a file, we can just read it in
and then work with it in our program.
The textToEnglish.txt file is on Moodle
I'm going to open it and print its contents.

Create a function to open and read the file.
'''
def openAndReadFile(filename):
	myFile = open(filename, "r")
	'''
	The open command is built-in to Python, and it's looking for two arguments.
	First, the name of the file to open, here, that's textToEnglish.txt. 
	The file is
	in the same directory as the .py file. The second
	argument is what can be done to the file once it's open. There are several
	options for actions on the file. The "r" means only allow reading of the
	file, nothing can be written back out to the file in this way. This is
	a safe way to open a file because it means that you can't 
	do anything in your code that will overwrite the file in any 
	way. You don't have write permissions on the file when it's opened with
	the "r". 
	'''

	print myFile
	'''
	The variable myFile is a data type that we haven't used yet, it's 
	called a file object, and it contains a pointer to the data stored in the
	file.  
	Objects variables have methods, aka functions, that you can call to get
	information about the object or modify it in some way. 

	In the line myFile.close(), the close() is a method, an action 
	that we do to myFile
	If you print myFile, you'll see information about the object, showing the
	name and type of permissions, and the encoding.
	'''

	'''
	Another method on the file object is the readlines method, which is
	one mechanism for getting the information stored in the file into
	our program. Here, we create a variable called fileData and store
	everything in the file in the variable fileData.
	'''
	fileData = myFile.readlines()
	#close the file
	myFile.close()
	'''
	We want our main program to be aware of the data we just read, so
	we'll return the fileData variable.
	'''
	return fileData

def dataCleanup(word):
	word = word.strip("\n")
	word = word.split("\t")
	return word
	
def writeDataToFile(filename, data):
	'''
	We can also reverse the process and write data to a file
	
	We need to open the file the same way we did to read the file. 
	However, we open the file in a different mode. Here, we open it for
	writing, using the "w" specifier. When we do this, it will wipe out
	whatever is currently in that file, or create a file with that name
	if the file doesn't already exist.
	'''
	myFileOut = open(filename, "w")
	'''
	other modes that could be used are 
	r+ to open a file for reading and writing
	a to open a file and append the new data onto the existing file data
	'''

	'''
	Write all data in the data variable out to myFileOut
	'''
	for element in data:
		myFileOut.write(element[0] + "\t" + element[1] + "\n")
	
	myFileOut.close()

def openAndReadFileWExceptions(filename):
	'''
	The syntax here is try to open the file, and if it doesn't work, 
	there is an exception. The code in the except IOError will run when
	there is an exception. If there isn't an exception, then the else
	code will run.
	'''
	try:
		f = open(filename, "r")
	except IOError:
		print 'cannot open', filename
		fileData = None
	else:
		fileData = f.readlines()
		f.close()
	return fileData
		
def main():
	filename = "textToEnglish.txt"
	'''
	fileData contains the data read out of the file in the openAndReadFile
	function.
	'''
	fileData = openAndReadFile(filename)
	print fileData
	'''
	readlines generates a list, where each item in the list is one of the 
	lines in the file. You can access individual lines using the index of 
	the line in the file. For example, to access the first line
	'''
	print(fileData[0])
	'''and the second line'''
	print(fileData[1])

	'''
	The openAndReadFile function works fine as long as the file actually
	exists. However, what if the filename is typed wrong, or someone 
	enters the wrong name, or it's been deleted already. If that happens,
	then, when we try to open the file the program will generate an 
	I/O exception. We can add code to handle the exception and let the
	program fail gracefully instead of crashing.

	open a file that doesn't exist.
	'''
	#f = openAndReadFile("bogusFile")
	f = openAndReadFileWExceptions("bogusFile")
	print f
	'''
	The data is currently a list of strings, where each string contains
	the abbreviation and the translation. But, depending on what we want
	to do with this data, that might not be useful to us. Usually in 
	computer science, we want data to be searchable. We want discrete
	element where we can compare things to each other and check if we 
	have a certain value. In this case, we might want to check if a 
	particular abbreviation is in our list. We can't easily do that now
	with what we have because the abbreviation is just part of a string
	with some extra formatting and the translation. We need to do some
	string manipulation to get that string into a format that is easier 
	to work with. We're going to convert it to a list of lists, where 
	the first list element is the abbreviation and the second list 
	element is the translation.

	The process to do that is to create a new empty list, look at each 
	list element, remove the formatting, create a list with the abbrev.
	and translation, and append that list to a master list.
	'''
	newList = []
	for data in fileData:
		'''
		dataCleanup is a function that removes formatting and converts
		the string into a list. I put it in its own function to make this
		loop easier to read.
		'''
		word = dataCleanup(data)
		'''
		The word variable is a list. append it to the master list.
		'''
		newList.append(word)
	print newList

	'''
	Adding rows to the file.
	What if there are abbreviations not in the file and you want to add
	them. If you do, then next time you open and read the file, your
	additions will be there.
	'''
	filename = "fileTestOut.txt"
	writeDataToFile(filename, newList)

	'''
	exercise: add a new abbrev and translation to your list and write
	it out to a file. You can use the same filename, or create a new one
	'''
	
main()





