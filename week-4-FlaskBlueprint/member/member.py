from flask import Flask, Blueprint, render_template, redirect, url_for, session

member_blueprints = Blueprint('member_blueprints', __name__, static_folder="static",
                              template_folder="templates\member")


@member_blueprints.route("/member/")
def member():
    if "account" in session:
        account = session["account"]
        return render_template("member.html", accountVal=account)
    else:
        return redirect(url_for("login"))
