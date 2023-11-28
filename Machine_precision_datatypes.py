#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# Machine precision for float16
machine_precision_float16 = np.finfo(np.float16).eps
print(f'Machine Precision for float16: {machine_precision_float16}')

# Machine precision for float32
machine_precision_float32 = np.finfo(np.float32).eps
print(f'Machine Precision for float32: {machine_precision_float32}')

# Machine precision for float64
machine_precision_float64 = np.finfo(np.float64).eps
print(f'Machine Precision for float64: {machine_precision_float64}')

# Machine precision for longdouble
machine_precision_longdouble = np.finfo(np.longdouble).eps
print(f'Machine Precision for longdouble: {machine_precision_longdouble}')


# In[3]:


import sys

machine_precision_float = sys.float_info.epsilon
print(f'Machine Precision for float: {machine_precision_float}')


# In[ ]:




