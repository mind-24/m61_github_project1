def calculate_net_salary():
    print("=== โปรแกรมคำนวณเงินเดือนสุทธิ (หักภาษี 3%) ===")
    
    try:
        # 1. รับค่าเงินเดือนจากผู้ใช้
        salary = float(input("กรุณากรอกเงินเดือนของคุณ (บาท): "))
        
        if salary < 0:
            print("❌ กรุณากรอกจำนวนเงินที่มากกว่าหรือเท่ากับ 0")
            return

        # 2. คำนวณภาษี 3% และเงินคงเหลือ
        tax = salary * 0.03
        net_salary = salary - tax

        # 3. แสดงผลลัพธ์
        print("-" * 40)
        print(f"💰 เงินเดือนต้น:    {salary:,.2f} บาท")
        print(f"📉 ภาษีที่หัก (3%):  {tax:,.2f} บาท")
        print(f"✨ เงินเดือนสุทธิ:   {net_salary:,.2f} บาท")
        print("-" * 40)
        
    except ValueError:
        print("❌ ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น")

# รันโปรแกรม
if __name__ == "__main__":
    calculate_net_salary()