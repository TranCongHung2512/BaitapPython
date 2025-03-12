import matplotlib.pyplot as plt

# Dữ liệu
weeks = [1, 2, 3, 4]
bcws = [1500, 4650, 8550, 10000]
bcwp = [0, 3900, 0, 0]  # Giá trị tuần 1, 3, 4 chưa có
acwp = [0, 4000, 0, 0]  # Giá trị tuần 1, 3, 4 chưa có

# Vẽ biểu đồ Earned Value
plt.figure(figsize=(8, 5))
plt.plot(weeks, bcws, marker='o', linestyle='-', color='blue', label='BCWS (Planned Value)')
plt.plot(weeks, bcwp, marker='s', linestyle='--', color='orange', label='BCWP (Earned Value)')
plt.plot(weeks, acwp, marker='^', linestyle=':', color='red', label='ACWP (Actual Cost)')

# Định dạng biểu đồ
plt.xlabel("Tuần")
plt.ylabel("Chi phí ($)")
plt.title("Earned Value Chart")
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()
