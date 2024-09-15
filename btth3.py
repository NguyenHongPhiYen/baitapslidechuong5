# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:15:26 2024

@author: Admin
"""

user_id=input("Nhập ID người dùng:")
password=input("Nhập mật khẩu:")
#ID USER
#Độ dài
if len(user_id) <6 or len(user_id) >24:
    print("Độ dài không phù hợp. Vui lòng kiểm tra lại!")
else:
    print("Hợp lệ")
#Ký tự đặc biệt
ktdb='!@#$%^&*()-=+'
x=True
for char in user_id:
  if char in ktdb:
    print("Ký tự không phù hợp. Vui lòng kiểm tra lại!", char)
    x=False
    break
if x:
    print("Hợp lệ")
#Khoảng trắng
if ' ' in user_id:
    print("Không được có khoảng trắng. Vui lòng nhập lại!")
else:
    print("Hợp lệ")
    
#PASSWORD
#Ít nhất 1 chữ cái nằm trong [a-z]
chuthuong="abcdefghijklmnopqrstuvwxyz"
x=False
for char in password:
    if char in chuthuong:
        x=True
        break
if x:
        print("Hợp lệ")
else:
        print("Không hợp lệ. Cấn ít nhất 1 chữ cái thường. Vui lòng kiểm tra lại!")
        
#Ít nhất 1 số từ [0-9]
so="123456789"
x=False
for char in password:
    if char in so:
        x=True
        break
if x:
        print("Hợp lệ")
else:
        print("Không hợp lệ. Cần có 1 chữ số. Vui lòng kiểm tra lại!")
        
#Ít nhất 1 chữ cái nằm trong [A-Z]
chuhoa="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x=False
for char in password:
    if char in chuhoa:
        x=True
        break
if x:
        print("Hợp lệ")
else:
        print("Không hợp lệ. Cần ít nhất 1 chữ cái thường. Vui lòng kiểm tra lại!")
        
#ít nhất 1 ký tự trong  [$ # @]
kytu= "$#@"
x=False
for char in password:
    if char in kytu:
        x=True
        break
if x:
        print("Hợp lệ")
else:
        print("Không hợp lệ. Cần ít nhất 1 ký tự trên. Vui lòng kiểm tra lại")
        
#Độ dài
if len(password) <6 or len(password) >24:
    print("Độ dài không phù hợp. Vui lòng kiểm tra lại!")
else:
    print("Hợp lệ")
    
    