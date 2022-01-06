from flask_restful import Resource, reqparse
from src.services.statisticsService import StatisticsService


class StatisticsOrder(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_date')
        data = parser.parse_args()
        order_date = data['order_date']
        if order_date is None or order_date == '':
            return StatisticsService.stats_order_all(), 200
        else:
            str_date = order_date[0:10]
            return StatisticsService.stats_order_by_date(str_date), 200


class StatisticsTicket(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_date')
        data = parser.parse_args()
        order_date = data['order_date']
        if order_date is None or order_date == '':
            return StatisticsService.stats_ticket_all(), 200
        else:
            str_date = order_date[0:10]
            return StatisticsService.stats_ticket_by_date(str_date), 200
