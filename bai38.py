# Sắp xếp số theo nhóm (âm, không, dương)
# Danh sách chứa tất cả các số được nhập
numbers = []

# Đọc số nguyên cho đến khi nhập dòng trống
while True:
    s = input("Nhập số nguyên (dòng trống để dừng): ")
    if s == "":
        break
    try:
        num = int(s)
        numbers.append(num)
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

# Tách số theo nhóm
negatives = [num for num in numbers if num < 0]
zeros = [num for num in numbers if num == 0]
positives = [num for num in numbers if num > 0]

# Nối các danh sách theo thứ tự: âm, 0, dương
ordered_numbers = negatives + zeros + positives

# Hiển thị kết quả
print("\nKết quả sau khi sắp xếp:")
print(" ".join(str(num) for num in ordered_numbers))
