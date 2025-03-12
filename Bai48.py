#Bài 48: Viết hàm có 03 tham số và trả về giá trị trung bình của các tham số đó.
#Bao gồm một chương trình chính đọc ba giá trị từ người dùng và hiển thị giá trị trung bình của chúng.

def average(a, b, c):
    return (a + b + c) / 3  # Tính trung bình cộng

# Chương trình chính
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Gọi hàm và in kết quả
avg = average(num1, num2, num3)
print(f"Giá trị trung bình của {num1}, {num2}, {num3} là: {avg}")