#!/usr/bin/python3

# Constants - These constants will help improve the readability of your code
SHELDON = "Sheldon"
LEONARD = "Leonard"

LEONARD_WINS = 0
SHELDON_WINS = 1
TIE = 2

ROCK = 0
PAPER = 1
SCISSORS = 2
LIZARD = 3
SPOCK = 4

# Variables - Use these variables in your code to track the program's progress
leonardsShape = 0
sheldonsShape = 0 
roundsToPlay = 0

leonardsWinCount = 0
sheldonsWinCount = 0
tieCount = 0

def convertShapeToText(shape):
    choices = {ROCK : "Rock", PAPER : "Paper", SCISSORS : "Scissors", LIZARD : "Lizard", SPOCK : "Spock"}
    return choices.get(shape, "default")

# =======================================================================================================
# DO NOT MODIFY any of the code above this point
# ========================================================================================================

# It's OK to change these constants (use the shape names above - ROCK, SCISSORS, PAPER, LIZARD, SPOCK)
# See the Initial Values in the provided examples
SHELDONS_FIRST_SHAPE = SPOCK
LEONARDS_FIRST_SHAPE = ROCK
NUMBER_OF_ROUNDS = 4

def determineLeonardsNextShape(roundOutcome):
    global leonardsShape
    if roundOutcome == LEONARD_WINS:
        leonardsShape = leonardsShape
    elif roundOutcome == SHELDON_WINS:
        leonardsShape = getBetterShape(sheldonsShape)
    elif roundOutcome == TIE:
        leonardsShape = getBetterShape(leonardsShape)
    return leonardsShape

def determineSheldonsNextShape(roundOutcome):
    global sheldonsShape, roundsToPlay, roundCount
    for i in range(0, roundsToPlay, 2):
        if roundCount == i:
            sheldonsShape = SPOCK
            roundCount = roundCount + 1
        else:
            if roundOutcome == SHELDON_WINS:
                sheldonsShape = ROCK
                roundCount = roundCount + 1
            elif roundOutcome == LEONARD_WINS:
                sheldonsShape = PAPER
                roundCount = roundCount + 1
            elif roundOutcome == TIE:
                sheldonsShape = LIZARD
                roundCount = roundCount + 1
        return sheldonsShape, roundCount

def determineWinner():
    if leonardsShape == ROCK and sheldonsShape == SCISSORS:
        outcome = LEONARD_WINS
    elif leonardsShape == ROCK and sheldonsShape == LIZARD:
        outcome = LEONARD_WINS
    elif leonardsShape == PAPER and sheldonsShape == ROCK:
        outcome = LEONARD_WINS
    elif leonardsShape == PAPER and sheldonsShape == SPOCK:
        outcome = LEONARD_WINS
    elif leonardsShape == SCISSORS and sheldonsShape == PAPER:
        outcome = LEONARD_WINS
    elif leonardsShape == SCISSORS and sheldonsShape == LIZARD:
        outcome = LEONARD_WINS
    elif leonardsShape == LIZARD and sheldonsShape == SPOCK:
        outcome = LEONARD_WINS
    elif leonardsShape == LIZARD and sheldonsShape == PAPER:
        outcome = LEONARD_WINS
    elif leonardsShape == SPOCK and sheldonsShape == SCISSORS:
        outcome = LEONARD_WINS
    elif leonardsShape == SPOCK and sheldonsShape == ROCK:
        outcome = LEONARD_WINS
    elif sheldonsShape == ROCK and leonardsShape == SCISSORS:
        outcome = SHELDON_WINS
    elif sheldonsShape == ROCK and leonardsShape == LIZARD:
        outcome = SHELDON_WINS
    elif sheldonsShape == PAPER and leonardsShape == ROCK:
        outcome = SHELDON_WINS
    elif sheldonsShape == PAPER and leonardsShape == SPOCK:
        outcome = SHELDON_WINS
    elif sheldonsShape == SCISSORS and leonardsShape == PAPER:
        outcome = SHELDON_WINS
    elif sheldonsShape == SCISSORS and leonardsShape == LIZARD:
        outcome = SHELDON_WINS
    elif sheldonsShape == LIZARD and leonardsShape == SPOCK:
        outcome = SHELDON_WINS
    elif sheldonsShape == LIZARD and leonardsShape == PAPER:
        outcome = SHELDON_WINS
    elif sheldonsShape == SPOCK and leonardsShape == SCISSORS:
        outcome = SHELDON_WINS
    elif sheldonsShape == SPOCK and leonardsShape == ROCK:
        outcome = SHELDON_WINS
    else:
        outcome = TIE
    return outcome

def getBetterShape(shape):
    if shape == ROCK:
        leonardsShape = SPOCK
    elif shape == PAPER:
        leonardsShape = LIZARD
    elif shape == SCISSORS:
        leonardsShape = SPOCK
    elif shape == LIZARD:
        leonardsShape = SCISSORS
    elif shape == SPOCK:
        leonardsShape = LIZARD
    return leonardsShape

# =======================================================================================================
# DO NOT MODIFY any of the code below this point
# =======================================================================================================	
def displayResults():
    print("{0}'s initial move: {1}\n{2}'s initial move: {3}\n\n".format(SHELDON, convertShapeToText(SHELDONS_FIRST_SHAPE), LEONARD, convertShapeToText(LEONARDS_FIRST_SHAPE)))
    if sheldonsWinCount > leonardsWinCount:
        print("{0} wins! ".format(SHELDON))
    elif leonardsWinCount > sheldonsWinCount:
        print("{0} wins! ".format(LEONARD))
    else:
        print("Tie Game!")
    if not sheldonsWinCount == leonardsWinCount:
        print("{0} won {1} game(s), {2} won {3} game(s), and they tied {4} game(s)\n".format(SHELDON, sheldonsWinCount, LEONARD, leonardsWinCount, tieCount))
    else:
        print("{0} and {1} each won {2} game(s) and tied {3} game(s)\n".format(SHELDON, LEONARD, sheldonsWinCount, tieCount))

def playGame():
    global leonardsShape, sheldonsShape

    for x in range(0, roundsToPlay):
        outcome = determineWinner()
        updateScores(outcome)
        leonardsShape = determineLeonardsNextShape(outcome)
        sheldonsShape = determineSheldonsNextShape(outcome)

def updateScores(roundOutcome):
    global leonardsWinCount, sheldonsWinCount, tieCount

    if roundOutcome == SHELDON_WINS:
        sheldonsWinCount = sheldonsWinCount + 1
    elif roundOutcome == LEONARD_WINS:
        leonardsWinCount = leonardsWinCount + 1
    else:
        tieCount = tieCount + 1

def main():
    print("Hayley Lewter\nRock-Paper-Scissors-Lizard-Spock\n")
    playGame()
    displayResults()

leonardsShape = LEONARDS_FIRST_SHAPE
sheldonsShape = SHELDONS_FIRST_SHAPE
roundsToPlay = NUMBER_OF_ROUNDS
roundCount = 1

main() # This must be the LAST statement of the program (DO NOT INDENT)