# Bài 30: Xác định năm nhuận
year = int(input("Nhập một năm: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")