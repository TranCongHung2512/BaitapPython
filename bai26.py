letter = input("Nhập một chữ cái: ").lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print("Chữ cái đã nhập là nguyên âm.")
elif letter == 'y':
    print("Chữ cái 'y' có thể là nguyên âm hoặc phụ âm.")
elif letter.isalpha() and len(letter) == 1:
    print("Chữ cái đã nhập là phụ âm.")
else:
    print("Vui lòng nhập một chữ cái hợp lệ.")