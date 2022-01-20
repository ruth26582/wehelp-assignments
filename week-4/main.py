from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)  # __name__代表目前執行的模組
app.secret_key = "#084$*2^n-_q+!qsf1d=zu967$dqs_xd0typdy!0&4+b(db7!f^f"


@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/signin", methods=["POST"])
def signin():
    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']

        # 帳號、密碼都輸入 test
        if account == 'test' and password == 'test':
            # 紀錄已登入的帳號
            session['account'] = account
            return redirect(url_for("member"))

        # 帳號、密碼都為空 or 帳號、密碼任一為空
        elif (account == '' and password == '') or (account == '' and password != '') or (account != '' and password == ''):
            return redirect(url_for("error", message='請輸入帳號、密碼'))

        # 帳號、密碼都不是輸入 test
        else:
            return redirect(url_for("error", message='帳號、或密碼輸入錯誤'))
    else:
        if "account" in session:
            return redirect(url_for("member"))
        return render_template("login.html")


@app.route("/member/")
def member():
    if "account" in session:
        account = session["account"]
        return render_template("member.html", accountVal=account)
    else:
        return redirect(url_for("login"))


@app.route("/error/")
def error():
    errMsg = request.args.get('message')
    return render_template("error.html", message=errMsg)


@ app.route("/signout")
def signout():
    session.pop("account", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)  # 立刻啟動伺服器
