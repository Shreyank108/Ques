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

##Dancing Doll

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
# s = "xyz"
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
# nums = [-1,2,-3,3]
# # Output: 3
# # Explanation: 3 is the only valid k we can find in the array.  
# posi=set() 
# nege=set() 
# result=[] 
# for i in nums: 
#      if i>0: 
#           posi.add(i) 
#      else : 
#           nege.add(i) 
# for i in posi: 
#      if -i in nege: 
#           result.append(i)
# print(*result)


# Input: 
# nums = [1,2,4,7,10]
# # Output: 9
# # Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9. 
# count =0  
# l=[]
# for i in nums: 
#      if i%3==0 and i%2==0: 
#           l.append(i)
#           count +=i   
# if len(l)==0: 
#      print(0) 
# else : 
#      print(count//len(l)) 

# Input:
# nums = [4,4,2,4,3]
# # Output: 3 
# p=[*set(nums)]  
# print(p)


# words = ["aba","aabb","abcd","bac","aabc"] 
# m=[]
# for i in words: 
#     p=sorted(set(i)) 
#     k="".join(p) 
#     m.append(k) 
# print(m) 
# p={} 
# for i in m: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# print(p)
# count =0 
# for value in p.values(): 
#     if value >1:  
#         count +=1 
# print(count) 

# Input: 
# num = 121
# # Output: 1
# # Explanation: 7 divides itself, hence the answer is 1.
# l=[]
# p=set(str(num)) 
# l.append([*p])  
# print(len(*l))

# nums = [-3,-2,-1,0,0,1,2]
# count_neg =0 
# count_posi=0  
# for i in nums: 
#     if i==0: 
#         nums.remove(0) 
#     if i<0: 
#         count_neg+=1 
#     else : 
#         count_posi+=1  
# print(max(count_posi,count_neg))

# n=10   
# for i in range(2,n): 
#     for j in range(2,i): 
#         if i%j==0: 
#             break 
#     else : 
#         print(i) 

# Input: 
# nums = [13,25,83,77]
# # Output: [1,3,2,5,8,3,7,7] 
# print("".join(nums)) 


# # Input: 
# n = 15
# # Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"] 
# '''answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.''' 
# l=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0: 
#         l.append("FizzBuzz") 
#     if i%3==0: 
#         l.append("Fizz") 
#     if i%5==0: 
#         l.append("Buzz") 
#     else : 
#         l.append(i) 
# print(l)


 
# # Input:
# nums1 = [[1,2],[2,3],[4,5]]
# nums2 = [[1,4],[3,2],[4,1]]
# # Output: [[1,6],[2,3],[3,2],[4,6]]  
# n1={i[0]:i[1] for i in nums1}
# n2={i[0]:i[1] for i in nums2} 

# print(n1)
# print(n2)
# from collections import Counter  
# num3 =Counter(n1)
# num4 =Counter(n2) 

# merger= num3+num4   

# changes_to_dict =dict(merger) 
# print([changes_to_dict]) 

# result = [[k,v] for k,v in changes_to_dict.items()] 
# print(result) 


# a=nums1[:]
# a.extend(nums2)
# dic=Counter(a)
# m=max(dic.values())
# ans=[]
# if m>1:
#     for i,j in dic.items():
#         if j==m:
#             ans.append(i)
#     return min(ans)
# else:
#     min1=min(nums1)
#     min2=min(nums2)
#     if min1>min2:
#         return int(str(min2)+str(min1))
#     else:
#         return int(str(min1)+str(min2))


# Input: 
# n = 9
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are 3, 5, 6, 7. The sum of these numbers is 21. 
# sum=0
# for i in range(1,n+1): 
#     if i %3==0 or i%5==0 or i%7==0: 
#         sum+=i      
# print(sum)



# Input: 
# arrivalTime = 15
# delayedTime = 5 
# # Output: 20 
# # Explanation: Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours) 
# sum= arrivalTime+delayedTime  
# if sum ==24 : 
#     print(0) 
# else : 
#     print(sum) 

# tmp = list(s)
# start = 0
# end = len(s) - 1

# while start <= end:
#     l = tmp[start]
#     r = tmp[end]
#     if l != r:
#         change = l if l<r else r
#         tmp[start], tmp[end] = change, change
#     start += 1
#     end -= 1

# return ("").join(tmp) 


# Input: 
# n = 10 
# ["call","call","call"]
# # Output: [10,11,12]
# # Explanation: 
# # counter() = 10 // The first time counter() is called, it returns n.
# # counter() = 11 // Returns 1 more than the previous time.
# # counter() = 12 // Returns 1 more than the previous time. 
# print(n)

