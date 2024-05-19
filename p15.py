l=[1,4,2,3,5,6] 
# l.sort()
# print(l) 
# l.sort(reverse=True) 
# print(l) 

# for i in range(len(l)): 
#     for j in range(len(l)-1-i): 
#         if l[i]>l[i+1]: 
#             p=l[i] 
#             l[i]=l[i+1] 
#             l[i+1]=p            
# print(l) 

# for j in range(len(l)):
#     for i in range(len(l) - 1 - j):
#         if l[i] < l[i + 1]:
#             p = l[i]
#             l[i] = l[i + 1]
#             l[i + 1] = p
# print(l)

# l=[1,4,3,2,5,6,7,34,4,3,2] 
# max1 = l[0] 
# for i in range(len(l)): 
#     if l[i]>max1 : 
#         max1=l[i] 
# print(max1)

# l=[1,4,3,2,5,6,7] 
# for i in l: 

# l=[1,2,3,2,1] 
# s="" 
# for i in l: 
#     s+=str(i) 
# print(s)
# p=s[::-1]
# print(p) 
# if p==s : 
#     print(True) 
# else : 
#     print(False) 

# l=[1,2,3,6,5] 
# flag =0
# for i in range(len(l)-1): 
#     for j in range(1,len(l)): 
#         if l[i]<l[i+1] : 
           
#             flag =1 
#         else : 
#             flag =0
          
# if flag ==1 : 
#     print("Sorted") 
# else : 
#     print("Not Sortede")

p={1:2,2:3,3:4} 
# p2={4:5,5:2,6:8} 
# p.update(p2) 
# print(p)

# merger= {**p,**p2} 
# print(merger) 

# from collections import ChainMap 
# marger = ChainMap(p,p2) 
# print(marger) 

# p={key:value} 
# count =0
# for value in p.values(): 
#     count +=value 
# print(count)
# l=[1,2,3,4,5] 
# p={}
# for i in l: 
#     if i in p: 
#         p[i]+=1  
#     else : 
#         p[i]=1 
# print(p) 

# p={1:2,2:3,3:5,6:2} 
# p1={2:4,1:5,6:3} 
# from collections import Counter 

# p2=Counter(p)
# p3=Counter(p1)  
# print(p2)
# print(p3)

# merger= p2+p3 
# print(merger)

# dict_conv = dict(merger)
# print(dict_conv)