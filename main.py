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
date1 = "2020-01-15"
date2 = "2019-12-31"
# Output: 1

from datetime import datetime   

dt1 =datetime.strptime(date1,"%Y-%m-%d")
dt2 =datetime.strptime(date2,"%Y-%m-%d")

delay_time =abs(dt2 - dt1) 

print(delay_time.days)