# โปรแกรมคำนวณ BMI

print("=================================")
print("      โปรแกรมคำนวณ BMI")
print("=================================")

# รับน้ำหนักและส่วนสูง
weight = float(input("กรุณากรอกน้ำหนัก (กิโลกรัม):  "))
height = float(input("กรุณากรอกส่วนสูง (เมตร): "))

# คำนวณ BMI
bmi = weight / (height ** 2)

# แสดงค่า BMI
print("\n===== ผลการคำนวณ =====")
print(f"BMI ของคุณ = {bmi:.2f}")

# แปลผลสุขภาพ
if bmi < 18.5:
    health = "น้ำหนักต่ำกว่าเกณฑ์"
elif bmi < 25:
    health = "น้ำหนักปกติ"
elif bmi < 30:
    health = "น้ำหนักเกิน"
else:
    health = "โรคอ้วน"

print("ผลสุขภาพ =", health)