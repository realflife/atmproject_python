#Feature

from setting import get_db_connection as getdb


def read_balance(b_id):
    con = getdb()
    cur = con.cursor()
    cur.execute("SELECT `balance` FROM user_db WHERE %s = `Bank_id`",(b_id))
    balance = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    return balance[0]


def showmenu():
    print("=====Menu====")
    print("1.ฝากเงิน")
    print("2.ถอนเงิน")
    print("3.เช็คยอดเงิน")
    print("4.ดูข้อมูลเบื้องต้นของบัญชี")
    print("5.ออก")

def write_balance(b_id,new_balance) :
    con = getdb()
    cur = con.cursor()
    cur.execute("UPDATE user_db SET balance = %s WHERE Bank_id = %s",(new_balance,b_id))
    con.commit()
    cur.close()
    con.close()

def deposit(b_id,money):
    balance = read_balance(b_id)
    balance += money
    write_balance(b_id,balance)
    print("คุณฝากเงินจำนวน ",money," บาท")
    print(f"คุณมียอดเงินคงเหลือ {balance} บาท")

def withdraw(b_id,money):
    balance = read_balance(b_id)
    balance -= money
    write_balance(b_id,balance)
    print(f"คุณถอนเงินจำนวน {money} บาท")
    print(f"คุณมียอดเงินคงเหลือ {balance} บาท")

def  display_balance(b_id):
    balance = read_balance(b_id)
    print(f"คุณมียอดเงินคงเหลือ  {balance} บาท")

def show_info(b_id):
    con = getdb()
    cur = con.cursor()
    cur.execute("SELECT * FROM user_db WHERE Bank_id = %s ",(b_id))
    rows = cur.fetchone()
    print("=====Account Info======")
    print(f"Bank ID\t : {rows[5]}")
    print(f"Name\t : {rows[3]} {rows[4]}")
    print(f"Gender\t : {rows[8]}")
    print(f"Current Balance\t : {rows[6]}")
    print(f"Create at\t : {rows[7]}")
    print(f"Account Status\t : {rows[9]}")
    

def show_alternate():
    print("หากคุณต้องการทำธุรกรรมอื่นๆต่อ [1]")
    print("หากคุณไม่ต้องการทำธุรกรรมอื่นและออกจากระบบกด [0]")




