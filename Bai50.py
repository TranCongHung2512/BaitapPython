#Bài 50: Viết hàm không có tham số để tạo mật khẩu ngẫu nhiên. Mật khẩu phải có độ dài ngẫu nhiên từ 7 đến 10 ký tự.
#Mỗi ký tự phải được chọn ngẫu nhiên từ các vị trí 33 đến 126 trong bảng ASCII. Hàm sẽ trả về mật khẩu được tạo ngẫu nhiên.
#Hiển thị mật khẩu được tạo ngẫu nhiên trong chương trình chính.

import random

def generate_password():
    """Tạo mật khẩu ngẫu nhiên có độ dài từ 7 đến 10 ký tự"""
    length = random.randint(7, 10)  # Chọn độ dài ngẫu nhiên từ 7 đến 10
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))  # Tạo mật khẩu ngẫu nhiên
    return password

# Chương trình chính
random_password = generate_password()
print(f"Mật khẩu ngẫu nhiên: {random_password}")