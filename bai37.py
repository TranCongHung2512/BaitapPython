# Tạo danh sách rỗng để lưu các từ duy nhất
unique_words = []

# Đọc từ người dùng cho đến khi gặp dòng trống
while True:
    word = input("Nhập từ (để trống để dừng): ")
    if word == "":
        break
    # Nếu từ chưa có trong danh sách, thêm vào
    if word not in unique_words:
        unique_words.append(word)

# Hiển thị các từ duy nhất theo thứ tự đã nhập
print("\nCác từ đã nhập (không trùng lặp):")
for w in unique_words:
    print(w)
