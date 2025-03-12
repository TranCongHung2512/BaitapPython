# Chuyển đổi số thập phân sang nhị phân
# Nhập số thập phân từ người dùng
decimal = int(input("Nhập số thập phân: "))

if decimal == 0:
    binary = "0"
else:
    binary = ""
    num = decimal
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary  # ghép phần dư vào đầu chuỗi
        num //= 2

# Hiển thị kết quả
print(f"Số {decimal} chuyển thành nhị phân là: {binary}")
