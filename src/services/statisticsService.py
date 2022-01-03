from src.models.orderDb import OrderDb


class StatisticsService():

    @staticmethod
    def stats_order_all():
        query = OrderDb.stats_order_all()
        return StatisticsService.convert_dict(query)

    @staticmethod
    def stats_order_by_date(date):
        query = OrderDb.stats_order_by_date(date)
        return StatisticsService.convert_dict(query)

    @staticmethod
    def convert_dict(arr):
        dict_out = {}
        for i in range(len(arr)):
            dict_out[(arr[i][1])] = int(arr[i][0])
        return dict_out

    @staticmethod
    def stats_ticket_all():
        query = OrderDb.stats_ticket_all()
        query_total = OrderDb.total_price_ticket_all()
        res = StatisticsService.convert_dict(query)
        res['total'] = int(query_total[0][0])
        return res

    @staticmethod
    def stats_ticket_by_date(date):
        query = OrderDb.stats_ticket_by_date(date)
        query_total = OrderDb.total_price_ticket_date(date)
        res = StatisticsService.convert_dict(query)
        res['total'] = int(query_total[0][0])
        return res

