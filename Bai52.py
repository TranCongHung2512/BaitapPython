#Bài 52: Một số nguyên, n, được cho là hoàn hảo khi tổng của tất cả các ước số của n bằng n.
#Ví dụ, 28 là một số hoàn hảo vì các ước số của nó là 1, 2, 4, 7 và 14. Tổng 1 + 2 + 4 + 7 + 14 = 28.
#Viết hàm xác định xem số nguyên dương có hoàn hảo hay không.

def is_perfect(n):
    """Kiểm tra xem số n có phải là số hoàn hảo hay không."""
    if n < 2:
        return False  # Số nhỏ hơn 2 không thể là số hoàn hảo

    # Tính tổng các ước số thực sự của n (trừ chính nó)
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)

    return sum_divisors == n  # Nếu tổng ước số bằng n, đó là số hoàn hảo

# Chương trình chính: Tìm các số hoàn hảo từ 1 đến 10.000
print("Các số hoàn hảo từ 1 đến 10.000 là:")
for num in range(1, 10001):
    if is_perfect(num):
        print(num)