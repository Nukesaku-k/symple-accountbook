from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import extract

db = SQLAlchemy()


class TItems(db.Model):
    __tablename__ = 't_items'

    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_name = db.Column(db.Text)
    item_cost = db.Column(db.Integer)
    category_id = db.Column(db.Text)
    paid_on = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


def init_db(app):
    db.init_app(app)
    db.create_all()


def get_all():
    return TItems.query.filter(TItems.paid_on >= date.today().replace(day=1))


def insert(item_name, item_cost, category_id, paid_on):
    model = TItems(item_name=item_name, item_cost=item_cost, category_id=category_id, paid_on=paid_on)
    db.session.add(model)
    db.session.commit()


def delete(id):
    trget_item = TItems.query.filter_by(item_id=id).first()
    db.session.delete(trget_item)
    db.session.commit()
