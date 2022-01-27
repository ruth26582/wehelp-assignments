from flask import Flask, Blueprint, render_template, redirect, url_for, request

error_blueprints = Blueprint('error_blueprints', __name__, static_folder="static",
                             template_folder="templates\error")


@error_blueprints.route("/error")
def error():
    errMsg = request.args.get('message')
    return render_template("error.html", message=errMsg)
