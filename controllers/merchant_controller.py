from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.merchant_repository as merchant_repo
from models.merchant import Merchant


merchant_blueprint = Blueprint("merchants", __name__)


@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repo.select_all()
    return render_template("merchants/new.html", merchants=merchants)


@merchant_blueprint.route("/merchants/new/merchant", methods=["POST"])
def new_merchant():
    new_merchant = Merchant(request.form["merchant_name"])
    merchant_repo.save(new_merchant)
    return redirect("/merchants")
