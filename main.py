# Input: 
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8 
# count =0
# c=""
# l=[]
# p=str(grid).replace("[","").replace("]","").replace(" ","")  
# c+=p                           
# for i in c.split(",") : 
#     l.append(int (i)) 
# for i in l: 
#     if i<0: 
#         count +=1  
# print(count)

# count =0
# for i in grid: 
#     for j in i: 
#         if j<0: 
#             count +=1  
# print(count)


# Input:
# date1 = "2020-01-15"
# date2 = "2019-12-31"
# # Output: 1

# from datetime import datetime   

# dt1 =datetime.strptime(date1,"%Y-%m-%d")
# dt2 =datetime.strptime(date2,"%Y-%m-%d")

# delay_time =abs(dt2 - dt1) 

# print(delay_time.days) 


# Input: 
# nums = [1,3,4,2,2]
# # Output: 2
# p={}
# for i in nums: 
#     if i in p: 
#         p[i]+=1  
#     else : 
#         p[i] =1   
# print(p)  

# for key,value in p.items(): 
#     if value>1: 
#         print(key)
    
    
# Input: 
# nums = [8,1,2,2,3]
# # Output: [4,0,1,1,3] 
# m=[] 
# for i in range(len(nums)): 
#     count =0   
#     for j in range(len(nums)): 
#         if nums[i]> nums[j]: 
#             count +=1  
#     m.append(count) 
# print(m) 



# Input: 
# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# # Output: [15]
# # Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column. 

# zipped_matrix = [list(row) for row in zip(*matrix)]
# print(zipped_matrix)
# k=[]
# k2=[]
# for i in zipped_matrix: 
#     k.append(max(i)) 
# print(k)   
# for i in matrix: 
#     k2.append(min(i)) 
# print(k2)  

# print([*set(k).intersection(set(k2))]) 


# # Input: 
# arr = [2,2,3,4]
# # Output: 2
# p={} 
# for i in arr: 
#     if i in p: 
#        p[i]+=1  
#     else : 
#         p[i]=1  
# print(p) 
# l=[]
# m=0
# for key,value in p.items(): 
#     if key == value : 
#         l.append(key)  
#     else:
#         m=-1

# if m==0: 
#     print(max(l))  
# else : 
#     print(-1)



# Input: 
# words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# substring =[] 
# for i in range(len(words)): 
#     for j in range(len(words)): 
#         if i != j and words[i] in words[j]: 
#             substring.append(words[i]) 
# print(substring)

# Input: 
# nums = [1,0,0,0,1,0,0,1] 
# k = 2
# # Output: true
# # Explanation: Each of the 1s are at least 2 places away from each other. 
# l=[]
# for i in range(len(nums)): 
#     if nums[i]==1: 
#         l.append(i) 
# print(l)
# differences = []

# for i in range(0,len(l)-1):
#     diff = l[i + 1] - l[i]
#     differences.append(diff)

# differences.append(-l[-1])

# print(differences)

# Input: 
# s = "abbcccddddeeeeedcba"
# # Output: 5
# l=[]
# for i in s : 
#    l.append(i) 
# print(l)  
# count  =0
# for i in range(len(l)-1): 
#         if l[i] == l[i+1] : 
#             count +=1  
# print(count)    


# Input:
# target = [1,2,3,4]
# arr = [2,4,1,3]
# # Output: true 

# target.sort()  
# arr.sort()
# print(target) 
# print(arr) 
# if target == arr : 
#     print(True) 
# else : 
#     print(False)


# Input:
# nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 
# (indexed from 0), you will get the maximum value, that is, 
# (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.  

# nums.sort(reverse=True) 
# print(nums)
# print((nums[0]-1) * (nums[1]-1))



# Input:
# nums = [2,5,1,3,4,7]
# n = 3
# # Output: [2,3,5,4,1,7] 
# # Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]. 
# l=[] 
# m=[] 
# k=[]
# for i in range(n): 
#     l.append(nums[i]) 
# print(l) 
# for i in range(n,len(nums)): 
#     m.append(nums[i]) 
# print(m)
# i=0 
# while len(k) != len(nums): 
#     k.append(l[i])
#     k.append(m[i])
#     i+=1
# print(k)

