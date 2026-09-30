from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from datetime import datetime
from . import db
from .models import Income, Expense, Goal
from .finance import analyze

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    incomes = Income.query.order_by(Income.date.desc()).all()
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    goals = Goal.query.order_by(Goal.id.desc()).all()
    report = analyze(incomes, expenses)
    return render_template("dashboard.html", report=report, incomes=incomes[:6],
                           expenses=expenses[:10], goals=goals)

@main.route("/add-income", methods=["POST"])
def add_income():
    try:
        amount = float(request.form["amount"])
        source = request.form["source"].strip() or "Income"
        dt = datetime.strptime(request.form.get("date") or datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d").date()
        if amount <= 0: raise ValueError
        db.session.add(Income(source=source, amount=amount, date=dt))
        db.session.commit()
        flash("Income added successfully.", "success")
    except (ValueError, KeyError):
        flash("Please enter valid income details.", "error")
    return redirect(url_for("main.dashboard"))

@main.route("/add-expense", methods=["POST"])
def add_expense():
    try:
        amount = float(request.form["amount"])
        category = request.form["category"].strip()
        desc = request.form.get("description", "").strip()
        dt = datetime.strptime(request.form.get("date") or datetime.today().strftime("%Y-%m-%d"), "%Y-%m-%d").date()
        if not category or amount <= 0: raise ValueError
        db.session.add(Expense(category=category, amount=amount, description=desc, date=dt))
        db.session.commit()
        flash("Expense added successfully.", "success")
    except (ValueError, KeyError):
        flash("Please enter valid expense details.", "error")
    return redirect(url_for("main.dashboard"))

@main.route("/add-goal", methods=["POST"])
def add_goal():
    try:
        name = request.form["name"].strip()
        target = float(request.form["target"])
        deadline = request.form.get("deadline")
        deadline = datetime.strptime(deadline, "%Y-%m-%d").date() if deadline else None
        if not name or target <= 0: raise ValueError
        db.session.add(Goal(name=name, target=target, saved=0, deadline=deadline))
        db.session.commit()
        flash("Savings goal created.", "success")
    except (ValueError, KeyError):
        flash("Please enter valid goal details.", "error")
    return redirect(url_for("main.dashboard"))

@main.route("/api/summary")
def api_summary():
    incomes = Income.query.all()
    expenses = Expense.query.all()
    return jsonify(analyze(incomes, expenses))
