# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:37:54 2024

@author: Admin
"""

import random

# Số lượng vé số người chơi mua
num_tickets = int(input("Nhập số lượng vé số người chơi mua: "))

# Tạo danh sách để chứa các vé số người chơi
tickets = []

# Tạo vé số người chơi
for _ in range(num_tickets):
    ticket = sorted(random.sample(range(1, 46), 6))  # Tạo vé số với 6 số không trùng nhau
    tickets.append(ticket)

# Tạo dãy số trúng
winning_numbers = sorted(random.sample(range(1, 46), 6))

# In dãy số trúng
print(f"Dãy số trúng: {winning_numbers}")

# Giá bán mỗi vé
ticket_price = 10_000

# Khởi tạo tổng số tiền người chơi nhận được
total_prize = 0

# Duyệt qua từng vé số
for ticket in tickets:
    # Tính số lượng số trùng khớp
    matches = len(set(ticket) & set(winning_numbers))
    
    # Tính tiền thưởng dựa trên số lượng số trùng khớp
    if matches == 6:
        prize = 10_000_000_000
    elif matches == 5:
        prize = 10_000_000
    elif matches == 4:
        prize = 300_000
    elif matches == 3:
        prize = 30_000
    else:
        prize = 0
    
    # Cộng tiền thưởng vào tổng tiền thưởng
    total_prize += prize
    
    # In kết quả cho từng vé
    print(f"Vé số: {ticket} - Số trùng khớp: {matches} - Tiền thưởng: {prize}")

# Tổng số tiền người chơi đã chi
total_spent = num_tickets * ticket_price

# In tổng số tiền người chơi đã chi và nhận được
print(f"\nTổng số tiền người chơi đã chi: {total_spent} đ")
print(f"Tổng số tiền người chơi nhận được: {total_prize} đ")
