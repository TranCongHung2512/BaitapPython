letter = input("Nhập một chữ cái: ").lower()

# Bài 27: Xác định tên hình dạng dựa trên số cạnh
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Chữ cái đã nhập là nguyên âm.")
elif letter == 'y':
    print("Chữ cái 'y' có thể là nguyên âm hoặc phụ âm.")
elif letter.isalpha() and len(letter) == 1:
    print("Chữ cái đã nhập là phụ âm.")
else:
    print("Vui lòng nhập một chữ cái hợp lệ.")

# Bài 27: Xác định tên hình dạng dựa trên số cạnh
shapes = {
    3: "Tam giác",
    4: "Tứ giác",
    5: "Ngũ giác",
    6: "Lục giác",
    7: "Thất giác",
    8: "Bát giác",
    9: "Cửu giác",
    10: "Thập giác"
}

num_sides = int(input("Nhập số cạnh của hình (từ 3 đến 10): "))
if num_sides in shapes:
    print(f"Hình có {num_sides} cạnh là {shapes[num_sides]}.")
else:
    print("Lỗi: Số cạnh phải nằm trong khoảng từ 3 đến 10.")