# Input: 
# nums = [1,2,3,4]
# # Output: [1,3,6,10]
# # Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# l=[]
# i=0   
# while len(l) != len(nums)-1 : 
#     l.append(nums[1]+nums[i+1]) 
#     i+=1  
# print(l) 

# Input: 
# n = 5
# start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator. 
# l=[]

# for i in range(start,start + n*2,2): 
#     l.append(i)      
# print(l)
# result =0   
# for i in l: 
#     result ^=i           
# print(result)
    
    
    
# def isPathCrossing(path):
#     visited = {(0, 0)}  
#     x, y = 0, 0

#     for direction in path:
#         if direction == 'N':
#             y += 1
#         elif direction == 'S':
#             y -= 1
#         elif direction == 'E':
#             x += 1
#         elif direction == 'W':
#             x -= 1

#         if (x, y) in visited:
#             return True
#         visited.add((x, y))

#     return False

# print(isPathCrossing("NES"))  
# print(isPathCrossing("NESWW")) 



# Input: 
# arr = [1,2,4]
# Output: true
# Explanation: We can reorder the elements as [1,3,5]
# or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements. 
# arr.sort(reverse=True)
# l=[] 
# print(arr)
# for i in range(len(arr)-1): 
#     l.append(arr[i]-arr[i+1]) 
# print(l) 
# flag =0
# p={} 
# for i in l: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# if len(p) ==1 : 
#     print(True) 
# else : 
#     print(False) 



# Input: 
# date = "20th Oct 2052"
# # Output: "2052-10-20"
# p=date.split(" ") 
# months={
#     "Jan" :1 ,
#     "Feb":2,
#     "Mar":3, 
#     "Apr":4,
#     "May":5,
#     "Jun":6,
#     "Jul":7,
#     "Aug":8,
#     "Sep":9,
#     "Oct":10,
#     "Nov":11,
#     "Dec":12}
# print(p)
# val=0
# for key,value in months.items(): 
#     if key == p[1]: 
#         val+=value 
# print(val) 
# d_p=[]
# for i in p[0]: 
#     d_p.append(i) 
# print(d_p) 
# d_p=d_p[:-2] 
# join_d_p= "".join(d_p) 
# print(join_d_p) 


# Input: 
# low = 8
# high = 10
# # Output: 3
# # Explanation: The odd numbers between 3 and 7 are [3,5,7]. 
# count  =0  
# for i in range(low,high+1): 
#     if i%2 !=0 : 
#         print(i)
#         count +=1 
# print(count)


# Input: 
# arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.


# Input: 
# nums = [1,1,2,3,3,4,4,8,8]
# Output: 2 
# p={}
# for i in nums: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# print(p) 
# for key,value in p.items(): 
#     if value==1: 
#         print(key)

# result =0  
# for i in nums: 
#     result^=i     
# print(result)

# Input: 
# arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

# for i in range(len(arr)-2): 
#     if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0 : 
#         print("true") 
#     else : 
#         print("false")

# def threeConsecutiveOdds(arr):
#     # Iterate through the array up to the third-last element
#     for i in range(len(arr) - 2):
#         # Check if the current element and the next two elements are all odd
#         if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
#             return True
#     return False

# # Example test cases
# print(threeConsecutiveOdds([2, 6, 4, 1]))  # Output: False
# print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))  # Output: True


# Example 1:
# Input: 
n = 1345987
# Output: "987"
# Example 2:

# Input: n = 1234
# Output: "1.234" 

# formatted_str = '{:,}'.format(n) 
# print(formatted_str)
# # Replace commas with dots
# result = formatted_str.replace(',', '.')
# print(result)

# Input: 
# s = "?zs"
# # Output: "azs" 
# l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# p=[]
# for i in l: 
#     if i not in s: 
#         p.append(i) 
# print(p)  
# m=s.replace('?',p[0])   
# print(m)

# Input: 
# s = "()(())((()()))" 



# arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# Max = max(arr)
# Min = min(arr) 
# arr.remove(Max)
# arr.remove(Min) 
# len=len(arr) 
# sum=0 
# for i in arr: 
#     sum+=i   
# print(sum/len) 

