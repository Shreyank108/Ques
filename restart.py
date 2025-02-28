# a= int(input("enter a nmber")) 
# b= int(input("enter b number")) 
# print(a+b) 

# a= input("Enter a name") 
# age = int(input("Ente4r age ")) 
# print(f"Hello {a}, you are {age} years old ")

# CONDITIONAL STATEMENTS   

# a= int(input("Entrer a"))
# b= int(input("Entrer b"))
# c= int(input("Entrer c"))
# if a == b ==c  :  
#     print("all are equal") 
# elif a ==b or a==c or b==c :           
#     print("two are eual") 
# else : 
#     print("all are unique")  

# gender = input("Enter ur gender : Male or Female") 
# if gender == 'Male': 
#     print("Good morning sir" ) 
# else : 
#     print("Good morning Mam")

# n= int(input("Enter")) 
# if n%2==0 : 
#     print("Even") 
# else : 
#     print("Odd")

# age = int(input("Enter your age")) 
# if age >=18 : 
#     print("You are eligible for vote") 
# else : 
#     print(f"{18-age} years left to eligible to vote")


#ITERATIVE STATEMENTS---------------------------  
# n= int(input("Enrter n number")) 
# for i in range(n): 
#     print("Hello") 

# n= int(input("enter a number")) 
# for i in range(n,0,-1): 
#     print(i)

# n=int(input("Enter a number which u want to make a number table ")) 
# for i in range(1,11): 
#     print(f"{n}X{i}={n*i}") 

# n= int(input("Enter a number")) 
# sum =0 
# for i in range(1,n+1):  
#     sum+=i    
# print(sum) 

# n=int(input("enter a number")) 
# fact =1 
# for i in range(1,n+1):
#       fact *=i           
# print(fact)

# n=int(input("enter a nu,mber ")) 
# even =0   
# odd =0  
# for i in range(n): 
#     if i%2==0: 
#         even+=i          
        
#     else : 
#         odd+=i   
# print(even,odd) 

# n = int(input("Enter a number"))
# sum =0  
# for i in range(1,n): 
#     if n%i==0:
#        sum+=i      
# print(sum)   

# n= int(input("Enter a number "))  
# sum =0 
# for i in range(1,n): 
#     if n%i==0: 
#        sum+=i   
# if sum == n : 
#     print("Perfect nnumber") 
# else : 
#     print("Not a perfect number") 

# n= 234
# sum = 0    
# for i in str(n): 
#     sum+=int(i) 
# print(sum)


# p=10 
# count =0 
# for i in range(1,3): 
#     if p%i==0: 
#         count +=1   
# if count >2: 
#     print("prime") 
# else : 
#     print("Not a prime number") 
     
# number = 111   
# m = str(number) 
# k=m[::-1] 
# if number == int(k): 
#     print("pallindrome") 
# else : 
#     print("Not a Pallindrome")   

# n= 153
# sum =0    
# for i in str(n): 
#     sum+=int(i)**3  
# print(sum) 

# n= 145  
 
# sum =0  
# for i in str(n):
#     fact =1 
    
#     for j in range(1,int(i)+1): 
#         fact*=j  
#     sum+=fact  
# print(sum) 


# number = 24
# sum_of_digit =0     
# for i in str(number): 
#     sum_of_digit+=int(i)  
# print(sum_of_digit)
# if number % sum_of_digit ==0 : 
#     print("Harshad number") 
# else : 
#     print("Not an Harshad number")

# n= 5  
# for i in range(3): 
#     n =n*n  
# print(n)

# noting to solve today 

# String  
# a= "shreyank" 
# b= "Agrawal" 
# print(a==b) 

# a="3" 
# b="5" 
# print(a+b)

# a="Shreyank" 
# print(len(a))

# a="shreyank" 
# print(a.capitalize()) 

# a="shreyank" 
# b="Agrawal" 
# c=a.join(b)
# print(c) 

