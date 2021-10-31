def switchText():
    file1 = open('essay.txt')
    file2 = open('nonsense.txt')

    file1Contents = file1.read()
    file2Contents = file2.read()

    file1 = open('essay.txt', 'w')
    file2 = open('nonsense.txt', 'w')

    file1.write(file2Contents)
    file2.write(file1Contents)

switchText()
print('Files switched, hehehe')