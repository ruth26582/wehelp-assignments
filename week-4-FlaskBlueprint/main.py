from flask import Flask, render_template, request, redirect, session, url_for
from member.member import member_blueprints
from error.error import error_blueprints

app = Flask(__name__)
app.secret_key = "#084$*2^n-_q+!qsf1d=zu967$dqs_xd0typdy!0&4+b(db7!f^nk"
app.register_blueprint(member_blueprints)
app.register_blueprint(error_blueprints)


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
            return redirect(url_for("member_blueprints.member"))

        # 帳號、密碼都為空 or 帳號、密碼任一為空
        elif (account == '' and password == '') or (account == '' and password != '') or (account != '' and password == ''):
            return redirect(url_for("error_blueprints.error", message='請輸入帳號、密碼'))

        # 帳號、密碼都不是輸入 test
        else:
            return redirect(url_for("error_blueprints.error", message='帳號、或密碼輸入錯誤'))
    else:
        if "account" in session:
            return redirect(url_for("member_blueprints.member"))
        return render_template("login.html")


@app.route("/signout")
def signout():
    session.pop("account", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
