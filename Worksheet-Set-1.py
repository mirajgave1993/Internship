#!/usr/bin/env python
# coding: utf-8

# # Write a python program to find the factorial of a number

# In[7]:


fact = 1
num = int (input("Enter the Number:"))
number = num
while num > 0:
    fact= fact * num
    num = num - 1 
print ("The factorial of ",number, "is", fact)


# In[ ]:





# # Write a python program to find whether a number is prime or composite.

# In[5]:


num = int (input ("Enter the Number"))
fact= 0
for i in range (2, num):
    if (num % i ==0):
        fact= 1
        break
if (fact==0):
    print ("The number is prime.")
else:
    print ("The number is not a prime.")


# # Write a python program to check whether a given string is palindrome or not

# In[11]:


num= int (input ("Enter the Number:"))
org= num
rev= 0

while num > 0:
    rem=num % 10
    rev= rev * 10 + rem
    num = num // 10
if rev == org:
    print ("The Number", org, "is Palindrome")
else:
    print ("The Number ", org, "is not a Palindrome")

print ("The Reverse of ", org, "is", rev)
    


# # Write a Python program to get the third side of right-angled triangle from two given sides.

# In[20]:


from math import sqrt
print("Lengths of the triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


# # Write a python program to print the frequency of each of the characters present in a given string

# In[22]:


str1 = input ("Enter the string")
d1 = dict()
for c in str1:
    if c in d1:
        d1[c] = d1[c] + 1
    else:
        d1[c] = 1 
        
print (d1)


# In[24]:


str1 = input ("Enter the string")
d1 = dict()
for c in str1:
    d1[c]=d1.get(c, 0)+1
        
print (d1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




