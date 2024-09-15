# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:10:58 2024

@author: Admin
"""

n=int(input("Nhập một giá trị thuộc [-99, 99]: "))
while -99> n or n>99:
    print("Giá trị không hợp lệ! Vui lòng nhập lại.")
    n= int(input("Nhập một giá trị thuộc [-99, 99]: "))
print(f"Giá trị {n}")