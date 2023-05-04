from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

#起始點(登入)
@app.route("/")
def log_in():   
    return render_template("log_in.html") 

#可以選要開團or購物
@app.route("/home")
def home():
    return render_template("home.html")

#修改會員資料頁面
@app.route("/member_profile")
def member_profile():
    return render_template("member_profile.html")

#編輯的畫面
@app.route("/edit", method=['POST', 'GET'])
def edit(): 
    if request.method == 'POST' :
        try:
            # some n variable 
            with sqlite3.connect('DB.db') as con :
                cur = con.cursor()
                cur.execute()
                #update n variable

                msg = "record successful " 
        except:
            #sth wrong 
            con.rollback()
            mas = "error!!" #where error
        finally:
            #db 連接結束
            return render_template("result.html" , msg=msg)
        
#要把開團的商品加入倉庫
@app.route("/grouping", methods=['POST','GET'])
def grouping():
    if request.method == 'POST' :
        try:
            #新增n個variable
            #連接資料庫    
            with sqlite3.connect('DB.db') as con:
                cur = con.cursor()
                cur.execute()
                #do sth 
                msg = "record successful"
        except:
            con.rollback()
            msg = "error in insert "
        finally:
            con.close()
            return render_template('result.html' , msg = msg )
        

