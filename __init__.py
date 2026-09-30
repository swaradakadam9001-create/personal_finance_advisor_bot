from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(Path(app.instance_path) / "finance.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        from .models import Expense
        if Expense.query.count() == 0:
            seed_demo_data()

    return app

def seed_demo_data():
    from .models import Expense, Income
    from datetime import date, timedelta
    income = Income(source="Salary", amount=50000, date=date.today().replace(day=1))
    db.session.add(income)
    sample = [
        ("Rent", 12000), ("Food", 4500), ("Transport", 2200),
        ("Entertainment", 1800), ("Shopping", 2500), ("Bills", 3000)
    ]
    for i, (category, amount) in enumerate(sample):
        db.session.add(Expense(category=category, amount=amount,
                                description="Demo expense", date=date.today()-timedelta(days=i*3)))
    db.session.commit()
