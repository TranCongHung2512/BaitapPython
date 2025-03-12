# Tạo dictionary với (i, i*i)
# Đọc số nguyên n từ người dùng
n = int(input("Nhập số nguyên n: "))

# Tạo dictionary với key là i và value là i*i
square_dict = {i: i * i for i in range(1, n + 1)}

# Hiển thị dictionary
print("Dictionary tạo ra:", square_dict)
