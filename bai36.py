# Đọc các số nguyên, dừng khi nhập 0, sau đó hiển thị theo thứ tự tăng dần
# Tạo danh sách rỗng
numbers = []

while True:
    num = int(input("Nhập một số nguyên (nhập 0 để dừng): "))
    if num == 0:
        break
    numbers.append(num)

# Sắp xếp danh sách theo thứ tự tăng dần
numbers.sort()

# Hiển thị kết quả
print("Các số đã nhập theo thứ tự tăng dần:")
for number in numbers:
    print(number)
