#Bài 49: Số nguyên tố là một số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính nó.
#Viết hàm xác định tham số của nó có phải là số nguyên tố hay không, trả về True nếu đúng và False nếu không phải.
#Viết chương trình chính đọc số nguyên từ người dùng và hiển thị thông báo cho biết đó có phải là số nguyên tố hay không.

def is_prime(n):
    """Kiểm tra số nguyên tố"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra đến căn bậc hai của n
        if n % i == 0:
            return False
    return True

# Chương trình chính
num = int(input("Nhập một số nguyên: "))

# Gọi hàm kiểm tra và hiển thị kết quả
if is_prime(num):
    print(f"{num} là số nguyên tố.")
else:
    print(f"{num} không phải là số nguyên tố.")