# Input: 
# init = 5
# calls = ["increment","reset","decrement"]
# # Output: [1,2,1,0,0] 
# count =init
# l=[]  
# for i in calls : 
#     if i =="increment" : 
#         count+=1  
#         l.append(count)  
#     elif i =="decrement": 
#         count -=1  
#         l.append(count)
#     elif  i=="reset" :
#         count =init  
#         l.append(count)
# print(l)


# s = "aaabc" 
# p=len(set(s)) 
# print(p)

# # Input:
# n = 192
# # Output: true
# # Explanation: We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting number is 192384576. This number contains all the digits from 1 to 9 exactly once. 
# l=[]
# one=n*2  
# two=n*3  
# l.append(n)
# l.append(one)
# l.append(two) 
# print(l) 
# p="" 
# for i in l: 
#     p+=str(i) 
# s="".join(sorted(p))
# print(s) 
# d='123456789' 
# if s==d:  
#     print(True) 
# else : 
#     print(False) 

# Input: 
# words = ["cd","ac","dc","ca","zz"]
# Output: 2  
# l=[]
# for i in words: 
#     l.append("".join(sorted(i))) 
# print(l) 
# p={}
# for i in l: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1 
# print(p) 
# count =0   
# for value in p.values(): 
#     if value ==2 : 
#         count+=1  
# print(count) 


s = "string"
# p = s.split('i')
# m = []
# x=p[len(p)-1]
# for i in range(len(p)-1):
#     m.append(p[i][::-1])

# result = ''.join(m) + ''.join(x) 

# print(result)


# result = []
# reverse = False
# for char in s:
#     if char == 'i':
#         reverse = not reverse
#     else:
#         if reverse:
#             result.insert(0, char)
#         else:
#             result.append(char)
# if reverse:
#     result.reverse()
# return ''.join(result)


# Input: 
# words = ["never","gonna","give","up","on","you"]
# s = "ngguoy"
# # Output: true 
# k=[]
# for i in range(len(words)): 
#     k.append(words[i][0]) 
# m="".join(k) 
# print(m) 
# if m==s: 
#     print(True) 
# else : 
#     print(False)


# # Input: 
# low = 1200
# high = 1230
# # Output: 9
# # Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99. 
# count =0 
# if low<10:
#     for i in range(11,high): 
#         if str(i)==str(i)[::-1]:   
#             print(i)
#             count +=1    
# else : 
#     for i in range(low,high): 
#         if str(i)==str(i)[::-1]:   
#             print(i)
#             count +=1
# print(count)


# ans = diff = prefix = 0 
#         for x in nums: 
#             ans = max(ans, x*diff)
#             diff = max(diff, prefix-x)
#             prefix = max(prefix, x)
#         return ans 


# Input: 
# n = 10
# m = 3
# # Output: 19
# # Explanation: In the given example:
# # - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# # - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# # # We return 37 - 18 = 19 as the answer. 
# NotDivisibleByM =0  
# DivisibleByM=0
# for i in range(1,n+1): 
#     if i%m==0: 
#         DivisibleByM+=i   
#     else : 
#         NotDivisibleByM+=i   
# print(NotDivisibleByM-DivisibleByM)


# Input: 
# nums = [5,1,4,1]
# indexDifference = 2
# valueDifference = 4
# # Output: [0,3]
# # Explanation: In this example, i = 0 and j = 3 can be selected.
# # abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
# # Hence, a valid answer is [0,3].
# # [3,0] is also a valid answer. 
# first = nums[0] 
# last = nums[len(nums)-1] 


# n = len(grid)
#         for i in range(n):
#             isChampion = True
#             for j in range(n):
#                 if i != j and grid[j][i] == 1:
#                     isChampion = False
#                     break
#             if isChampion:
#                 return i
#         return -1  



# count = Counter(nums)
# result = 0
# for num, cnt in count.items():
#     if cnt == 2:
#         result ^= num
# return result 

# Sort the color  
# nums =[1,0,2,3,4,0,2] 
# nums.sort() 
# print(nums)


# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         nawab =0 
#         seats.sort() 
#         students.sort() 
#         for i in range(len(students)): 
#             nawab+=abs(students[i]-seats[i]) 
#         return nawab 

        # nums.sort()
        # numTracker = 0
        # minIncreament = 0

        # for num in nums:
        #     numTracker = max(numTracker, num)
        #     minIncreament += numTracker - num
        #     numTracker += 1
        # return minIncreament
        
# ans = 0
#         for i in range(26):
#             letter = chr(97 + i)
#             if letter in word and letter.upper() in word:
#                 ans += 1
                
