# firat occurace of number using binary search   
# def binary(l,n,t): 
#     s= 0 
#     e= n  
#     ans =-1  
#     while (s<=e): 
#         mid = (s+e)//2  
#         if l[mid] == t :  
#             ans =mid
#             e=mid-1  
#         elif l[mid] < t:    
#             s=mid+1  
#         else : 
#             e=mid-1  
#     return ans 

# l=[1,3,3,3,3,3,4,5]; 
# n=len(l) 
# t=3
# print(binary(l,n,t))

# firat occurace of number using binary search  
 
# Find the Smallest Element Greater than Target:

# def binary(l, n, p): 
#     s = 0 
#     e = n - 1 
#     ans = -1
#     while s <= e: 
#         mid = s + (e - s) // 2 
#         if l[mid] > p: 
#             ans = l[mid]
#             e = mid - 1 
#         else:
#             s = mid + 1
#     return ans

# nums = [1, 2, 4, 6, 8]
# target = 6
# n = len(nums)
# print(binary(nums, n, target))  

# Check for Existence: 

# def finding(l,p): 
#     s=0   
#     e=len(l)-1 
#     while (s<=e): 
#         mid = s+(e-s)//2 
#         if l[mid]==p: 
#             return True   
#         elif l[mid] < p: 
#             s=mid+1 
#         else : 
#             e=mid-1 
#     return False
# l=[1,2,3,4,5]
# target =3
# print(finding(l,target)) 

