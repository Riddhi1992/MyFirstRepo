from authenticate_data import match
import numpy as np

continue_playing = True


def choice():
    global continue_playing
    if match():
        choices = input("Do you want to get in (Yes or No)?: ")
        choices = choices.lower()
        if choices == "yes":
            with open("game_instruction.txt", 'r') as instruction:
                print(instruction.read())

            while True:
                try:
                    y = input("Press 'P', if you want to play the game: ")
                    y = y.lower()
                    if y == 'p':
                        break
                    else:
                        raise Exception("You have entered the wrong choice, Enter 'P' to play.")
                except Exception as a:
                    print(a)

            continue_playing = True

            while continue_playing:
                createMatrix()


def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue

            traverseNode(i, j, matrix, visited, sizes)
    # print(sizes)
    userInput(sizes)
    return sizes


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue

        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors


def userInput(sizes):
    guess = []
    for i in range(len(sizes)):
        x = int(input("Enter your guess for the size of Island: "))
        guess.append(x)

    percentageCheck(sizes, guess)
    # print(guess)
    return guess


def percentageCheck(sizes, guess):
    global continue_playing
    res = len(set(sizes) & set(guess)) / float(len(set(sizes) | set(guess))) * 100
    result = round(res, 2)
    # print(result)
    if result == 100.0:
        print("Congratulations!!! You are the winner.")
    elif 60.0 < result < 90:
        print("You got Second position...")
    else:
        print("Invest more money on Almonds, then come back")

    ask = input("Do you want to play again (Yes or No)? ")
    ask = ask.lower()

    if ask == 'yes':
        continue_playing = True

    elif ask == 'no':
        continue_playing = False


def createMatrix():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    x = input("Enter the entries in a single line (separated by space): ")

    entries = list(map(int, x.split(' ')))
    matrix = np.array(entries).reshape(r, c)
    riverSizes(matrix)
    return matrix, r, c


choice()
