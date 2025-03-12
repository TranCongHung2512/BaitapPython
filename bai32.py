# 32: Mã hóa và giải mã Caesar
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift_amount = shift if encrypt else -shift
            result += chr((ord(char) - shift_base + shift_amount) % 26 + shift_base)
        else:
            result += char
    return result

option = input("Bạn muốn mã hóa (E) hay giải mã (D)? ").strip().upper()
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

if option == 'E':
    print(f"Tin nhắn đã mã hóa: {caesar_cipher(message, shift, True)}")
elif option == 'D':
    print(f"Tin nhắn đã giải mã: {caesar_cipher(message, shift, False)}")
else:
    print("Lựa chọn không hợp lệ.")