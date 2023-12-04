


'''
For Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
card is 41 48 83 86 17, hand is 83 86  6 31 17  9 48 53
'''
def score_card(card, hand):
    matches = -1
    points = 0
    for hand_num in hand:
        for card_num in card:
          if eval(hand_num) == eval(card_num):
            matches += 1
    if matches == -1:
      points = 0
    else: 
      points = pow(2, matches)
    return matches, points

'''
Returns the number of matches
'''
def process_card(card, hand):
  matches = 0
  for hand_num in hand:
    for card_num in card:
        if eval(hand_num) == eval(card_num):
            matches += 1
  return matches

def main():
    inputFile = open('input.txt', 'r')
    matches = []
    totalCards = []
    for line in inputFile:
        totalCards.append(1)
        [card, hand] = line.split(': ')[1].split(' | ')
        cardList = card.split()
        handList = hand.split()
        number = process_card(cardList, handList)
        matches.append(number)
    for i in range(len(totalCards)):
      nextCards = matches[i]
      copies = totalCards[i]
      # populate the next cards
      for j in range(i + 1, len(totalCards)):
        if nextCards == 0:
          break
        totalCards[j] += copies
        nextCards -= 1
    return sum(totalCards)

print(main())
