"""
Problem 54

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card:  Highest value card.
One Pair:   Two cards of the same value.
Two Pairs:  Two different pairs.
Three of a Kind:    Three cards of the same value.
Straight:           All cards are consecutive values.
Flush:              All cards of the same suit.
Full House:         Three of a kind and a pair.
Four of a Kind:     Four cards of the same value.
Straight Flush:     All cards are consecutive values of same suit.
Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:

Hand|   Player 1|       Player 2|               Winner
1|5H 5C 6S 7S KD
Pair of Fives|          2C 3S 8S 8D TD
                        Pair of Eights|         Player 2
2|5D 8C 9S JS AC
Highest card Ace|       2C 5C 7D 8S QH
                        Highest card Queen|     Player 1
3|2D 9C AS AH AC
Three Aces|             3D 6D 7D TD QD
                        Flush  with Diamonds|   Player 2

4|4D 6S 9H QH QC
Pair of Queens,Highest card Nine|   3D 6D 7H QD QS
                                    Pair of Queens, Highest card Seven|     Player 1
5|2H 2D 4C 4D 4S
Full House w/Three Fours|   3C 3D 3S 9S 9D
                            Full Housewith Three Threes|                    Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""
import collections
poker = open('problem54/poker.txt','r').read()
poker = poker[0:-1]

test = """5H 5C 6S 7S KD 2C 3S 8S 8D TD
5D 8C 9S JS AC 2C 5C 7D 8S QH
2D 9C AS AH AC 3D 6D 7D TD QD
4D 6S 9H QH QC 3D 6D 7H QD QS
2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"""

card_rank = '__23456789TJQKA'

def total_rank(arr):
    return sum([card_rank.index(c) for c in arr])
def group_by_number(cards):
    # return arr by lengths: [5 of kind, 4 of kind, 3 of kind, pairs, singles]
    counts = collections.Counter(cards)
    groups = sorted([[c]*counts[c] for c in counts] , key = lambda x:len(x),reverse=True)
    return groups


def is_Royal_Flush(h1):
    suits = [c[-1] for c in h1]
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    if len(set(suits)) > 1: return False
    if set(cards) == {'T','J','Q','K','A'}:
        return total_rank(cards)
    return False

def is_straight_flush(h1):
    suits = [c[-1] for c in h1]
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    if len(set(suits)) > 1: return False

    start = card_rank.index(cards[0])
    if ''.join(cards) == card_rank[start:start+5]:
        return total_rank(cards)
    return False

def is_four_kind(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    counts = collections.Counter(cards)
    if max(counts.values()) == 4:
        groups = group_by_number(cards)
        ranks = [total_rank(arr) for arr in groups]
        return tuple(ranks)
    return False

def is_full_house(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    counts = collections.Counter(cards)
    if set(counts.values()) == {3,2}:
        groups = group_by_number(cards)
        ranks = [total_rank(arr) for arr in groups]
        return tuple(ranks)
    return False

def is_flush(h1):
    suits = [c[-1] for c in h1]
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x),reverse=True)
    if len(set(suits)) > 1: return False

    ranks = [card_rank.index(c) for c in cards]
    return tuple(ranks)

def is_straight(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    start = card_rank.index(cards[0])
    if ''.join(cards) == card_rank[start:start+5]:
        return total_rank(cards)
    return False

def is_three_kind(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    counts = collections.Counter(cards)
    if max(counts.values()) == 3:
        groups = group_by_number(cards)
        ranks = [total_rank(arr) for arr in groups]
        return tuple(ranks)
    return False

def is_two_pair(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    counts = collections.Counter(cards)
    if sorted(counts.values()) == [1,2,2]:
        groups = group_by_number(cards)
        ranks = sorted([total_rank(arr) for arr in groups[0:-1]] , reverse=True)
        #check order of pair1 and pair2
        ranks.append(total_rank(groups[-1]))
        return tuple(ranks)
    return False

def is_pair(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x))
    counts = collections.Counter(cards)
    if sorted(counts.values()) == [1,1,1,2]:
        groups = group_by_number(cards)
        pair_rank = [total_rank(groups[0])]
        single_ranks = sorted([total_rank(arr) for arr in groups[1:]] , reverse=True)
        ranks = pair_rank+single_ranks
        return tuple(ranks)
    return False

def is_high_card(h1):
    cards = sorted([c[0:-1] for c in h1], key = lambda x:card_rank.index(x),reverse=True)
    ranks = [card_rank.index(c) for c in cards]
    return tuple(ranks)

def get_hand_rank(h1:list):
    """
    # High Card:  Highest value card.
    # One Pair:   Two cards of the same value.
    # Two Pairs:  Two different pairs.
    # Three of a Kind:    Three cards of the same value.
    # Straight:           All cards are consecutive values.
    # Flush:              All cards of the same suit.
    # Full House:         Three of a kind and a pair.
    # Four of a Kind:     Four cards of the same value.
    # Straight Flush:     All cards are consecutive values of same suit.
    # Royal Flush:        Ten, Jack, Queen, King, Ace, in same suit.
    """
    types = [
        is_Royal_Flush,         # rank 10
        is_straight_flush,
        is_four_kind,
        is_full_house,
        is_flush,
        is_straight,            # rank 5
        is_three_kind,
        is_two_pair,
        is_pair,
        is_high_card            # rank 1
    ]

    for i,func in enumerate(types):
        if func(h1):
            return (10-i, func(h1))

def winning_hand(h1,h2):
    # check hand type first
    t1, r1 =get_hand_rank(h1)
    t2, r2 =get_hand_rank(h2)

    if t1>t2: return 1
    if t1<t2: return 2

    # both same type, go through ranks
    if r1>r2: return 1
    if r1<r2: return 2

def problem54(data):
    data = data.split('\n')
    player1 = 0
    player2 = 0
    for hand in data:
        hand = hand.split()
        h1,h2 = hand[0:5],hand[5:]

        if winning_hand(h1,h2) == 1:
            player1+=1
            print(h1,h2, 'player 1')
        elif winning_hand(h1,h2) == 2:
            player2+=1
            print(h1,h2, 'player 2')

    print(player1,player2)

problem54(poker)
# 376 correct!
