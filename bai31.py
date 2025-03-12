# Bài 31: Mã hóa Caesar
message = input("Nhập tin nhắn cần mã hóa: ")
shift = 3
encrypted_message = ""

for char in message:
    if char.isalpha():
        shift_base = ord('A') if char.isupper() else ord('a')
        encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
    else:
        encrypted_message += char

print(f"Tin nhắn đã mã hóa: {encrypted_message}")