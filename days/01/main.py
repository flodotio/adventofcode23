path = './input_data.txt'
lines = []
result = 0

with open(path, 'r') as file:
    for line in file:
        lines.append(line.strip())

def calcValue (line):
    numbers = []

    for p in range(0, len(line)):
        for c in convertWritten(line[p:p+5]):
            if c.isnumeric():
                numbers.append(c)

    return numbers[0] + numbers[len(numbers)-1]

def convertWritten (line):
    writtenNumbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(1, 10):
        line = line.replace(writtenNumbers[i-1], str(i))
    
    return line

for line in lines:
    result += int(calcValue(line))

print(result)