#         return ans

# rev=s[::-1]
#         for i in range(len(s)-1):
#             if(s[i:i+2] in rev):
#                 return True
#         return False

# x = 18
# count =0
# for i in str(x): 
#         count +=int(i) 
# if x%count==0: 
#         print(True) 
# else : 
#         print(False)


#  M = {}
#         maxFreq = 0

#         # Iterate through the list and populate the dictionary
#         for num in nums:
#             if num in M:
#                 M[num] += 1
#             else:
#                 M[num] = 1
#             maxFreq = max(maxFreq, M[num])

#         res = 0
#         # Iterate through the dictionary to find elements with frequency equal to maxFreq
#         for key, value in M.items():
#             if value == maxFreq:
#                 res += value

#         return res

# nums=[3,3,3]
# if nums[0]+nums[2] > nums[1]: 
#         if nums[1]+nums[2] >nums[0] : 
#                 if nums[0]+nums[1] > nums[2]:
#                         p={} 
#                         for i in nums: 
#                                 if i in p: 
#                                         p[i]+=1 
#                                 else :
#                                         p[i]=1    
#                         for i in p: 
#                                 if len(p) ==2 : 
#                                         return "isosceles" 
#                                 elif len(p)==1: 
#                                         return "equilateral" 
#                                 else : 
#                                         return "scalene" 
#                 else : 
#                         return "none"                
#         else : 
#                 return "none" 

                
                
# else : 
#         return "none"


#  n = len(nums1)
#         m = len(nums2)

#         c1 = 0
#         c2 = 0

#         for i in range(n) :
#             if nums1[i] in nums2 :
#                 c1 += 1
#         for i in range(m) :
#             if nums2[i] in nums1 :
#                 c2 += 1
                
#         return [c1, c2]



# nums = [1,1,0,0,1]
# m = nums.count(1) 

# zipped_list = []
# for i in range(len(nums) - m + 1): 
#     zipped_list.append(nums[i:i + m])  

# print(zipped_list)

# p = [] 
# for i in zipped_list:
#     p.append(i.count(0))  

# print(min(p))
    
# from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
#         dummy = ListNode()  # Create a dummy node
#         current = dummy     # Set current to the dummy node
        
#         # Traverse both lists
#         while list1 and list2: 
#             if list1.val < list2.val: 
#                 current.next = list1  # Link current node to list1
#                 list1 = list1.next     # Move to the next node in list1
#             else: 
#                 current.next = list2  # Link current node to list2
#                 list2 = list2.next     # Move to the next node in list2
            
#             current = current.next  # Move current to the last node in the merged list

#         # If there are remaining nodes in either list, append them
#         if list1: 
#             current.next = list1   
#         elif list2: 
#             current.next = list2   

#         return dummy.next
  
# nums = [4, 5, 6, 7, 0, 1, 2]
# target = 0
# found = False  # Flag to check if the target is found

# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)  # Print the index of the target
#         found = True  # Set the flag to True
#         break  # Exit the loop once the target is found

# if not found:
#     print(-1) 
        
# dummy = ListNode(0)
#         dummy.next = head
        
#         # Initialize current pointer
#         current = dummy
        
#         # Traverse the list
#         while current.next is not None:
#             if current.next.val == val:
#                 # Skip the node with the value to remove
#                 current.next = current.next.next
#             else:
#                 # Move to the next node only if we didn't remove the current one
#                 current = current.next
        
#         # Return the next of dummy, which is the new head
#         return dummy.next 

# nums = [1,1,1,2,2,3]
# p={}
# for i in nums: 
#         if i in p: 
#                 p[i]+=1     
#         else : 
#                 p[i]=1   
# result =[] 
# for key , value in p.items(): 
#         if value >=2: 
#                 result.append(key) 
#                 result.append(key) 
#         else : 
#               result.append(key) 
# print(result)
                
# if len(nums) <= 2:
#         print(len(nums))
# k = 2  
# for i in range(2, len(nums)):
#         if nums[i] != nums[k-2]:
#          nums[k] = nums[i]
#         k += 1
# print(nums)
# print(k) 


# p={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} 
# s = "III"
# l=[]   
# sum = 0   
# for key,value in p.items(): 
#         if s.split("") in p: 
#                 l.append(value)   
# print(l) 


# Input: 
# strs = ["flower","flow","flight"]
# # Output: "fl"    
# min_string = min(strs,key=len) 
# print(min_string)
# for i in 

# Input: 
# n = 2
# Output: 12 

