# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:18:14 2024

@author: Admin
"""

n=int(input("nhập số nguyên n:"))
dict={i: i ** i for i in range(1, n + 1)}
print(dict)