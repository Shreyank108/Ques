#Sum of n natural number

# def sum_of_n_natural_number(n): 
#     if n==1 :
#         return 1 
#     return n+sum_of_n_natural_number(n-1) 

# print(sum_of_n_natural_number(10))

#WRITE A RECURSIVE FUNCTION TO PRINT N NATURAL NUMBER  

# def print_n_natural_number(n): 
#     if n ==1 : 
#         return 1        
#     return print_n_natural_number(n-1)  



# nums = [3,2,1,4,5]
# count=0
# i=0 
# while len(nums)!=0 : 
#     if nums[i]+nums[i+1]==nums[i+2]: 
#         count+=1  
#     i+=1  
# print(count) 

words = ["abab","ab"]
p=words[0] 
count=0
for i in words: 
    if p in words: 
        count+=1  
print(count) 