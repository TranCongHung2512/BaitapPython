# Kiểm tra Palindrome
# Nhập chuỗi từ người dùng
s = input("Nhập một chuỗi: ")

is_palindrome = True
n = len(s)

# Duyệt từ đầu đến giữa chuỗi
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_palindrome = False
        break

# Hiển thị kết quả
if is_palindrome:
    print(f"Chuỗi '{s}' là Palindrome.")
else:
    print(f"Chuỗi '{s}' không phải là Palindrome.")
