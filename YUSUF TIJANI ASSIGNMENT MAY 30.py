#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bmi(weight, height): #
    "Function that calculates the Body Mass Index of a person" #
    BMI = weight/(height*height)
    return BMI #


# In[3]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        
        


# In[4]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        


# In[5]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        


# In[6]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        


# In[9]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        
else:
        print("\nThe age should be between 13 and 69")
        


# In[12]:


print("Input the requested details to calculate your BMI")

print("\nAge")
age = int(input()) # inseert the data type


print("\nWeight in kg:")
weight = float(input()) # insert the data type

print("\nHeight in m:")
height = float(input()) # insert the data type

# write a condition that validates the age and calls the function

if age >12 and age <70: # insert your conditional age bracket
    result = bmi(weight, height) # insert your function
    
    # Let the user know their BMI and also know if it's healthy or not
if age < 12 and age >70:
        print(f"\it does not work for your age")
    if result > 25: # inseert a condition that can classify this
        print(f"\nYour BMI is: {result} and it shows you are overweight")
    elif result < 18:
        print(f"\nYour BMI is: {result} and it shows you are underweight")
    else:
        print(f"\nYour BMI is: {result} and it shows you are healthy")
        


# In[13]:


my_plan = "I will perform all my outstanding kadatemy assignments asap"
my_plan.split() # split the sentence into words


# In[14]:


my_plan_in_words = my_plan.split()


# In[16]:


for i in range(1, len(my_plan_in_words)):
    if i == 5:
        print(my_plan_in_words[i])


# In[ ]:




