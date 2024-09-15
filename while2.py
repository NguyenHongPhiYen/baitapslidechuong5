# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:11:12 2024

@author: Admin
"""

n=float(input("nhập giá trị thuộc khoảng [-89.9, 88.8]:"))
while -89.9> n or n>88.8:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n= int(input("Nhập một giá trị thuộc [-89.9, 88.8]: "))
print(f"Giá trị {n}")