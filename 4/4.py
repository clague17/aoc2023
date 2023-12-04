


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



def main():
    inputFile = open('input.txt', 'r')
    scores = []
    scores = 0
    for line in inputFile:
        [card, hand] = line.split(': ')[1].split(' | ')
        [matches, points] = score_card(card.split(), hand.split())
        scores += points
    return scores

print(main())
