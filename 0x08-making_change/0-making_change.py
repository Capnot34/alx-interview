#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total.
    
    Args:
        coins (list): List of coin denominations.
        total (int): The target amount.
        
    Returns:
        int: The fewest number of coins needed to meet total, or -1 if total cannot be met.
    """
    if total < 1:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
