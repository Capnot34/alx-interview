#!/usr/bin/python3

def minOperations(n):
  """
  This function calculates the minimum number of operations needed to achieve
  exactly n 'H' characters in a text file.

  Args:
      n: The target number of 'H' characters.

  Returns:
      The minimum number of operations required, or 0 if it's impossible.
  """
  if n <= 0:
    return 0

  operations = 0
  current_count = 1

  while current_count < n:
    if current_count % 2 == 0:
      # Double the characters if count is even
      current_count *= 2
      operations += 1
    else:
      # Paste once for odd count
      current_count += 1
      operations += 1

  return operations
