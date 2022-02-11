from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)  # __name__代表目前執行的模組
app.secret_key = "#084$*2^n-_q+!qsf1d=zu967$dqs_xd0typdy!0&4+b(db7!f^f"
app.config['TEMPLATES_AUTO_RELOAD'] = True


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="website"
)


@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/signup", methods=["POST"])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        sql = "select count(1) from member where username = %(username)s;"
        cursor.execute(sql, {'username': username})
        result = cursor.fetchone()
        if result[0] == 1:
            return redirect(url_for("error", message='帳號已經被註冊'))
        else:
            if name == '' or username == '' or password == '':
                return redirect(url_for("error", message='請輸入姓名、帳號、密碼'))
            else:
                cursor.execute(
                    "INSERT INTO member VALUES (NULL,%s,%s,%s,DEFAULT,DEFAULT);", (name, username, password))
                cursor.close()
                db.commit()
                return redirect(url_for("login"))


@app.route("/signin", methods=["POST"])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        sql = "select count(1) from member where username = %(username)s and password = %(password)s;"
        cursor.execute(sql, {'username': username, 'password': password})
        result = cursor.fetchone()
        if result[0] == 1:
            session['username'] = username
            cursor.close()
            return redirect(url_for("member"))
        else:
            if (username == '' and password == '') or (username == '' and password != '') or (username != '' and password == ''):
                return redirect(url_for("error", message='請輸入帳號、密碼'))
            else:
                return redirect(url_for("error", message='帳號、或密碼輸入錯誤'))
    else:
        if "username" in session:
            return redirect(url_for("member"))
        return render_template("login.html")


@app.route("/member/")
def member():
    if "username" in session:
        username = session["username"]
        cursor = db.cursor()
        sql = "select name from member where username = %(username)s;"
        cursor.execute(sql, {'username': username})
        result = cursor.fetchone()
        name = result[0]
        return render_template("member.html", accountVal=username, name=name)
    else:
        return redirect(url_for("login"))


@app.route("/error/")
def error():
    errMsg = request.args.get('message')
    return render_template("error.html", message=errMsg)


@ app.route("/signout")
def signout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)  # 立刻啟動伺服器
