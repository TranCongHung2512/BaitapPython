#Bài 47: Định nghĩa một hàm có thể tạo danh sách chứa giá trị bình phương của các số từ 1 đến 20
#(bao gồm cả 1 và 20). Sau đó in tất cả các giá trị của danh sách trừ 5 phần tử đầu tiên.

def generate_square_list():
    squares = [x**2 for x in range(1, 21)]  # Tạo danh sách bình phương từ 1 đến 20
    print(squares[5:])  # In tất cả phần tử trừ 5 phần tử đầu tiên

generate_square_list()