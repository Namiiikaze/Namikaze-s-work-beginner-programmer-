#!/usr/bin/env python
# coding: utf-8

# In[7]:


def say_hello(name='default'):
    print(f'hello {name}')


# In[9]:


say_hello()


# In[11]:


def add_num(num1,num2):
    return num1+num2


# In[13]:


result=add_num(20,30)


# In[14]:


20 % 5 ==0


# In[18]:


def even_check(num):
    result = num % 2 == 0
    return result


# In[19]:


even_check(20)


# In[33]:


def check_even_list(num_list):
    
    even_number = []
    
    for number in num_list:
        if number % 2 == 0:
            even_number.append(number)
        else:
            pass
    return even_number
    


# In[34]:


check_even_list([2,3,4])


# In[36]:


stock_prices = [('google',100),('apple',200),('amazon',400)]


# In[37]:


stock_prices


# In[38]:


for items in stock_prices:
    print(items)


# In[41]:


for a,b in stock_prices:
    print(b+(0.2*b))


# In[53]:


example = [1,2,3,4,5]


# In[54]:


from random import shuffle


# In[55]:


shuffle(example)


# In[56]:


example


# In[ ]:




