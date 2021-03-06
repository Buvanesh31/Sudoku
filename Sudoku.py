def valid_row(row, grid):
  temp = grid[row]
  temp = list(filter(lambda a: a != 0, temp))

  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1

  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1

def valid_col(col, grid):
  
  temp = [row[col] for row in grid]

  temp = list(filter(lambda a: a != 0, temp))
  
  if any(i < 0 and i > 9 for i in temp):
    print("Invalid value")
    return -1

  elif len(temp) != len(set(temp)):
    return 0
  else:
    return 1


def valid_subsquares(grid):
  for row in range(0, 9, 3):
      for col in range(0,9,3):
         temp = []
         for r in range(row,row+3):
            for c in range(col, col+3):
              if grid[r][c] != 0:
                temp.append(grid[r][c])

         if any(i < 0 and i > 9 for i in temp):
             print("Invalid value")
             return -1

         elif len(temp) != len(set(temp)):
             return 0
  return 1

def valid_board(grid):

  for i in range(9):
      res1 = valid_row(i, grid)
      res2 = valid_col(i, grid)
  
      if (res1 < 1 or res2 < 1):
          print("The board is invalid")
          return
 
  res3 = valid_subsquares(grid)
  if (res3 < 1):
      print("The board is invalid")
  else:
      print("The board is valid")
def print_board(grid):
  for row in grid:
    print(row)

n_rows= 9
n_cols = 9
matrix = [ ]

print("Enter the entries row-wise:")

for i in range(n_rows):          
    a =[ ]
    print("Row:%d" % (i+1))
    for j in range(n_cols):     
         a.append(int(input()))

    matrix.append(a)

print_board(matrix)
valid_board(matrix)
    
board = [[1, 4, 7, 0, 0, 0, 0, 0, 3],
        [2, 5, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 2, 0, 0, 0, 4],
        [0, 0, 0, 4, 1, 0, 0, 2, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 9],
        [4, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 7]]

print_board(board)
valid_board(board)
