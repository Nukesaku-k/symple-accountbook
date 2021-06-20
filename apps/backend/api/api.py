# -*- coding: utf-8 -*-
import calendar
import datetime
# import inspect
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, request
from api.models import t_items

api_bp = Blueprint('api', __name__, url_prefix='/api')
post_parser = reqparse.RequestParser()


class List(Resource):
    def get(self):
        return [{
            'id': x.item_id, 'item_name': x.item_name,
            'item_cost': x.item_cost, 'category_id': x.category_id,
            'paid_on': x.paid_on.strftime('%Y-%m-%d')} for x in t_items.get_all()]

    def post(self):
        t_items.insert(
            request.form['item_name'],
            request.form['item_cost'],
            request.form['category_id'],
            datetime.datetime.strptime(request.form['paid_on'], '%Y-%m-%d'))

    def delete(self):
        # for x in inspect.getmembers(request, inspect.ismethod):
        #     print(x[0])
        t_items.delete(request.form['item_id'])


class Chart(Resource):
    def get(self):
        return wraped_chart_data()


def wraped_chart_data():
    # Initialaize variables.
    wraped_data = {}
    labels = date_labels()
    data = [0]*len(labels)
    # today = datetime.datetime.today()

    for i, label in enumerate(labels):
        for item in t_items.get_all():
            if label == item.paid_on.strftime('%m/%d'):
                data[i] += item.item_cost

    wraped_data['labels'] = labels
    wraped_data['datasets'] = [{
        'label': '2020-07',
        'data': data,
        # 'backgroundColor': 'rgba(248, 121, 121, 0.1)',
        'borderColor': 'teal'}]

    # print(wraped_data)
    return wraped_data


def date_labels():
    today = datetime.datetime.today()
    return ["{0:%m/%d}".format(datetime.datetime(today.year, today.month, (ix+1)))
            for ix in range(calendar.monthrange(today.year, today.month)[1])]

# from the first day of this year to today.
# todo:TBD


api = Api(api_bp)
api.add_resource(List, '/list')
api.add_resource(Chart, '/chart')
