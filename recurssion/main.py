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

# class Solution:
#     def maximumStrongPairXor(self, nums: List[int]) -> int:
#         maxXor = 0
#         n = len(nums)
#         for start in range(n):
#             for end in range(start, n):
#                 x = nums[start]
#                 y = nums[end]
#                 if abs(x-y) <= min(x,y) and x^y > maxXor:
#                     maxXor = x^y
#         return maxXor



# Input:
# nums = [1,2,1,3,2,5]
# # Output: [3,5] 
# p={}
# for i in nums: 
#     if i in p: 
#         p[i]+=1  
#     else : 
#         p[i]=1   
# k=[] 
# for key,value in p.items(): 
#     if value <2: 
#             k.append(key) 
# print(k)     

# s1 = "this apple is sweet"
# s2 = "this apple is sour"
# spliteds1 = s1.split()
# s2splited = s2.split()
# new_word = spliteds1 + s2splited
# p = {}

# for i in new_word:
#     if i not in p:
#         p[i] = 1  
#     else:
#         p[i] += 1  

# print(p) 
# l=[]
# for key,value in p.items():  
#     if value <2: 
#         l.append(key)  
# print(l) 
        
 
# # Input: 
# nums = [10,2]
# # Output: "210" 
# s="" 
# l=[]
# for i in nums: 
#     s+=str(i) 
# print(s)
# print(s)  
# for i in s: 
#     l.append(int(i)) 
# print(l)
# l.sort() 
# l=l[::-1]
# m=""
# for i in l: 
#     m+=str(i)[::-1]             
# print(m)


# class Solution:
#     def diffWaysToCompute(self, s: str) -> List[int]:
#         def dfs(i, j):
#             if i == j:
#                 return [int(s[i])]
#             if i == j - 1 and s[j] not in '+-*':
#                 return [int(s[i: j + 1])]
#             if (i, j) in memo:
#                 return memo[(i, j)]
#             res = []
#             for k in range(i, j + 1):
#                 ch = s[k]
#                 if ch in '+-*':
#                     left = dfs(i, k - 1)
#                     right = dfs(k + 1, j)
#                     for l1 in left:
#                         for l2 in right:
#                             if ch == '+':
#                                 res += [l1 + l2]
#                             elif ch == '-':
#                                 res += [l1 - l2]
#                             elif ch == '*':
#                                 res += [l1 * l2]
#             memo[(i, j)] = res
#             return memo[(i, j)]
#         n = len(s)
#         memo = dict()
#         return dfs(0, n - 1)
 
# class Solution:
#     def shortestPalindrome(self, s: str) -> str:
#         count = self.kmp(s[::-1], s)
#         return s[count:][::-1] + s
#     def kmp(self, txt: str, patt: str) -> int:
#         new_string = patt + '#' + txt
#         pi = [0] * len(new_string)
#         i = 1
#         k = 0
#         while i < len(new_string):
#             if new_string[i] == new_string[k]:
#                 k += 1
#                 pi[i] = k
#                 i += 1
#             else:
#                 if k > 0:
#                     k = pi[k - 1]
#                 else:
#                     pi[i] = 0
#                     i += 1
#         return pi[-1]
# class Solution:
#     def getReqNum(self, a, b, n):
#         gap = 0
#         while a <= n:
#             gap += min(n + 1, b) - a
#             a *= 10
#             b *= 10
#         return gap

#     def findKthNumber(self, n: int, k: int) -> int:
#         num = 1
#         i = 1
#         while i < k:
#             req = self.getReqNum(num, num + 1, n)
#             if i + req <= k:
#                 i += req
#                 num += 1
#             else:
#                 i += 1
#                 num *= 10
#         return num


# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Consultation Form</title>
#     <link rel="preconnect" href="https://fonts.googleapis.com">
# <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
# <link href="https://fonts.googleapis.com/css2?family=Italiana&display=swap" rel="stylesheet">
#     <link rel="stylesheet" href="style.css">
# </head>
# <body>
#     <div id="main">
#         <header>
#             <h1>Book a Consultation</h1>
#         </header>  
#         <div id="extra">
#             <div class="border">
#                 <div class="box">
#                     <video autoplay loop muted src="/assets/reels/reel2.mp4"></video>
#                 </div>
#             </div> 
#             <div class="form">
#                 <form action="#" method="POST">
#                     <div class="form-group">
#                         <label for="name">Full Name:</label>
#                         <input type="text" id="name" name="name" placeholder="Enter your full name" required>
#                     </div>
#                     <div class="form-group">
#                         <label for="email">Email Address:</label>
#                         <input type="email" id="email" name="email" placeholder="Enter your email" required>
#                     </div>
#                     <div class="form-group">
#                         <label for="phone">Phone Number:</label>
#                         <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
#                     </div>
#                     <div class="form-group">
#                         <label for="date">Preferred Date:</label>
#                         <input type="date" id="date" name="date" required>
#                     </div>
#                     <div class="form-group">
#                         <label for="time">Preferred Time:</label>
#                         <input type="time" id="time" name="time" required>
#                     </div>
#                     <div class="form-group">
#                         <label for="message">Additional Information:</label>
#                         <textarea id="message" name="message" rows="4" placeholder="Enter any additional information or questions"></textarea>
#                     </div>
#                     <button type="submit" class="submit-btn">Submit</button>
#                 </form>
#             </div>
#         </div>
#     </div>
# </body>
# </html>
