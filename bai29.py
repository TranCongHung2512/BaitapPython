# Bài 29: Phân loại tam giác
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều.")
    elif a == b or a == c or b == c:
        print("Tam giác cân.")
    else:
        print("Tam giác thường.")
else:
    print("Ba cạnh nhập vào không tạo thành tam giác.")