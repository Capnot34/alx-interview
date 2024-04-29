#!/usr/bin/python3
def rotate_matrix(matrix):
  """
  Rotate a 2D matrix 90 degrees clockwise
  """
  # The number of layers is half the length of the matrix
  n = len(matrix)
  layers = n // 2

  for layer in range(layers):
    first = layer
    last = n - layer - 1
    for i in range(first, last):
      # Save top element
      top = matrix[layer][i]

      # Move left to top
      matrix[layer][i] = matrix[-i - 1][layer]

      # Move bottom to left
      matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

      # Move right to bottom
      matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

      # Move saved top to right
      matrix[i][-layer - 1] = top

  return matrix
