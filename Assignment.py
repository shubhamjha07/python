#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Print user input table
def print_table(num,upto):
    for i in range(1, upto + 1):
        result = num * i
        print(num ,"*", i ,"=",result)
        
a=int(input("Enter number"))
b=int(input("Enter till you want table"))
print_table(a,b)


# In[29]:


#  Print palindrome string taking input as string
def palindrome(rev):
    return rev == rev[::-1]


a = input("Enter a string: ")

if palindrome(a):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[30]:


# Take input as string and reverse it

a = input("Enter a string: ")

rev = a[::-1]

print("Reversed string:", rev)


# In[ ]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


limit = 50
prime_numbers = find_primes_up_to(limit)

print(prime_numbers)