# Input: 
# s = "abca"
# # Output: 2
# # Explanation: The optimal substring here is "bc". 
# l=[]
# for i in s: 
#     l.append(i) 
# print(l)
# p={} 
# for i in l: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1 
# print(p) 
# key= 0
# for key,value in p.items(): 
#     if value ==2: 
#         key+=key



# Input: 
# nums = [1,1,2,2,2,3]
# # Output: [3,1,1,2,2,2]
# # Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.    
# p={}
# for i in nums: 
#    if i in p: 
#        p[i]+=1 
#    else : 
#        p[i] =1 
# print(p)  
# l=[] 
# for key,value in p.items(): 
#     l.append(value) 
# l.sort() 
# print(l) 
# for i in l: 
    
# Input: 
# s = "daabcbaabcbc"
# part = "abc"
# # Output: "dab" 
# p=""
# for i in s:
#     if part in s: 
#         p=s.replace(part,"") 
# print(p)

# Input: 
# s = "abbaca"
# # Output: "ca" 
# i=0
# while s[i]==s[i+1]:  
#     s.replace()
#     i+=1 

# Input: 
# arr = [15,88]
# pieces = [[88],[15]]
# # Output: true
# # Explanation: Concatenate [15] then [88] 
# count =0
# l=[]
# for i in str(pieces): 
#     l.append(i) 
# for i in l: 
#     if '[' == i: 
#         count +=1 
# if count >= len(arr): 
#     print(True) 
# else : 
#     print(False)


# Input: 
# word1 = ["ab", "c"]
# word2 = ["a", "bc"] 

# word_parse="".join(word1)
# word_parse2="".join(word2)  
# if word_parse == word_parse2 : 
#     print(True) 
# else : 
#     print(False)


# Input: 
# sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
# word = "aaaba"

# count = 0
# index = sequence.find(word)

# while index != -1:
#     count += 1
#     index = sequence.find(word, index + 1)

# print(count) 

# Input: 
accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
# l=[] 
# for i in accounts: 
#    l.append(sum(i)) 
# print(max(l)) 

# OR   

# accounts = [[1,2,3],[3,2,1]] 
# l=[] 
# for i in accounts: 
#     count =0  
#     for j in i: 
#         count+=j   
#         l.append(count) 
# print(l)
# print(max(l)) 


# Input: 
# command = "G()()()()(al)"
# # Output: "Gooooal"
# p=command.replace("()",'o').replace('(al)','al')
# print(p)

# Input: 
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# # Output: 2 
# count =0
# for i in allowed: 
#     print(i)
#     for j in words: 
#         if i in j:
#             count +=1 
# print(count)



# Input: 
# nums = [1,2,3]
# # Output: true
# # Explanation: [1,2,3,4,5] is the original sorted array.
# # You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2]. 
# p=nums[:]
# print(p)
# nums.sort() 
# print(nums) 
# #[1,2,3,4,5]
# #[3,4,5,1,2]  
# l=[] 
# for _ in range (len(nums)):
#     last_elem=nums[-1] 
#     for i in range(len(nums)-1,0,-1):  
#         nums[i]=nums[i-1] 
#     nums[0]=last_elem  
#     l.append(nums[:]) 
# print(l) 
# flag=False
# for i in l: 
#     if i== p: 
#         flag =True
#         break
# if flag ==True: 
#     print(True) 
# else : 
#     print(False)



# Input: 
# s = "YazaAay"
# # Output: "aAa"
# # Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# # "aAa" is the longest nice substring. 
# l=[]
# for i in s :  
#     l.append(i) 
# print(l) 
# for i in range(len(l)): 
#     if l[i].isupper(): 
#         if l[i+1]==l[i].islower() or l[i-1]==l[i].islower(): 
#             print(True)

# Input: 
# word1 = "abc"
# word2 = "pqr"
# # Output: "apbqcr" 
# word3=[] 
# word1_list=[]
# word2_list=[] 
# for i in word1: 
#     word1_list.append(i) 
# for i in word2: 
#     word2_list.append(i) 
# print(word1_list)
# print(word2_list) 


# if n ==1 : 
#     print(True) 
# elif n > 0:
#     if n%4==0: 
#         print(True) 
#     else : 
#         print(False) 
# else : 
#     print(False) 


