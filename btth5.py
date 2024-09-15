# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:23:18 2024

@author: Admin
"""

import random

# Danh sách các lựa chọn
luachon = ["Kéo", "Búa", "Bao"]

# Tạo số lượng người chơi ngẫu nhiên từ 8 đến 20
so_luong_nguoi_choi = random.randint(8, 20)

# Tạo danh sách người chơi và lựa chọn của họ
nguoi_choi = []
choices = []

for i in range(so_luong_nguoi_choi):
    player_name = f"Người chơi {i + 1}"
    player_choice = random.choice(luachon)
    nguoi_choi.append(player_name)
    choices.append(player_choice)

# In ra số lượng người chơi và lựa chọn của họ
print(f"Số người chơi: {so_luong_nguoi_choi}\n")
for i in range(so_luong_nguoi_choi):
    print(f"{nguoi_choi[i]} chọn: {choices[i]}")

# Tìm người chiến thắng
kéo_count = choices.count("Kéo")
búa_count = choices.count("Búa")
bao_count = choices.count("Bao")

# Kiểm tra trường hợp hòa (nếu tất cả cùng chọn 1 loại)
if kéo_count == so_luong_nguoi_choi or búa_count == so_luong_nguoi_choi or bao_count == so_luong_nguoi_choi:
    print("\nTất cả người chơi đã chọn giống nhau, trận đấu hòa!")
else:
    # Xác định chiến thắng dựa trên số lượng
    if kéo_count > 0 and bao_count > 0 and búa_count == 0:
        print("\nKéo thắng vì có nhiều người chọn Kéo và không ai chọn Búa!")
    elif búa_count > 0 and kéo_count > 0 and bao_count == 0:
        print("\nBúa thắng vì có nhiều người chọn Búa và không ai chọn Bao!")
    elif bao_count > 0 and búa_count > 0 and kéo_count == 0:
        print("\nBao thắng vì có nhiều người chọn Bao và không ai chọn Kéo!")
    else:
        # Nếu có tất cả các lựa chọn, sử dụng quy tắc
        if kéo_count > bao_count and kéo_count > búa_count:
            print("\nKéo thắng vì có nhiều người chọn Kéo hơn!")
        elif búa_count > kéo_count and búa_count > bao_count:
            print("\nBúa thắng vì có nhiều người chọn Búa hơn!")
        elif bao_count > kéo_count and bao_count > búa_count:
            print("\nBao thắng vì có nhiều người chọn Bao hơn!")
        else:
            print("\nKhông có kết quả rõ ràng, có thể cần thêm vòng chơi khác!")
