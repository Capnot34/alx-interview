#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total != 0:
        return -1
    return count
