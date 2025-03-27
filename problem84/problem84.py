"""
Problem 84

In the game, Monopoly, the standard board is set up in the following way:



A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""
import random
import time

# board_squares:
# 0 : GO
# ...
# 2, 17, 33 : community chest
# ...
# 7, 22, 36 : chance
# 10 : JAIL
# 20 : Free Parking, n/a
# 30 : G2J





class Game(object):
    def __init__(self, die_size):
        # initialize ch_cards and cc_card
        community_chest_deck = [None]*14 + [0] + [10]
        chance_deck = [None]*6 + [0,10,11,24,39,5,'next R','next R','next U','back 3']
        random.shuffle(chance_deck)
        random.shuffle(community_chest_deck)


        self.die_size = die_size
        self.chance_deck = chance_deck
        self.community_chest_deck = community_chest_deck
        self.pos = 0
        self.doubles_streak = 0

        self.counts = [0]*40
        pass

    def roll_dice(self):
        d1 = random.randint(1,self.die_size)
        d2 = random.randint(1,self.die_size)
        return (d1,d2)

    def community_chest(self):
        ## output is next position if applicable
        ## 16 total cards, onlt 2 change pos
        # Advance to GO     0
        # Go to JAIL        10
        card = self.community_chest_deck.pop(0)
        self.community_chest_deck += [card]

        if card is None : return self.pos
        else: return card

    def chance(self):
        # deck is 16 cards
        # Advance to GO     0
        # Go to JAIL        10
        # Go to C1          11
        # Go to E3          24
        # Go to H2          39
        # Go to R1          5
        # Go to next R (railway company)    [5,15,25,35]
        # Go to next R                      [5,15,25,35]
        # Go to next U (utility company)    [12,28]
        # Go back 3 squares                 [4,19,33]

        card = self.chance_deck.pop(0)
        self.chance_deck += [card]

        if card == None : return self.pos
        elif card == 'next R':
            r = [5,15,25,35]
            # return first r greater than current postion, else return 5
            for i in r:
                if self.pos<i: return i
            return 5
        elif card == 'next U':
            u = [12, 28]
            # return first r greater than current postion, else return 5
            for i in u:
                if self.pos<i: return i
            return 12
        elif card == 'back 3':
            return self.pos-3
        else: return card

    def turn(self):
        dice = self.roll_dice()
        a = 1
        if dice[0]==dice[1]: self.doubles_streak+=1
        else: self.doubles_streak = 0

        if self.doubles_streak == 3:
            #go to jail
            self.doubles_streak=0
            self.pos = 10

        else:
            # move game piece, check for passing go
            self.pos = (self.pos+sum(dice)) % 40

            # go to jail
            if self.pos == 30:
                self.pos = 10
            elif self.pos in [2,17,33]:
                self.pos = self.community_chest()
            elif self.pos in [7,22,36]:
                self.pos = self.chance()
                # ##small chance that this leads to community chest
                if self.pos == 33:
                    self.pos = self.community_chest()

            # end turn
        self.counts[self.pos] +=1

    def play_rounds(self,rounds):
        s = time.time()
        for _ in range(rounds):
            self.turn()
        e = time.time()
        # get most common squares, showing normilized probabilities
        x = 5
        final_counts = sorted([(self.counts[i]*100/rounds,i) for i in range(40)],reverse=True)[0:x]
        print(f"top {x} squares: {final_counts}")
        ans = ''.join([f'{pair[1]:02d}' for pair in final_counts])[0:6]
        print(f'the six-digit modal string is {ans}, found in {e-s:4f} seconds')

rounds = 4_000_000
game_with_6side = Game(6)
game_with_6side.play_rounds(rounds)
# top 5 squares: [(6.2391, 10), (3.1847375, 24), (3.0960625, 0), (3.085325, 19), (3.06825, 25)] found in 6.735854 seconds
# the six-digit modal string is 102400


game_with_6side = Game(4)
game_with_6side.play_rounds(rounds)
# top 4 squares: [(7.0208, 10), (3.6091, 15), (3.2834125, 24), (3.224025, 16)] found in 7.109123 seconds
# the six-digit modal string is 101524



