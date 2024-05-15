# Input: 
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
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
date = "20th Oct 2052"
# Output: "2052-10-20"
p=date.split(" ") 
months={
    "Jan" :1 ,
    "Feb":2,
    "Mar":3, 
    "Apr":4,
    "May":5,
    "Jun":6,
    "Jul":7,
    "Aug":8,
    "Sep":9,
    "Oct":10,
    "Nov":11,
    "Dec":12}
print(p)
val=0
for key,value in months.items(): 
    if key == p[1]: 
        val+=value 
print(val) 
d_p=[]
for i in p[0]: 
    d_p.append(i) 
print(d_p) 
d_p=d_p[:-2] 
join_d_p= "".join(d_p) 
print(join_d_p) 


