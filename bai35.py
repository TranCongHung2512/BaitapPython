# Tạo danh sách các số lẻ từ danh sách các số nhập vào
# Nhập danh sách số dưới dạng chuỗi, các số cách nhau bởi dấu phẩy
input_str = input("Nhập các số, cách nhau bởi dấu phẩy: ")

# Tách chuỗi và chuyển đổi từng phần tử thành số nguyên
numbers = [int(x.strip()) for x in input_str.split(',')]

# Tạo danh sách chứa các số lẻ
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

# Hiển thị kết quả
print("Danh sách các số lẻ:", odd_numbers)
