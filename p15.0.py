# l=[1,2,3,4] 

# l=[1,2,3,4] 
# l[::-1]
# p=[]
# for i in range(len(l)-1,-1,-1): 
#     p.append(l[i]) 
# print(p)     

# Print list in ascending or descending order 

# l=[1,2,5,4,3,8,7,6] 
# m=[]
# l.sort() 
# for i in range(len(l)-1,-1,-1): 
#     m.append(l[i])     
# print(m) 

# l=[1, 69, 420, 66, 41] 
# count =0
# for i in l: 
#     print(i)  
#     count +=i           
# print(count//len(l))

# l=[1,4,3,56,7,9] 
# # max_elem= l[0] 
# # for i in range(len(l)): 
# #     if l[i]<max_elem: 
# #         max_elem = l[i] 
# # print(max_elem) 

# # print(min(l))  

# # l.sort() 
# # print(l)
# # print(l[1]) 

# l=[1,2,3,47,5] 
# flag =0
# for i in range(len(l)-1): 
#     for j in range(1,len(l)): 
#         if l[i]<l[i+1] : 
#            flag =1  
#         else : 
#             flag =0 
# if flag ==1 : 
#     print("Sorted")
# else : 
#     print("Not Soprted ")  


# p={1:2,3:5,6:8}  
# # =>  [Key:Value]
# print(p) 
# for keys ,value in p.items(): 
#     print(keys,"->",value)

# p={1:2,4:6,7:9} 
# p2={9:4,6:2}  
# # # p.update(p2) 
# # # print(p)

# # merger={**p,**p2}  # unpack operator 
# # print(merger) 

# from collections import ChainMap  

# merger=ChainMap(p,p2) 
# print(merger)
# counmt =0
# for value in p.values(): 
#     counmt+=value 
# print(counmt) 

# l=[1,3,2,2,3,4,5,4,3,2,1,1] 
# p={} 
# for i in l: 
#     if i in p: 
#         p[i]+=1  
#     else : 
#         p[i]=1 
# print(p) 
# # result = 0 
# # for i in l: 
# #     result^=i  
# # print(result)
# for keys in p.keys(): 
#     print(keys)



# p={1:2,4:6,7:9} 
# p2={9:4,6:2,4:2,1:5}    

# from collections import Counter  

# p3=Counter(p)
# p4=Counter(p2) 
# print(p3)
# print(p4)

# merge = p3+p4    
# print(merge) 

# dic_cov= dict(merge) 
# print(dic_cov)

