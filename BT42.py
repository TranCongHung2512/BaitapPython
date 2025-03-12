def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Nhập số và in kết quả
num = 8
print(factorial(num))
