#Bài 54: Khi viết ra một danh sách các từ bằng tiếng Anh, người ta thường phân tách các từ bằng dấu phẩy.
#Ngoài ra, thêm từ “and” trước từ cuối cùng, trừ khi danh sách chỉ chứa một từ. Hãy xem xét bốn danh sách sau đây:
#	apples
#	apples and oranges
#	apples, oranges and bananas
#	apples, oranges, bananas and lemons
#Viết hàm lấy danh sách các chuỗi làm tham số của nó. Hàm sẽ trả về một chuỗi chứa tất cả các từ trong danh sách,
#được định dạng theo cách được mô tả như trên. Hàm hoạt động cho danh sách có độ dài bất kỳ.
#Code bao gồm một chương trình chính đọc một số từ do người dùng nhập vào,
#định dạng chúng bằng cách gọi hàm và sau đó hiển thị kết quả mà hàm trả về

def format_word_list(words):
    """Định dạng danh sách từ theo kiểu tiếng Anh (dùng dấu phẩy và 'and')."""
    if not words:
        return ""  # Trả về chuỗi rỗng nếu danh sách trống
    elif len(words) == 1:
        return words[0]  # Nếu chỉ có 1 từ, trả về từ đó
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]  # Ghép các từ theo định dạng yêu cầu

# Chương trình chính
words = input("Nhập danh sách từ, cách nhau bởi dấu cách: ").split()  # Nhập và tách thành danh sách

formatted_string = format_word_list(words)  # Gọi hàm để định dạng
print("Danh sách định dạng:", formatted_string)