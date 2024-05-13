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
matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column. 

