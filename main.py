def replaceTextInFile(fileName, originText, newText):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = data.replace(originText, newText)

    with open(fileName, 'w') as fileHandler:
        fileHandler.write(data)


def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)


myFile = 'test.txt'

print("Original file content:")
readFromFile(myFile)

replaceTextInFile(myFile, 'while', 'пока')

print("New file content:")
readFromFile(myFile)