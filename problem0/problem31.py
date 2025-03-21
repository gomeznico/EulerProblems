"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?
"""

## how many ways to sum up to 200 given 1,2,5,10,10,50,100,200

## for 1p, thers only 1 way
# for 2p, there are 2 ways (2p and 2x1p)
# for 3p, there is 1 way

coins = (10,5,2,1)
amount = 10
def num_combinations(coins,amount,memo={}):
    key = (amount,coins)
    if key in memo: return memo[key]
    if amount == 0: return 1

    # memmo stores num of combinations for given coin and money amount
    combinations = []
    if len(coins) == 1:
        num = amount//coins[0]
        combo =[(coins[0],num)]
        ans = 1
    elif coins[0]>amount:
        remaining_coins = coins[1:]
        ans = num_combinations(remaining_coins,amount,memo)
    else:
        ## add 1st coin to 'count', adjust amount, recurse
        ## or
        ## get remaining posibilities without anymore of the fist coin, but same amount
        coin1=coins[0]
        ans1 = num_combinations(coins,amount-coin1,memo)
        ans2 = num_combinations(coins[1:],amount,memo)
        ans = ans1+ans2

    memo[key] = ans
    # print(memo)
    return ans

print(num_combinations(coins,amount))       # 293 for dollar and us coins



coins = (100,50,25,10,5,1)
amount = 100
print(num_combinations(coins,amount))       # 293 for dollar and us coins

coins = (200,100,50,20,10,5,2,1)
amount = 200
print(num_combinations(coins,amount))
