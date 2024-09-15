# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:00:08 2024

@author: Admin
"""

n=int(input("nhập số nguyên dương cần tính giai thừa:"))
if n<0:
    print("Vui lòng nhập lại số nguyên dương")
giaithua=1
for i in range(1, n+1):
    giaithua *= i
print(f"Giai thừa của {n} là {giaithua}")