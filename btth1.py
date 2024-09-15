# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:24:51 2024

@author: Admin
"""

str_input=input("Mời nhập chuỗi:")
#Đếm độ dài chuỗi
len_str=0
for char in str_input:
    len_str +=1
print(f"Độ dài của chuỗi là:", len_str)

#Đếm và in các ký tự đặc biệt: ! @ # $ % ^ & * ( ) - = + . /
ky_tu_dac_biet="! @ # $ % ^ & * ( ) - = + . /"
count_ky_tu=0
for char in str_input:
    if char in ky_tu_dac_biet:
        print(f"Ký tự đặc biệt có trong chuỗi là: {char}")
        count_ky_tu +=1
print(f"Tổng ký tự đặc biệt có trong chuỗi là: {count_ky_tu}")

#Đếm và in các ký tự chữ cái từ [a-z]
chuthuong=" a b c d e f g h i j k l m n o p q r s t u v w x y z"
count_chuthuong=0
for char in str_input:
    if char in chuthuong:
     print(f"Ký tự chữ cái có trong chuỗi là: {char}")
     count_chuthuong +=1
print(f"Tổng ký tự chữ cái có trong chuỗi là: {count_chuthuong}")

#Đếm và in các ký tự chữ số [0-9]
chuso=" 0 1 2 3 4 5 6 7 8 9 "
count_so=0
for char in str_input:
    if char in chuso:
        print(f"Chữ số có trong chuỗi là: {char}")
        count_so +=1
print(f"Tổng chữ số có trong chuỗi là: {count_so}")

#Đếm và in các ký tự chữ cái [A-Z]
chuhoa=" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
count_chuhoa=0
for char in str_input:
    if char in chuhoa:
     print(f"Ký tự chữ cái có trong chuỗi là: {char}")
     count_chuhoa +=1
print(f"Tổng ký tự chữ cái có trong chuỗi là: {count_chuhoa}")