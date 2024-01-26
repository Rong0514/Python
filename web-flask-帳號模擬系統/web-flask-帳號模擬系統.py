from flask import Flask
from flask import request
from flask import session
from flask import make_response
from flask import render_template
from flask_mail import Mail, Message
from check_user_re import check_user
from check_password_re import check_password
import os 
import random
import sqlite3
import webbrowser
from datetime import datetime

app = Flask(__name__)

MAIL_USERNAME = input('請輸入寄出信箱Mail : ')
MAIL_PASSWORD = input('請輸入應用程式密碼 : ')
global MAIL_USERNAME , MAIL_PASSWORD

app.config['MAIL_SERVER']   = 'smtp.gmail.com'
app.config['MAIL_PORT']     = 465
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS']  = False
app.config['MAIL_USE_SSL']  = True
mail = Mail(app)

app.secret_key = 'Rong secret key'

db_name        = 'shopping.db'
db_exists      = os.path.exists(db_name)
conn = sqlite3.connect('shopping.db')
if db_exists  == True:
    print("Database file exists, opened successfully.")
else:
    sql = "CREATE TABLE 'account' ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'name' TEXT, 'birthday' TEXT, 'sex' TEXT, 'email' TEXT, 'user' TEXT, 'password' TEXT, 'verify' TEXT);"
    conn.execute(sql)
    conn.commit()
conn.close()

'''____________________________________________________________0.連接登入註冊'''
@app.route('/home')
def home():
    return render_template('home.html')


'''________________________________________________________________1.檢查登入'''
@app.route('/check-login')
def check_login():
    if session.get('user') == None and session.get('password') == None and session.get('logined') == '1':
        return render_template('login_successfully.html')
    else:
        userID = request.cookies.get('userID')
        if userID == None:
            return render_template('login_form.html')
        else:
            return render_template('login_form.html' , userID = userID)
    
    