# n=1
# result =[] 
# i=1  
# if n==1 : 
#       result.append(1)
# while len(result) < n-1: 
#         if i%2==0 or i%3==0 or i%5==0 : 
#                 result.append(i) 
#         i+=1   
# print( result[-1])


# Input: 
# nums = [1,2,3,4,10]  
# l1=[] 
# l2=[] 
# for i in nums: 
#         if i< 10 : 
#                 l1.append(i) 
#         if i >= 10 : 
#                 l2.append(i) 
# sum_of_l1= sum(l1) 
# sum_of_l2= sum(l2) 
# if sum_of_l1 > sum_of_l2 or sum_of_l2 > sum_of_l1 : 
#         print(True) 
# else : 
#         print(False) 


# s = "dart"
# k = 3
# p=""
# l=[] 
# if s[k] == s[0]: 
#         print(s) 
# else :
#         for i in s : 
#                 if i !=s[k]: 
#                         l.append(i) 
#         print(s[k]+"".join(l)) 

# Input: 
# strs = ["eat","tea","tan","ate","nat","bat"]
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]] 
# map={} 
# for i in strs: 
#         sorted_word= "".join(sorted(i))
#         if sorted_word not in map : 
#                 map[sorted_word]=[] 
#         map[sorted_word].append(i)  
# print(list(map.values()))

# s="a1b10c3d5" 
# #output = "abbbbbbbbbb" 

# i=0    
# result=""
# while i < len(s): 
#       char = s[i] 
#       i+=1   
#       num_string="" 
#       while i<len(s) and s[i].isdigit(): 
#               num_string+=s[i] 
#               i+=1   
#       int_conversion= int(num_string) 
#       result+=char*int_conversion 
# print(result)

# a=1 
# a=bin(5)[2:] 
# l=[]
# for i in str(a): 
#         l.append(i)
# print(l) 
# m=[]
# for i in l: 
#         if i == '0': 
#                 m.append("1")
#         elif i=='1': 
#                 m.append('0') 
# print(m)
# s=""
# for i in m: 
#         s+=i         
# print(s) 
# therealvalue = int(s,2) 
# print(therealvalue) 


# Input: 
# s = "IceCreAm"
# # Output: "AceCreIm"
# l=['a','e','i','o','u','A','E','I','O','U']
# p=[]  
# for i in s : 
#         if i in l:  
#                 p.append(i)
#                 k=s.replace(i," ") 
# print(p) 
# print(k)


# nums = [0,0,1,1,1,2,2,3,3,4]
# if len(nums) == 0:
#         return 0

# i = 0  # first pointer
# for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#                 i += 1
#                 nums[i] = nums[j]
    
# print( i + 1) 


# Input: 
# digits = [1,2,3]
# # Output: [1,2,4]
# s=""  
# for i in digits: 
#         s+=str(i) 
# print(s) 
# m=int(s)+1
# l=[]  
# for i in str(m): 
#    l.append(int(i))  
# print(l)     
 
 
# nums = [3,0,1] 
# p=0
# for i in range(1,len(nums)+1): 
#         if i not in nums: 
#                 p+=i   
# print(p)   


# Input: 
s = "((()"
# Output: 1 
# comon ='()'
# for i in range(len(s)):
#         if comon in s : 
#                 p= s.replace('()',"")   
#                 s=p
#         else : 
#                 p=s
# print(p)
# print(len(p))           
        
# stack =[] 
# for i in s: 
#         if i =='(': 
#                 stack.append(i) 
#         elif i==')' and stack and stack[-1]=='(': 
#                 stack.pop() 
#         else : 
#                 stack.append(i) 
# print(len(stack))

# result = []
    
#     def backtrack(curr_str, open_count, close_count):
#         # If the current string has reached the maximum length, add it to the result
#         if len(curr_str) == 2 * n:
#             result.append(curr_str)
#             return
        
#         # Add an opening parenthesis if we have less than n opening parentheses
#         if open_count < n:
#             backtrack(curr_str + "(", open_count + 1, close_count)
        
#         # Add a closing parenthesis if the number of closing is less than opening
#         if close_count < open_count:
#             backtrack(curr_str + ")", open_count, close_count + 1)
    
#     # Start the backtracking with an empty string and no parentheses used yet
#     backtrack("", 0, 0)
#     return result 


# num1 = 987
# num2 = 879
# num3 = 798

# # num1  -> 0001 
# l=[] 
# l.append(num1)
# l.append(num2)
# l.append(num3)
 
