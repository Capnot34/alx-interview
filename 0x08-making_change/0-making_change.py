#!/usr/bin/python3
"""
Dynamic Coin Change Algorithm
"""

def makeChange(coins, total):
    """
    Calculates the minimum number of coins needed to reach the total amount.

    Args:
        coins (list): List of available coin denominations.
        total (int): Total amount needed.

    Returns:
        int: Minimum number of coins needed to reach the total, or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    
    coins_used = 0
    amount_checked = 0
    
    coins.sort(reverse=True)
    
    for coin in coins:
        while amount_checked < total:
            amount_checked += coin
            coins_used += 1
    
        if amount_checked == total:
            return coins_used
        
        amount_checked -= coin
        coins_used -= 1
    
    return -1
