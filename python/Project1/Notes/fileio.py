def openFilesAndRead():
    myFile = open("lines.txt","r")
    
    lns = myFile.readlines()
    
    for line in lns:
        print line
    
    myFile.close()


def addTwoNumbers(num1, num2):
    return num1+num2


"""
create a function to read in two numbers at a time and print the first number divided by the second
then the remainder after division

e.g. for 14 and 7 it should print 2 r 0
"""    


def printDivision(num1,num2):
    return str(num1/num2) +" r "+ str(num1%num2)
    
def main():
    openFilesAndRead()
    print "2+2 =",addTwoNumbers(2,2)
    print "4+8 =",addTwoNumbers(4,8)
    
    numFile = open("nums.dat","r")
    numLines = numFile.readlines()
    
    for line in range(0,len(numLines),2):
        print int(numLines[line]), "+", int(numLines[line+1]), "=", \ # the backslash allows me to go to a new line
            addTwoNumbers(int(numLines[line]), int(numLines[line+1]))
        print int(numLines[line]), "/", int(numLines[line+1]), "=", \ # the backslash allows me to go to a new line
            printDivision(int(numLines[line]), int(numLines[line+1]))
    numFile.close()
    
    try:
        newFile = open("non-existent.txt","r")
    except IOError:
        print "file non-existent.txt does not exist"
    else:
        print "do other work here"
if __name__=="__main__":
    main()
