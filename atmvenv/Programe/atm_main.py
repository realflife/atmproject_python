#Main Program

from setting import get_db_connection as getdb
import login as ln
import feature as ft
import time
if __name__ == "__main__":
    print("Welcom to My bank")
    ln.showlog()
    while True:
        try:
            choice = int(input("กรุณกาเลือกบริการที่ต้องการใช้งาน : "))
        except ValueError:
            print("เกิดข้อผิดพลาด,กรุณากรอกตัวเลขจำนวนเต็มเท่านั้น")
        else:
             if choice >=1 and choice <=3:
                if choice == 1:
                    print("คุณยังไม่มีบัญชี! สมัครเลย!!")
                    ln.register()
                    current_user = ln.login()
                    break
                elif choice == 2:
                    print("คุณมีบัญชีแล้ว ล็อกอินเลย!!")
                    current_user = ln.login()
                    break
                elif choice == 3:
                    print("ขอบคุณที่ใช้บริการ")
                    exit()
             else:
                print("กรุณาใส่แค่ตัวเลข [1-3] เท่านั้น")

    acc_bank_id = ln.get_user_bank_id(current_user)
    while True:
        while True:
            try :
                b_id = input("Enter Your Bank ID : ") 
                if not b_id.isdigit:
                    raise ValueError("กรุณากรอกชนิดข้อมูลที่เป็นตัวเลขเท่านั้น")
                if b_id != acc_bank_id:
                    raise ValueError("เกิดข้อผิดพลาด\nเลขบัญชีของคุณไม่ถูกต้อง,กรุณาลองใหม่")
            except ValueError as ve:
                print(ve)
            else:
                print("Bank ID verified successfully.")
                break
        while True:
            ft.showmenu()
            try:
                choice_menu = int(input("กรุณาเลือกเมนูที่คุณต้องการใช้บริการ [1-5] : "))
                if choice_menu >=1 and choice_menu <= 5:
                    if choice_menu == 1:
                        while True:
                            print("คุณเลือกบริการฝากเงิน")
                            try:
                                money = int(input("กรอกจำนวนเงินที่ต้องการฝาก : "))
                                break
                            except ValueError:
                                print("เกิดขอผิดพลาด!!")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น")
                                time.sleep(2)
                        ft.deposit(b_id,money)
                        ft.show_alternate()
                        while True:
                            try:
                                choice_alternate = int(input("คุณต้องการทำธุรกรรมอื่นๆต่อหรือไม่ : "))
                                if choice_alternate == 1 or choice_alternate == 0:
                                    if choice_alternate == 1:
                                        break
                                    elif choice_alternate == 0:
                                        print("ขอบคุณที่ใช้บริการ\n")
                                        time.sleep(0.5)
                                        print("ออกจากระบบ...")
                                        time.sleep(1)
                                        exit()
                                else:
                                    print("กรุณากรอกเลข [1] หรือ 0 เท่านั้น")
                                    time.sleep(1)
                            except ValueError:
                                print("เกิดขอผิดพลาด!!")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น\n")
                                time.sleep(0.5)

                    elif choice_menu == 2:
                        while True:
                            print("คุณเลือกบริการถอนเงิน")
                            try:
                                money = int(input("กรอกจำนวนเงินที่ต้องการถอน : "))
                                break
                            except ValueError:
                                print("เกิดข้อผิดพลาด")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น")
                                time.sleep(2)
                        ft.withdraw(b_id,money)
                        ft.show_alternate()
                        while True:
                            try:
                                choice_alternate = int(input("คุณต้องการทำธุรกรรมอื่นๆต่อหรือไม่ : "))
                                if choice_alternate == 1 or choice_alternate == 0:
                                    if choice_alternate == 1:
                                        break
                                    elif choice_alternate == 0:
                                        print("ขอบคุณที่ใช้บริการ\n")
                                        time.sleep(0.5)
                                        print("ออกจากระบบ...")
                                        time.sleep(1)
                                        exit()
                                else:
                                    print("กรุณากรอกเลข [1] หรือ 0 เท่านั้น")
                                    time.sleep(1)
                            except ValueError:
                                print("เกิดขอผิดพลาด!!")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น\n")
                                time.sleep(0.5)
                    elif choice_menu == 3:
                        print("คุณเลือกเมนู เช็คยอดเงิน")
                        ft.display_balance(b_id)
                        ft.show_alternate()
                        while True:
                            try:
                                choice_alternate = int(input("คุณต้องการทำธุรกรรมอื่นๆต่อหรือไม่ : "))
                                if choice_alternate == 1 or choice_alternate == 0:
                                    if choice_alternate == 1:
                                        break
                                    elif choice_alternate == 0:
                                        print("ขอบคุณที่ใช้บริการ\n")
                                        time.sleep(0.5)
                                        print("ออกจากระบบ...")
                                        time.sleep(1)
                                        exit()
                                else:
                                    print("กรุณากรอกเลข [1] หรือ 0 เท่านั้น")
                                    time.sleep(1)
                            except ValueError:
                                print("เกิดขอผิดพลาด!!")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น\n")
                                time.sleep(0.5)

                    elif choice_menu == 4:
                        print("คุณเลือกเมนู ดูข้อมูลเบื้องต้นของบัญชี")
                        time.sleep(1.5)
                        ft.show_info(b_id)
                        ft.show_alternate()
                        while True:
                            try:
                                choice_alternate = int(input("คุณต้องการทำธุรกรรมอื่นๆต่อหรือไม่ : "))
                                if choice_alternate == 1 or choice_alternate == 0:
                                    if choice_alternate == 1:
                                        break
                                    elif choice_alternate == 0:
                                        print("ขอบคุณที่ใช้บริการ\n")
                                        time.sleep(0.5)
                                        print("ออกจากระบบ...")
                                        time.sleep(1)
                                        exit()
                                else:
                                    print("กรุณากรอกเลข [1] หรือ 0 เท่านั้น")
                                    time.sleep(1)
                            except ValueError:
                                print("เกิดขอผิดพลาด!!")
                                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น\n")
                                time.sleep(0.5)
                    elif choice_menu == 5:
                        print("คุณเลือกเมนู ออก")
                        time.sleep(0.5)
                        print("ขอบคุณที่ใช้บริการ")
                        time.sleep(1)
                        exit()
                else :
                    print("เกิดข้อผิดพลาด!!")
                    print("กรุณากรอกเลขจำนวนเต็มระหว่าง [1-5] เท่านั้น")
                    time.sleep(2)
            except ValueError:
                print("เกิดขอผิดพลาด!!")
                print("ไม่สามารถกรอกตัวหนังสือหรือเลขทศนิยมได้,กรุณากรอกข้อมูลในรูปแบบจำนวนเต็มเท่านั้น")
                time.sleep(2)