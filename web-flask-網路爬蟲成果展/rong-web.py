import db
import webbrowser
from datetime import datetime
from flask_paginate import Pagination
from flask import Flask,render_template,request,redirect,url_for              

app = Flask(__name__)                                                        

'''______________________________________________________________________首頁'''
@app.route('/home')
def HOME():
    
    sql = "select title,link_url,photo_url,star from jpfoods where platform = '大阪' order by star desc limit 13"
    db.cursor.execute(sql)
    jpfoods = db.cursor.fetchall()
    sql = "select title,link_url,photo_url from ifoods where platform = '愛食記' order by id asc limit 10"
    db.cursor.execute(sql)
    ifoods1 = db.cursor.fetchall()
    sql = "select title,link_url,photo_url from ifoods where platform = '愛食記' order by id desc limit 11"
    db.cursor.execute(sql)
    ifoods2 = db.cursor.fetchall()
    sql = "select title,link_url,photo_url from travel where platform = '東京' order by id asc limit 12"
    db.cursor.execute(sql)
    travel = db.cursor.fetchall()
    return render_template('HOME.html',**locals())


'''____________________________________________________________________愛食記'''
@app.route('/ifoods')
def ifoods():
    
    page = int(request.args.get('page',1))
    sql = "select count(*) as c from ifoods"                                 
    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()                                          
    count = int(datacount[0])
    if page == 1:
        sql  = "select title,link_url,photo_url,address from ifoods order by id desc limit 20"
    else:
        startp = page-1
        sql  = "select title,link_url,photo_url,address from ifoods limit {},{}".format(startp*20,20)
                                                                                # 頁數*36 = 初始筆數
    db.cursor.execute(sql)
    ifood = db.cursor.fetchall()
    pagination = Pagination (page = page, total = count , per_page = 20)
                   # 使用函式    頁數           總比數          以20筆為分頁
    return render_template('ifoods.html',**locals())


'''__________________________________________________________________日本美食'''
@app.route("/jpfoods")
def jpfoods():
    
    p = request.args.get('p', '')
    if len(p) == 0:
        sql = "select title,link_url,photo_url,star from jpfoods order by star desc"
    else:
        sql = "select title,link_url,photo_url,star from jpfoods where platform = '{}'".format(p)
    db.cursor.execute(sql)
    jpfood = db.cursor.fetchall()
    return render_template("jpfoods.html", **locals())


'''__________________________________________________________________可樂旅遊'''
@app.route("/travel")
def travel():
    
    p = request.args.get('p', '')
    page = int(request.args.get('page',1))
    sql = "select count(*) as c from travel"                                   
    db.cursor.execute(sql)
    datacount = db.cursor.fetchone()                                          
    count = int(datacount[0])
    if  page == 1 and p == '':
        if len(p) == 0:
            sql = "select title,link_url,photo_url,platform from travel order by id asc limit 20"
        else:
            sql = "select title,link_url,photo_url,platform from travel where platform = '{}' order by id asc limit 20".format(p)
    else: 
        startp = page-1
        if len(p) == 0:
            sql = "select count(*) as c from travel "
            db.cursor.execute(sql)           
            datacount = db.cursor.fetchone()                                   
            count = int(datacount[0])             
            print('page:',count)           
            sql = "select title,link_url,photo_url,platform from travel order by id asc limit {},{}".format(startp*20,20)           
        else:
            sql = "select count(*) as c from travel where platform = '{}'".format(p)             
            db.cursor.execute(sql)              
            datacount = db.cursor.fetchone()                                   
            count = int(datacount[0]) 
            print(count)
            sql = "select title,link_url,photo_url,platform from travel where platform = '{}' order by id asc limit {},{}".format(p,startp*20,20)
    db.cursor.execute(sql)
    travels = db.cursor.fetchall()
    count = int(datacount[0])
    pagination = Pagination (page = page, total = count , per_page = 20)
                    # 使用函式    頁數           總比數          以20筆為分頁
    return render_template("travel.html", **locals())


'''_________________________________________________________渲染 聯絡我們html'''
@app.route('/contact')
def message():
    
    return render_template('message.html')

'''_______________________________________________________接收資訊新增至資料庫'''
@app.route("/addcontact",methods = ['POST'])          
def contact():
    
    if request.method == "POST" :                     
        username = request.form.get('name')
        email    = request.form.get('email')
        title    = request.form.get('title')
        content  = request.form.get('content')
        today    = datetime.today()
        c_date   = datetime.strftime(today,'%Y-%m-%d') 
        sql = "insert into contact(subject,name,email,content,create_date) values('{}','{}','{}','{}','{}')".format(title,username,email,content,c_date)
        db.cursor.execute(sql)          
        db.conn.commit()              
    return redirect(url_for('message'))

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/home")
    app.run(debug=False)
