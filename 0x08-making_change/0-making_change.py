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
    
    # Initialize variables to keep track of total coins used and amount checked
    coins_used = 0
    amount_checked = 0
    
    # Sort the coins in descending order for greedy approach
    coins.sort(reverse=True)
    
    # Iterate through each coin denomination
    for coin in coins:
        # Keep adding coins until the checked amount equals or exceeds the total
        while amount_checked < total:
            amount_checked += coin
            coins_used += 1
        
        # If the checked amount matches the total, return the number of coins used
        if amount_checked == total:
            return coins_used
        
        # Otherwise, backtrack by subtracting the current coin and its count
        amount_checked -= coin
        coins_used -= 1
    
    # If the loop completes without finding a solution, return -1
    return -1
