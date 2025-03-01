# matrix = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]

# row = len(matrix) 
# col = len(matrix[0]) 

# row_zero =set() 
# col_zero = set() 

# for i in range(row): 
#     for j in range(col): 
#         if matrix[i][j] ==0  : 
#             row_zero.add(i) 
#             col_zero.add(j) 

# for i in range(row): 
#     for j in range(col): 
#         if i in row_zero or j in col_zero: 
#             matrix[i][j] =0    
# print(matrix) 


#-------------------------------- PASCALS TRIANGLE --------------------------  
'''
        1
       1  1 
      1  2  1
     1  3  3  1 
    1  4  6  4  1 
   1  5  10 10  5 1
'''
# Type 1   -   which element exists  row 5 col -3 
# formula is ncr  [Combinations ] 
n=int("input") 
