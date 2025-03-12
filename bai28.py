# Bài 28: Xác định số ngày trong một tháng
days_in_month = {
    "january": 31, "february": "28 hoặc 29", "march": 31, "april": 30,
    "may": 31, "june": 30, "july": 31, "august": 31,
    "september": 30, "october": 31, "november": 30, "december": 31
}

month = input("Nhập tên tháng: ").strip().lower()
if month in days_in_month:
    print(f"Tháng {month.capitalize()} có {days_in_month[month]} ngày.")
else:
    print("Lỗi: Vui lòng nhập một tháng hợp lệ.")