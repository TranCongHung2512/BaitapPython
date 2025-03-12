#Bài 51: Viết một hàm có một tham số password để xác định xem mật khẩu có tốt hay không.
#Một mật khẩu tốt là một mật khẩu dài ít nhất 8 ký tự và chứa ít nhất một chữ cái viết hoa, ít nhất một chữ cái viết thường
#và ít nhất một số. Hàm sẽ trả về True nếu mật khẩu là tốt, ngược thì nó sẽ trả về Fales.
#Chương trình có một chương trình chính đọc mật khẩu từ người dùng và hiển thị xem nó có tốt hay không.

def is_strong_password(password):
    """Kiểm tra mật khẩu có đủ mạnh hay không"""
    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)  # Kiểm tra chữ hoa
    has_lower = any(char.islower() for char in password)  # Kiểm tra chữ thường
    has_digit = any(char.isdigit() for char in password)  # Kiểm tra số

    return has_upper and has_lower and has_digit

# Chương trình chính
password = input("Nhập mật khẩu: ")

# Kiểm tra mật khẩu và hiển thị kết quả
if is_strong_password(password):
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu. Hãy sử dụng ít nhất 8 ký tự, bao gồm chữ hoa, chữ thường và số.")
