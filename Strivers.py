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
# def factorial(n): 
#     if n ==1 or n ==0  : 
#         return 1  
#     result =1   
#     for i in range(2,n+1): 
#         result *=i               
#     return result   

# def ncr(row,col): 
#      return factorial(row)// (factorial(col)*factorial(row-col)) 

# row=5   
# col=3
# print(ncr(row-1,col-1))

# Type -2    - print whole column  of Triangle     

# def facto(n): 
#     if n ==0 or n ==1  : 
#         return 1   
#     result =1  
#     for i in range(2,n+1): 
#         result *=i   
#     return result   

# def ncr(row,col ): 
#     return facto(row)//(facto(col)*facto(row-col)) 

# def PrintWholeCol(row): 
#     row= row-1 
#     for col in range(row+1): 
#         print(ncr(row,col), end=" ") 
#     print() 

# row=3    
# print(PrintWholeCol(row))
    
# Type 3 - where we have to print whole triangle     

# def facto (n): 
#     if n ==0 or n==1  : 
#         return 1   
#     result =1    
#     for i in range(2,n+1): 
#         result *=i     
#     return result    

# def ncr (row, col): 
#     return facto(row)//(facto(col)*facto(row-col)) 

# def PrintFullTriangle(rows): 
#     triangle  =[]
#     for row in range(rows): 
#         current_col=[] 
#         for col in range(row+1 ): 
#             current_col.append(ncr(row,col))
#         triangle.append(current_col) 
#     return triangle

# row =5  
# print(PrintFullTriangle(row)) 


# ----------------- QUE 3 --------------------------------------------------------------- 
# def nextPermutation(self, nums: List[int]) -> None:
#     n = len(nums)
#     i = n - 2
    
    # Step 1: Find the breakpoint
    # while i >= 0 and nums[i] >= nums[i + 1]:
    #     i -= 1
    
    # if i >= 0:
    #     # Step 2: Find the smallest element larger than nums[i]
    #     j = n - 1
    #     while nums[j] <= nums[i]:
    #         j -= 1
    #     # Swap nums[i] and nums[j]
    #     nums[i], nums[j] = nums[j], nums[i]
    
    # # Step 3: Reverse the subarray to the right of i
    # nums[i + 1:] = reversed(nums[i + 1:])


# def maxSubArray(self, nums: List[int]) -> int:
#     sumation = 0   
#     n= len(nums) 
#     maximum = float("-inf") 
#     for i in range(0,n):  
#         sumation += nums[i]
#         if nums[i] > maximum : 
#             maximum= nums[i] 
#         if sumation > maximum:  
#             maximum = sumation   
#         if sumation < 0: 
#             sumation =0   
#     return maximu

# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]] 

for i in range(len(matrix)): 
    for j in range(i+1,len(matrix)): 
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 

for i in matrix: 
    i.reverse()
    
print(matrix)