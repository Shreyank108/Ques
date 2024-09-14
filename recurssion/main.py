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


# for i in range(1,n+1): 
#     result =result*10+i           
# print(result)


# multiply two number   
# count=0
# a=int(input("enter 1st number")) 
# b=int(input("enter 2st number"))  
# for i in range(a):
#         count+=b          
# print(count)

# divide two number   

# l=[4,3,-7,0,2,3,1,-3,6,0] 
# sum = 0   
# maximum = float("-inf") 
# for i in range(0,len(l)):  
#     sum += l[i]
#     if l[i]>maximum:
#         maximum = l[i]
#     if sum > maximum: 
#         maximum =sum  
#     if sum < 0: 
#         sum =0  
# print(sum)
# print(maximum)
    
 
# a="shsrteeyaank" 
# l=[]
# for i in a: 
#     l.append(i) 
# print(l)
# p={}
# for i in l: 
#     if i in p: 
#         p[i]+=1   
#     else : 
#         p[i]=1  
# print(p) 
# m=[]
# s=""
# for  key,value in p.items(): 
#     print (key ,"occurs", value) 
# for i , j in p.items(): 
#     if j==1 : 
#         s+=i   
# print(s)


# l=[1,1,2,3,2,3,4,3,]  
# p={} 
# for i in l: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1 
# print(p)
# for key,value in p.items(): 
#    k= max(p.values()) 
# print(k)     
 
# Input:
# s = "zbax"
# k = 2

# # Mapping of letters to their corresponding positions in the alphabet
# p = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
#     'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
#     'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
# }

# converted_num = ""
# for i in s:
#     converted_num += str(p[i])
    
# print("Converted String to Number:", converted_num)

# for j in range(k):
#     current_sum = sum(int(digit) for digit in converted_num)

#     converted_num = str(current_sum)
#     print(f"After transformation {j+1}: {converted_num}")

# print("Final Output:", converted_num) 


# nums = [2,1,3,5,6]
# k = 5
# multiplier = 2

# for i in range(k): 
#     p=min(nums)
#     m=p*multiplier 
#     l=nums.index(p) 
#     nums[l] = m
# print(nums)

# word1= "abc" 
# word2="pq"
# c="" 
# if len(word1)>len(word2): 
#     for i in range(len(word1)-1): 
#         c+=word1[i]+word2[i] 
# print(c)
 
# n = 13
# k = 4 
# p=bin(n) 
# p2=bin(k) 
# print(int(p+p2))


# a='abc' 
# b='pqr' 
# # c=""
# # for i in range(max(len(a),len(b))): 
# #     c+=a[i]+b[i]
# # print(c)
# p=[] 
# for i in range(2*len(a),2): 
#     p.append(a[i]) 
# print(p) 

# Input:

# nums = [7,8,3,4,15,13,4,1]
# new = []

# while len(nums) > 1: 
#     nums.sort() 
#     maxi = nums[-1] 
#     mini = nums[0] 
#     avg = (maxi + mini) / 2  # Use / for floating-point division
#     new.append(avg) 
#     nums.remove(maxi)
#     nums.remove(mini)

# # If there's one element left, calculate the average of the remaining number
# if len(nums) == 1:
#     new.append(nums[0])

# # Compute the final average of the averages in the new list
# final_avg = sum(new) / len(new)
# print(final_avg)


# grid = [[1],[2],[3]] 
# flag = False
# for i in range(len(grid)-1): 
#     if grid[i] == grid[i+1] : 
#         flag =True
#     else : 
#         flag =False                      
# if flag == False : 
#     print(False) 
# else : 
#     print(True)


# k = 6 
# l=[2,12,1,11,4,5]

# count =0
# for i in l:  
#     p=bin(i)[2:] 
#     count+=int(p,2)
# print(count) 


# s="Hello i am Shreyank" 
# p=s.split(" ") 
# print(" ".join(p[::-1]))  

# s="Hello i am Shreyank"  
# p=s.split(" ")
# k=[]
# for i in p: 
#     m=i[::-1]
 
#     k.append(m) 
# print(" ".join(k)) 

# s="Hello i am Shreyank"   
# p=s.split(" ")
# k=[]
# for i in p: 
#     m=i[::-1]
    
#     k.append(m) 
# print(" ".join(k[::-1]))


# Input: 
# date = "2024-09-13" 

# p = date.split("-")  
# l = []  

# for i in p:
#     convert_to_binary = bin(int(i))[2:]  
#     l.append(convert_to_binary)

# print("-".join(l))  

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxXor = 0
        n = len(nums)
        for start in range(n):
            for end in range(start, n):
                x = nums[start]
                y = nums[end]
                if abs(x-y) <= min(x,y) and x^y > maxXor:
                    maxXor = x^y
        return maxXor