# a="shReyAnk"
# c="" 
# for i in a : 
#     if i.islower(): 
#         c+=i   
# for i in a : 
#     if i.isupper(): 
#         c+=i    
# print(c)     

# str1 = "P@#yn26at^&i5ve"
# countlower =0   
# countupper=0  
# countspecial=0  
# for i in str1: 
#     if i.isalpha(): 
#         countlower+=1   
#     elif i.isnumeric(): 
#         countupper+=1  
#     else : 
#         countspecial+=1  
# print(countlower,countupper,countspecial)

# a="P@#yn26at" 
# c="" 
# for i in range(len(a)-1,-1,-1): 
#     c+=a[i] 
# print(c)

#List  
# n=int(input("Enter a range u want to genrate "))
# l=[] 
# for i in range(n): 
#     x=int(input("Enter elements")) 
#     l.append(x) 
# print(l)

# l=[1,2,3,5,7,6]
# sum=0    
# for i in l: 
#     sum+=i   
# print(sum) 
# max = l[0]
# for i in range(len(l)): 
#     if l[i]> max : 
#         max = l[i] 
# print(max)

# a="jatin" 
# for i in range(len(a)): 
#     print(i)   

# l=[2,5,4,3,67,78,45,69] 
# first = float("-inf") 
# second = float("-inf")   
# for i in l: 
#     if i> first : 
#         second, first = first , i     
#     elif first > i > second :  
#         second = i   
# print(second)







# def IsSorted(l): 
#     for i in range(len(l)-1): 
#         if l[i]> l[i+1]: 
#             return False                       
#     return True
# l=[1,2,3,4,5,6]  
# print(IsSorted(l))

# a=0   
# b=1  
# for i in range(10): 
#     c=a+b   
#     b=a   
#     a=c   
#     print(c) 



# def IsPallindrome(l): 
#     start = 0  
#     end =len(l)-1  
#     while start < end : 
#         if l[start] != l[end]   : 
#             return False       
#         start +=1  
#         end -=1    
#     return True  
    
# l=[1,2,3,2,1] 
# print(IsPallindrome(l)) 

# l=[1,2,3,4,5,6] 
# n= int(input("Enter a number"))
# # [2,3,4,5,6,1] 
# for i in range(n):
#     left = l[len(l)-1]
#     for i in range(len(l)-1,0,-1): 
#         l[i] = l[i-1]  
#     l[0] = left 

# print(l)
# def linear_Search(l,n): 
#     for i in range(len(l)-1): 
#         if l[i] == n: 
#             return i     
#     return -1  
# l=[1,2,3,4,5,6] 
# n=int(input("Enter a Number which u want to search ")) 
# print(linear_Search(l,n)) 

# def BinarySearch(l,n): 
#     left = 0   
#     right = len(l)-1   
#     while left <= right:  
#         mid = (left+right) //2     
#         if l[mid] == n: 
#             return mid    
#         elif l[mid]< n: 
#             left = mid+1   
#         else : 
#             right = mid -1   
#     return -1 
        

# l=[1,2,3,4,5,6] 
# n= int(input("enter a Number which u want to search ")) 
# print(BinarySearch(l,n,))

# def bubblesort(l): 
#     n= len(l) 
#     for i in range (n): 
#         swapped = False     
#         for j in range(n-i-1): 
#             if l[j]> l[j+1]: 
#                 l[j],l[j+1]= l[j+1],l[j] 
#                 swapped = True 
#         if not swapped: 
#             break     

# l=[100,2,3,56,34,200] 
# bubblesort(l)
# print(l) 

# Input: 
# nums = [3,3]
# target = 6
# l=[]
# # Output: [1,2] 
# for i in range(len(nums)-1): 
#     for j in range(1,len(nums)): 
#         if (nums[i]+nums[j])== target:  
#             l.append(i) 
#             l.append(j) 
# print(l)

Hello World! 123 @2025