# Input: 
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# # Output: true 
# l=[] 
# for i in set(sentence): 
#     l.append(i) 
# l.sort() 
# sentence="".join(l)
# s='abcdefghijklmnopqrstuvwxyz' 
# print(sentence) 
# if sentence == s : 
#     print(True) 
# else : 
#     print(False)


# Input: 
# nums = [2,2,3,2]
# # Output: 3 
# p={}
# for i in nums: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# print(p)
# for key,value in p.items(): 
#     if value ==1 : 
#         print(key)

# Input: 
# nums = [2,7,9,3,1]
# # Output: 4
# # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# # Total amount you can rob = 1 + 3 = 4. 
# m,n=[],[] 

# for i in range(0,len(nums),2): 
#     m.append(nums[i]) 
# for i in range(1,len(nums),2): 
#     n.append(nums[i]) 
# print(m)
# print(n) 
# count1,count2=0,0 
# for i in m: 
#     count1+=i   
# for i in n: 
#     count2+=i 
# print(max(count1,count2))   


# l=[10,20,30,50,40,30,20,10] 
# s=0  
# e=len(l)-1 
# while (s<e): 
#     mid = s+(e-s)//2   
#     if (l[mid]<l[mid+1]): 
#         s=mid+1  
#     else : 
#         e=mid 
# print(s)


# Input: 
# chars = ["a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c"]
# # Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"] 
# p={}
# for i in chars: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1 
# print(p) 
# s="" 
# for key,value in p.items(): 
#     s+=key   
#     s+=str(value)
# print(s)
# l=[] 
# for i in s: 
#    l.append(str(i)) 
# print(l)  

# prime number => jo khud ya 1 se devide ho jaye     

# n=10  
# if n%2==0: 
#     print ("Even") 
# else ("Not an Even ")
             
#Finding Range   
# n=10  
# for i in range(2,n+1): 
#     flag =True
#     for j in range(2,i): 
#         if i%j==0: 
#             flag =False                      
#             break   
#     if flag :
#         print(i)
   
# Input: 
# s1 = "bank"
# s2 = "knab"
# Output: true   
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# if s1 ==s2 : 
#     print (True)  
# if sorted(s1) != sorted(s2): 
#     print(False)  
# count =0
# for i in range(len(s1)) : 
#     if s1[i] != s2[i]: 
#          count +=1    
# if count <=2: 
#      print(True) 
# else : 
#     print(False) 


# Input: 
s = "xyz"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2. 
# l=[]
# num ="123456789" 
# falg =0
# for i in num: 
#     if i in s: 
#         flag =True   
#         break 
#     else : 
#         flag = 0  
# if flag ==1 : 
#     for i in s: 
#         if i.isdigit(): 
#             l.append(int(i)) 
#     m=set(l) 
#     l.clear()
#     for i in m : 
#         l.append(i) 
#     l.sort() 
#     if len(l)==1:
#         print(-1) 
#     else : 
#         print(l[1]) 
# else : 
#     print(-1)

# Input:
# s = "Hello how are you Contestant"
# k = 4
# d=""
# # Output: "Hello how are you"
# p=s.split(" ")
# print(p)  
# for i in range(0,k): 
#     print(p[i])
#     d+=p[i]
#     d+=" "
# print(d.strip())


# Input: 
# firstWord = "acb"
# secondWord = "cba"
# targetWord = "cdb"
# # Output: true
# # Explanation:
# # The numerical value of firstWord is "acb" -> "021" -> 21.
# # The numerical value of secondWord is "cba" -> "210" -> 210.
# # The numerical value of targetWord is "cdb" -> "231" -> 231.
# # We return true because 21 + 210 == 231. 
# p=firstWord.replace('a','1').replace('b','2').replace('c','3') 
# p1=secondWord.replace('a','1').replace('b','2').replace('c','3') 
# p2=targetWord.replace('a','1').replace('b','2').replace('c','3') 
# if int(p) + int(p1) == int(p2): 
#     print(True) 
# else : 
#     print(False)


# Input: 
# num = "35427"
# # Output: "35427"
# # Explanation: "35427" is already an odd number. 
# p=num[::-1] 
# print(p) 
# for i in p: 
#     if int(i)%2!=0: 
#       print(i[1::])  

