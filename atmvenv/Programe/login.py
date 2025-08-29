#login & register

from setting import get_db_connection as get_db


def register():
    print("=======Regirster Menu======")
    while True:
        username = input("Enter Username : ")
        con =get_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM user_db WHERE username = %s",(username))
        result = cur.fetchone()
        if result:
            print("User already exists")
            cur.close()
            con.close()
        else:
            cur.close()
            con.close()
            break
    allowed_gender = ("M","F","U")
    password = input("Enter password : ")
    f_name = input("Enter Firsname : ")
    l_name = input("Enter Lastname : ")
    while True:
        try:
            gender = input("กรุณากรอกเพศของคุณ [M:เพศชาย / N:เพศหญิง / U = เพศทางเลือก] : ").strip()
            if gender not in allowed_gender:
                raise ValueError("กรุณากรอกข้อมูลที่เป็นตัวอักษรและเป็นตัวอักษร [M:F:U] เท่านั้น")
        except ValueError as v:
            print(v)
        else:
            break
    
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT `Bank_id` FROM user_db ORDER BY id DESC LIMIT 1",)
    result = cur.fetchone()
    if result:
        new_number = int(result[0]) + 1
    else :
        new_number = '700512001'
    acc_id = str(new_number)
    cur.execute("INSERT INTO user_db (username,password,first_name,last_name,Bank_id,balance,gender) VALUES(%s,%s,%s,%s,%s,0,%s)",(username,password,f_name,l_name,acc_id,gender))
    con.commit()
    cur.close()
    con.close()
    print(f"Bank ID ของคุณคือ : {acc_id}")
    print("Register Successful")
    
def login():
    print("======LOGIN======")
    while True:
        username = input("Enter Username : ")
        pass_word = input("Enter Password : ")
        con = get_db()
        cur = con.cursor()
        cur.execute("SELECT* FROM user_db WHERE username = %s AND password = %s",(username,pass_word))
        result = cur.fetchone()
        cur.close()
        con.close()


        if result:
            print("Login Successful")
            print(f"Welcome {username}")
            print(f"Account Name: {result[3]} {result[4]}")
            return username
        else:
            print("Error Username or password is invalid\nTry again\n")


def showlog():
    print("หากคุณยังไม่มีบัญชี กด [1] เพื่อ สมัครบัญชี")
    print("หากคุณมีบัญชีแล้ว กด [2] เพื่อ Login")
    print("กด [3] หากต้องการออกจากระบบ")

def get_user_bank_id(username):
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT `Bank_id` FROM user_db WHERE %s = `username`",(username))
    result = cur.fetchone()
    if result:
        for item in result:
            return item
    else :
        None
    cur.close()
    con.close()

