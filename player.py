# each has 27 cards
# 14's are aces, 15's are jokers
# starts from the front, cards are added to back with the card that was won inserted first
firstPlayer = [12, 12, 12, 12, 15, 15, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 13, 13, 13, 13]
secondPlayer = [2, 2, 2, 2, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 3, 3, 11, 11, 11, 11, 14, 14, 14, 14, 15, 15]

while True:

    # checks if a player won already
    if len(firstPlayer) == 0:
        print('Second Player Wins!')
        break
    elif len(secondPlayer) == 0:
        print('First Player Wins!')
        break

    # playing the cards
    cardsPlaying = [firstPlayer[0], secondPlayer[0]]
    del firstPlayer[0]
    del secondPlayer[0]
    # if cards are the same
    if cardsPlaying[0] == cardsPlaying[1]:
        i = 0
        while True:
            if len(firstPlayer) > 4:
                print('Second Player Wins!')
                break
            elif len(secondPlayer) > 4:
                print('First Player Wins!')
                break
            # counter for iteration number
            if i == 0:
                i += 1
            else:
                i += 2
            for x in range(0, 4):
                cardsPlaying.append(firstPlayer[0])
                del firstPlayer[0]
            for y in range(0, 4):
                cardsPlaying.append(secondPlayer[0])
                del secondPlayer[0]
            if i == 1:
                if cardsPlaying[5] == cardsPlaying[9]: # if the last card in the tie for both players is also the same
                    continue
                elif cardsPlaying[5] > cardsPlaying[9]:
                    firstPlayer.extend(reversed(cardsPlaying))
                    cardsPlaying.clear()
                    break
                else:
                    secondPlayer.extend(cardsPlaying)
                    cardsPlaying.clear()
                    break
            else:
                if cardsPlaying[i * 4 + 5] == cardsPlaying[i * 4 + 9]:
                    continue
                elif cardsPlaying[i * 4 + 5] > cardsPlaying[i * 4 + 9]:
                    firstPlayer.extend(reversed(cardsPlaying))
                    cardsPlaying.clear()
                    break
                else:
                    secondPlayer.extend(cardsPlaying)
                    cardsPlaying.clear()
                    break
        break
    elif cardsPlaying[0] > cardsPlaying[1]:
        firstPlayer.extend(reversed(cardsPlaying))
        cardsPlaying.clear()
    else:
        secondPlayer.extend(cardsPlaying)
        cardsPlaying.clear()


