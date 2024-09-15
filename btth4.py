# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:16:41 2024

@author: Admin
"""

import random

luachon = ["Kéo", "Búa", "Bao"]

while True:
    #Máy chọn
    may = random.choice(luachon)
    
    # Người chọn
    nguoi = input("Chọn Kéo, Búa hoặc Bao (hoặc gõ 'Exit' để dừng): ")

    # Kiểm tra nếu người dùng muốn thoát
    if nguoi.lower() == 'thoát':
        print("Cảm ơn bạn đã chơi trò chơi!")
        break

    # Kiểm tra xem lựa chọn của người dùng có hợp lệ không
    if may not in luachon:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
        continue

    # In lựa chọn của máy và người chơi
    print(f"Bạn chọn: {nguoi}")
    print(f"Máy chọn: {may}")

    # Kiểm tra kết quả dựa trên quy tắc trò chơi
    if nguoi == may:
        print("Hòa!")
    elif (nguoi == "Kéo" and may == "Bao") or \
         (nguoi == "Búa" and may == "Kéo") or \
         (nguoi == "Bao" and may == "Búa"):
        print("Bạn thắng!")
    else:
        print("Máy thắng!")

    print("-" * 30)  # In dòng ngăn cách