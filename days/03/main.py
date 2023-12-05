path = './input_data.txt'

def readFile (path):
    lines = []

    with open(path, 'r') as file:
        for line in file:
            #lines.append(line.replace('.', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').strip())
            lines.append(line.strip())

    return lines

def explode (data):
    result = []

    for line in data:
        result.append(list(line))

    return result

def findNumbers(line, line_number):
    numbers = []
    number = ''

    for i in range(0, len(line)):

        if line[i].isnumeric():
            number += str(line[i])

        elif line[i-1].isnumeric():
            if isEnginePart(line_number, i, len(number)):
                numbers.append(number)
                number = ''
                
            else:
                number = ''

    if isEnginePart(line_number, 139, len(number)):
        numbers.append(number)
            
    return numbers

def isEnginePart (line_number, index, length):

    for ln in range(-1, 2):
        for li in range(index-length-1, index+1):
            if (0 <= line_number + ln < 140) and lines[line_number + ln][li] in ['*', '$', '/', '@', '%', '#', '+', '&', '-', '=']:
                return True
            
    return False

def calcResult (lines):
    result = 0
    
    for i in range(0, 140):
        for number in findNumbers(lines[i], i): 
            result += int(number)

    return result

#print(readFile(path))
lines = explode(readFile(path))

print('Result Part 1: ' + str(calcResult(lines)))
