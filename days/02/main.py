path = './input_data.txt'
cubes = {'green': 13, 'red': 12, 'blue': 14}
index = 1
result = 0

def readFile (path):
    lines = []

    with open(path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines

def convertToMap(game):
    colors = ['green', 'red', 'blue']
    map = []

    # Remove game number and spaces
    game = game.replace(' ', '').split(':')[1].split(';')

    # Loop through each round of the game
    for round in range(0, len(game)):
        #print('Round: '+ str(round) + ' ' + game[round])
        values = {'green': 0, 'red': 0, 'blue': 0}

        # Loop through each color shown
        for show in game[round].split(','):
            #print('Show: ' + show)
            
            # Loop through each available color
            for color in colors:
                #print('Color: ' + color)

                if color in show:
                    values[color] = show.replace(color, '')
                    #print('Hit')
                    break

        map.append(values)

    return map

def getMax(game):
    #print(game)
    max = {'green': 0, 'red': 0, 'blue': 0}

    for round in game:
        #print(round)

        for color in round:
            #print(round[color])
            if int(round[color]) > max[color]:
                max[color] = int(round[color])

    return max

def isPossible(game, cubes):

    for color in game:
        if game[color] <= cubes[color]:
            continue
        else:
            return False
    
    return True



for game in readFile(path):

    if isPossible(getMax(convertToMap(game)), cubes):
        result += index
    
    index += 1
 
print(result)