def last_five_squares():
    squares = [i ** 2 for i in range(1, 21)]  # Tạo danh sách bình phương
    print(squares[-5:])  # In 5 phần tử cuối cùng

# Gọi hàm
last_five_squares()