# # Input: 
# words1=["a","ab"]
# words2 = ["a","a","a","ab"]
# # Output: 2 
# p={}
# for i in words1 : 
#   if i in p: 
#     p[i]+=1
#   else: 
#     p[i]=1 
# print(p) 
# p1={} 
# for i in words2: 
#   if i in p1: 
#     p1[i]+=1 
#   else : 
#     p1[i]=1  
# print(p1)
# l,l1=[],[] 
# for kwy,value in p.items(): 
#   if value ==1 : 
#     l.append(kwy)  
# for kwy,value in p1.items(): 
#   if value ==1 : 
#     l1.append(kwy)   
# print(l)
# print(l1) 
# count =0
# for i in l: 
#   if i in l1: 
#     count +=1  
# print(count)


# Input: 
# nums = [1,2,5,2,3]
# target = 5
# # Output: [1,2]
# l=[]
# nums.sort() 
# for i in range(len(nums)): 
#   if nums[i] ==target : 
#       l.append(i) 
# print(l) 


# Input:
# nums = [-1,-2,3,4]
# k = 3
# # Output: [3,3]
# # Explanation:
# # The subsequence has the largest sum of 3 + 3 = 6. 
# nums.sort(reverse=True) 
# print(nums) 
# count =0
# l=[]
# for i in range(k): 
#     l.append(nums[i]) 
# print(l)


# Input: 
# words = ["abc","car","adad","racecatr","cool"]
# # Output: "ada" 
# for i in words: 
#   if i==i[::-1] :
#     print(i) 
#     break 
# else : 
#     print("")


# Input: 
# title = "capiTalIze tHe titLe"
# # Output: "Capitalize The Title" 
# p=title.lower() 
# m=p.split(" ")  
# print(m)
# l=[] 
# for i in m: 
#   l.append(i.capitalize()) 
# print(" ".join(l))
 
# Input: 
# num = 30
# # Output: 2
# # Explanation:
# # The only integers less than or equal to 4 whose digit sums are even are 2 and 4. 
# count =0
# for i in range(num): 
#   print(i) 
#   for j in str(i): 


# Input: 
# words = ["pay","attention","practice","attend"]
# pref = "at"
# lenght= len(pref)
# p=[]
# for i in words: 
#     p.append(i[:lenght]) 
# print(p) 
# count =0
# for i in p:
#   if pref in i: 
#     count +=1  
# print(count)

# Input: 
# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# # Output: [3,4]
# for i in range(len(nums)): 
#      {nums[i]}.intersection({nums[i+1]}).intersection({nums[i+2]}) 



# items1 = [[1,1],[4,5],[3,8]]
# items2 = [[3,1],[1,5]] 

# result ={i[0]:i[1] for i in items1} 
# result1 ={i[0]:i[1] for i in items2} 
# print(result)
# print(result1) 
# from collections import Counter   
# p=Counter(result)
# p1=Counter(result1)  
# merger = p+p1   
# dict_hash= dict(merger) 
# print(dict_hash) 
# result2=[[k,v] for k,v in dict_hash.items()]
# print(result2)


# # Input: 
# word = "bac"
# # Output: true
# # Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.   
# m="".join(set(word)) 
# m.sort()
# print(word)
# if word == set(word): 
#      print(True) 
# else : 
#      p={}
#      for i in word: 
#           if i in p: 
#                p[i]+=1 
#           else : 
#                p[i]=1 
#      print(p) 
#      l=[]
#      for key,value in p.items(): 
#           if value==2: 
#                l.append(key) 
#      print(l)
#      if len(l)==1: 
#           print("True") 
#      else : 
#           print("False")  
     
     
# Input: 
# a = 12
# b = 6
# # Output: 4
# # Explanation: The common factors of 12 and 6 are 1, 2, 3, 6. 
# count =0
# for i in range (1,n): 
#      if a%i==0 and b%i==0: 
#           print(i)   
#           count +=1 
# print(count)

# Input: 
nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.  
posi=set() 
nege=set() 
result=[] 
for i in nums: 
     if i>0: 
          posi.add(i) 
     else : 
          nege.add(i) 
for i in posi: 
     if -i in nege: 
          result.append(i)
print(*result)
