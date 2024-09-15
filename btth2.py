# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:03:41 2024

@author: Admin
"""

email = input("Mời nhập email: ")

# Kiểm tra xem email có chứa "@" không
if "@" in email:
    # Tách chuỗi email thành 2 phần trước và sau "@"
    user, domain = email.split("@", 1)
    
    # Kiểm tra độ dài của phần trước "@"
    if len(user) < 6:
        print("Email không hợp lệ: phần trước @ phải có ít nhất 6 ký tự.")
    else:
        # Kiểm tra xem phần trước "@" có chứa khoảng trắng hoặc ký tự đặc biệt
        ktdb = "!@#$%^&*()-=+"
        x = True  # Biến để theo dõi tính hợp lệ
        for char in user:
            if char in ktdb or char == " ":
                x = False
                print("Email không hợp lệ: phần trước @ chứa ký tự đặc biệt hoặc khoảng trắng.")
                break
        
        if x:
            # Kiểm tra xem phần sau "@" có chứa dấu chấm "."
            if "." in domain:
                print(f"{email} là một email hợp lệ.")
            else:
                print("Email không hợp lệ: phần tên miền sau @ phải chứa dấu chấm.")
else:
    print("Email không hợp lệ: thiếu ký tự @.")