'''____________________________________________________________2.接收登入表單'''
@app.route('/login_form' ,  methods = ['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        user     = request.form.get('user')
        password = request.form.get('password')
        conn     = sqlite3.connect('shopping.db')
        cursor   = conn.cursor()
        sql      = "select user from account where user = ?"
        cursor.execute(sql, (user,))
        data     = cursor.fetchone()
        if data != None:
            sql      = "select user, password, verify from account where user = ? and password = ?"
            cursor.execute(sql, (user , password))
            data     = cursor.fetchone()
            if data != None:
                if data[2] == '1':
                    session['user']     = user
                    session['password'] = password
                    resp   = make_response(render_template("login_successfully.html"))
                    resp.set_cookie('userID'  , user)
                    return resp
                else:
                    msg = '您尚未驗證'
                    return render_template('login_verify.html')
            else:
                userID = request.cookies.get('userID')
                msg = '請輸入6-20碼英數字密碼'
                if userID != None:
                    return render_template('login_form.html' , message = msg , userID = userID)
                else:
                    return render_template('login_form.html' , message = msg)
        else:
            msg = '此用戶不存在'
            return render_template('login_form.html' , message = msg)
    else:
        return render_template('sginup_form.html')
    conn.close()
        

'''____________________________________________________________3.前往註冊表單'''
@app.route('/sginup')
def sginup():
    return render_template('sginup_form.html')


'''____________________________________________________________4.接收註冊表單'''
@app.route('/sginup_form' ,  methods = ['GET', 'POST'])
def sginup_form():
    if request.method == 'POST':
        name     = request.form.get('name')
        sex      = request.form.get('sex')
        email    = request.form.get('email')
        birthday = request.form.get('birthday')
        user     = request.form.get('user')
        password = request.form.get('password2')
        now = datetime.now()
        birthday_verify = datetime.strptime(birthday, "%Y-%m-%d")
        age = now.year - birthday_verify.year - ((now.month, now.day) < (birthday_verify.month, birthday_verify.day))
        if age >= 18:
            user_check  = check_user(user)
            if user_check == None:
                conn      = sqlite3.connect('shopping.db')
                cursor    = conn.cursor()
                sql       = "select user from account where user = ?"
                cursor.execute(sql, (user,))
                data      = cursor.fetchone()
                if data   == None:
                    password_check = check_password(password)
                    if password_check == None:
                        conn     = sqlite3.connect('shopping.db')
                        cursor   = conn.cursor()
                        sql      = "select email from account where email = ?"
                        cursor.execute(sql, (email,))
                        data     = cursor.fetchone()
                        if data is None:
                            sql = "insert into account (name, sex, email, birthday, user, password, verify) values (?, ?, ?, ?, ?, ?, '0')"
                            cursor.execute(sql, (name, sex, email, birthday, user, password))
                            conn.commit()
                            msg = '註冊成功'
                            session['email'] = email
                            return render_template('sginup_successfully.html',msg=msg,name=name,sex=sex,email=email,birthday=birthday,user=user,password=password,verify='未驗證')
                        else: 
                            msg = '此信箱已被註冊'
                            return render_template('sginup_form.html' , msg = msg)
                    else:
                        return render_template('sginup_form.html' , msg = password_check)
                else:
                    msg = '此用戶已被註冊'
                    return render_template('sginup_form.html', msg = msg)
            else:
                return render_template('sginup_form.html', msg = user_check)
        else:
            msg = '您未滿18歲'
            return render_template('sginup_form.html' , msg = msg)
    else:
        return render_template('sginup_form.html')
    conn.close()
    
    
'''____________________________________________________________5-1.寄送驗證碼'''
@app.route('/sendverify/')
def sendverify():
    email = session.get('email')
    verify_number_start = str(random.randint(1000 , 9999))
    session['verify_number_start'] = verify_number_start
    msg      = Message(subject='驗 證', sender = MAIL_USERNAME , recipients = [email])
    msg.body = '你的驗證碼是 {}'.format(verify_number_start)
    msg.html = render_template('email_template.html' , verify_number_start = verify_number_start)  
    try :
        mail.send(msg)
        return render_template('sendverifydone.html')
    except Exception :
        return render_template('verifyfail.html')
    
    
'''_________________________________________________________5-2.手動寄送驗證碼'''
@app.route('/loginverify/' , methods = ['GET', 'POST'])
def loginverify():
    if request.method == 'POST':
        email = request.form.get('email')
        session['email'] = email
        verify_number_start = str(random.randint(1000 , 9999))
        session['verify_number_start'] = verify_number_start
        msg = Message(subject='驗 證', sender='willy1012374@gmail.com' , recipients=[email])
        msg.body = '你的驗證碼是 {}'.format(verify_number_start)
        msg.html = render_template('email_template.html' , verify_number_start=verify_number_start)  
        try :
            mail.send(msg)
            return render_template('sendverifydone.html')
        except Exception :
            return '驗證碼發送失敗'


'''___________________________________________________________6.輸入驗證碼畫面'''
@app.route('/verify_form')
def verify_form():
    return render_template('verify_form.html')


'''_____________________________________________7.接收驗證碼資訊更新sql_verify'''
@app.route('/getverify' ,  methods = ['POST'])
def getverify():
    email                = session.get('email')
    verify_number_start  = session.get('verify_number_start')
    verify_number_ending = request.form.get('verify_number_ending')
    if verify_number_start == verify_number_ending:
        conn     = sqlite3.connect('shopping.db')
        cursor   = conn.cursor()
        sql      = "update account set verify=1 where email='{}'".format(email)
        cursor.execute(sql)
        conn.commit()
        return render_template('verifysuccessfully.html')
    else:
        msg = '驗 證 碼 錯 誤'
        return render_template('verify_form.html' , msg = msg)
    session.pop('email'               , None)   
    session.pop('verify_number_start' , None)  
    conn.close()
    

'''___________________________________________________________________8.登出'''
@app.route('/logout')
def logout():
    session.pop('user'      , None)
    session.pop('paswsword' , None)
    return render_template('logout.html')


if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/home")
    app.run(debug=True, use_reloader=False)
