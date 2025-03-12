#Bài 53: Viết một hàm trả về một danh sách chứa mọi danh sách con có thể có của danh sách.
#Ví dụ: danh sách con của [1, 2, 3] là [], [1], [2], [3], [1, 2], [2, 3] và [1, 2, 3].

def all_subsets_recursive(lst):
    """Trả về danh sách chứa tất cả danh sách con của lst bằng đệ quy."""
    if not lst:
        return [[]]  # Trường hợp cơ bản: danh sách rỗng có một tập con là chính nó
    first = lst[0]
    rest_subsets = all_subsets_recursive(lst[1:])  # Gọi đệ quy với phần còn lại của danh sách
    return rest_subsets + [[first] + subset for subset in rest_subsets]  # Gộp tập con với first vào

# Chạy thử
print(all_subsets_recursive([1, 2, 3]))