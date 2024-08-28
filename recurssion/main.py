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

# words = ["abab","ab"]
# p=words[0] 
# count=0
# for i in words: 
#     if p in words: 
#         count+=1  
# print(count)  

# l=[7,2,5,3,1] 
# max =l[0] 
# second_max =l[0]
# for i in l: 
#     if i>max: 
#         second_max=max  
#         max = i  
        
#     if second_max > max : 
#             second_max= max
# print(max)
# print(second_max) 

# finding second max element 
# l = [7, 2, 5, 3, 1]
# max_value = l[0]
# second_max = l[0]

# for i in l:
#     if i > max_value:
#         second_max = max_value  
#         max_value = i  
#     elif i > second_max :
#         second_max = i  

# print("Max:", max_value)
# print("Second Max:", second_max)

# l = [7, 2, 5, 3, 1]



#......?
#second approch  
# l.sort(reverse=True) 
# print(l[1]) 

# l=[3,5,4,2,6,7,8] 
# max_value= float("_inf")
# Secondmax_value= float("_inf") 

# for i in l: 
#     if i > max_value : 
#         Secondmax_value = max_value 
#         max_value =i  
#     elif i > Secondmax_value and i !=max_value : 
#         Secondmax_value= i 


# l=[2,1,5,6,3]
# n=6
# count =0   
# for i in l: 
#     count +=i              
# p= n*(n+1)/2  
# print(int(p-count))       

# s1= "shreyank" 
# s2="hrenkyas" 
# p=sorted(s1)
# p1=sorted(s2) 
# if p==p1: 
#     print("Anagrams") 
# else : 
#     print("not Anagram")  

# n=5   
# op =12345   

# n=4  
# op=1234    

# for i in range(1,n+1): 
#     print(i,end="") 

# result=0
# for i in range(1,n+1): 
#     result = result*10+i              
# print(result)





# multiply two number   
# count=0
# a=int(input("enter 1st number")) 
# b=int(input("enter 2st number"))  
# for i in range(a):
#         count+=b          
# print(count)

# divide two number   

# count = 0
# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))

# while a >= b:
#     a = a - b
#     count += 1

# print("Quotient:", count)
# print("Remainder:", a)