#!/usr/bin/python3
def rotate_2d_matrix(matrix):
  """
  Rotate a 2D matrix 90 degrees clockwise
  """
  # Transpose the matrix
  n = len(matrix)
  transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]

  # Reverse each row
  rotated = [row[::-1] for row in transposed]

  return rotated
