path = './input_data.txt'

def readFile (path):
    lines = []

    with open(path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    return lines

def splitCards (cards):
    cardsList = []

    for card in cards:
        split = card.split(':')[1].split('|')
        cardsList.append({"win": list(filter(None, split[0].split(' '))), "numbers": list(filter(None, split[1].split(' ')))})

    return cardsList

def findHits (card):
    hits = 0

    for number in card['numbers']:
        if number in card['win']:
            hits += 1

    return hits

def getScore (cards):
    score = 0

    for card in cards:
        hits = findHits(card)

        if hits != 0:
            score += 2 ** (hits - 1)

    return score



cards = splitCards(readFile(path))

print("Part 1 result: " + str(getScore(cards)))