from random import randint


def fileOpener():
    fileName = str(input("\nPlease enter the file you wish to be Encrypted: ")).upper()
    if fileName == "SAMPLE.TXT":
        fN = open(fileName)
        global fileContents
        fileContents = fN.read()
        fileName.close
        

def offsetCharacter():
    randomEight = []
    for i in range(8):
        randomEight.append(chr(randint(33, 126)))
    print("Here is your random Eight Character Key: " + ','.join(randomEight))
    asciiSum = 0
    for num in randomEight:
        asciiSum = asciiSum + ord(num)
    global offsetCharacter
    offsetCharacter = ((int(asciiSum/8))-32)
    print("Value of the offset character is : " + str(offsetCharacter))    



offsetCharacter()
    


#player = str(input("Please enter your name: ")) 
#print("\nHello " + player)
#print("\nPlease select one of the options below:\n1. Encrypt Code\n2. Decrypt Message\n3. Exit the Program")

