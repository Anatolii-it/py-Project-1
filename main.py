with open('test.txt', 'r') as fileHandler:
    for line in fileHandler:
        print(line)

path1 = "test.txt"
path2 = "test2.txt"

with open(path1) as inFile, open(path2, "w") as outFile:
    # прочитать содержимое файла example.txt
    fileContents = inFile.read()
    # трансформируем контент
    fileContents = fileContents.lower()
    # записываем преобразованное содержимое
    outFile.write(fileContents)