# l1=[]
# for i in l: 
#         p=""    
#         if i < 10:  
#                 p+="000"+str(i)  
#         elif i <100: 
#                 p+="00"+str(i) 
#         elif i< 1000:
#                 p+="0"+str(i)
#         elif i < 9999: 
#                 p+=str(i)
#         l1.append(p)    
# print(l1) 
# x=[] 
# num1 = l1[0]
# num2 = l1[1] 
# num3 = l1[2] 

# x.append(min(int(num1[0]),int(num2[0]),int(num3[0])))
# x.append(min(int(num1[1]),int(num2[1]),int(num3[1])))
# x.append(min(int(num1[2]),int(num2[2]),int(num3[2])))
# x.append(min(int(num1[3]),int(num2[3]),int(num3[3])))
 
# zeroes = ""
# for i in x: 
#         zeroes+=str(i)                 
# print(zeroes) 
# print(int(zeroes))


# coordinate1 = "a1"
# coordinate2 = "c3"

# p={
#     'a1': 'white', 'a2': 'black', 'a3': 'white', 'a4': 'black', 'a5': 'white', 'a6': 'black', 'a7': 'white', 'a8': 'black',
#     'b1': 'black', 'b2': 'white', 'b3': 'black', 'b4': 'white', 'b5': 'black', 'b6': 'white', 'b7': 'black', 'b8': 'white',
#     'c1': 'white', 'c2': 'black', 'c3': 'white', 'c4': 'black', 'c5': 'white', 'c6': 'black', 'c7': 'white', 'c8': 'black',
#     'd1': 'black', 'd2': 'white', 'd3': 'black', 'd4': 'white', 'd5': 'black', 'd6': 'white', 'd7': 'black', 'd8': 'white',
#     'e1': 'white', 'e2': 'black', 'e3': 'white', 'e4': 'black', 'e5': 'white', 'e6': 'black', 'e7': 'white', 'e8': 'black',
#     'f1': 'black', 'f2': 'white', 'f3': 'black', 'f4': 'white', 'f5': 'black', 'f6': 'white', 'f7': 'black', 'f8': 'white',
#     'g1': 'white', 'g2': 'black', 'g3': 'white', 'g4': 'black', 'g5': 'white', 'g6': 'black', 'g7': 'white', 'g8': 'black',
#     'h1': 'black', 'h2': 'white', 'h3': 'black', 'h4': 'white', 'h5': 'black', 'h6': 'white', 'h7': 'black', 'h8': 'white'
# }

# l=[]

# for key , value in p.items(): 
#         if coordinate1 == key  : 
#                 l.append(value) 
#         if coordinate2 == key  : 
#                 l.append(value)      
       
# if l[0]==l[1]: 
#         print(True)
# else : 
#         print(False)          



# l=[]
# for i in range(1,len(height)): 
#         if height[i-1]>threshold: 
#                 l.append(i) 
# return l 


# nums = [0,1,1,0] 
# p={}
# for i in nums: 
#         if i in p: 
#                 p[i]+=1  
#         else : 
#                 p[i]=1  
# print(p) 
# l=[]
# for key, value in p.items(): 
#         if value == 2 : 
#                 l.append(key) 
# print(l)             


# nums = [10,12,13,14]
# l=[]
# for i in nums: 
#         sum=0
#         for j in str(i): 
#              sum=+int(j) 
#              l.append(sum) 
# print(l)

# colors = [0,1,0,0,1]
# zeroes =0
# ones =0 
# for i in colors: 
#         if i==0: 
#                 zeroes+=1
#         elif i==1: 
#                 ones+=1   
# print(zeroes)  
# print(ones)  
# if ones == (zeroes +1) :  
#         print(zeroes)  
# else : 
#         print(0)  

# player_picks = defaultdict(lambda: defaultdict(int))
#     for player, color in pick:
#         player_picks[player][color] += 1
#     winners = 0
#     for player in range(n):

#         for color in player_picks[player]:
#             if player_picks[player][color] > player:
#                 winners += 1
#                 break  
#     return winners 
 
 
# Input:
# hours = [72,48,24,3]
# #  [24,42,54,48]
# Output: 2 
# p=[] 
# for i in range(1,11): 
#     p.append(i*24) 
# print(p)
# l=[] 
# j=1
# for i in range(len(hours)-1): 
#         l.append(hours[i]+hours[j]) 
#         j+=1 
# print(l)   
# count =0   
# for i in l: 
#     if i in p: 
#         count+=1  
# print(count)
    
# Input: 
nums = [3,6,9]
Output: 3 
count =0 

for i in nums: 
    if (i+1) % 3 ==0: 
        count+=1  
    elif (i-1)% 3==0: 
        count+=1   
print(count)