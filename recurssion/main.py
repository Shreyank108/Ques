#Sum of n natural number

# def sum_of_n_natural_number(n): 
#     if n==1 :
#         return 1 
#     return n+sum_of_n_natural_number(n-1) 

# print(sum_of_n_natural_number(10))

#WRITE A RECURSIVE FUNCTION TO PRINT N NATURAL NUMBER  

def print_n_natural_number(n): 
    if n ==1 : 
        return 1        
    return print_n_natural_number(n-1) 
