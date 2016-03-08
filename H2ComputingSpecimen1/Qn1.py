filew = open("HIGHEST.txt", 'w')
filew.write('TP 123')
filew.close()

def bestPlayer():
    file = open("HIGHEST.txt", 'r')
    player = file.readline()
    file.close()
    return player

def currHighestScore():
    bestplayer = bestPlayer()
    print(bestplayer)
    if bestplayer[-3] != ' ':
        return int(bestplayer[-3:])
    elif bestplayer[-2] != ' ':
        return int(bestplayer[-2:])
    else:
        return int(bestplayer[-1])

print(currHighestScore())

def scoreReading():
    numberOfPlayers = int(input("How many players do you want to input?"))
    curr = 0
    while curr != numberOfPlayers:
        player = input("Input player name: ")
        score = int(input("Input player score: "))
        if score > currHighestScore():
            filew = open("HIGHEST.txt", 'w')
            filew.write(player+' '+str(score))
            print(currHighestScore())
            
        else:
            print(player+" has not beat the current highest score of",currHighestScore(),". Try again!")
        curr += 1

scoreReading()
