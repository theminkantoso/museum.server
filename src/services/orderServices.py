class OrderService():
    @staticmethod
    def convert_to_dict(arr):
        print({'order_date': str(arr[0][0]),
                arr[0][2]: arr[0][1],
                arr[1][2]: arr[1][1],
                arr[2][2]: arr[2][1]})
        return {'order_date': str(arr[0][0]),
                arr[0][2]: arr[0][1],
                arr[1][2]: arr[1][1],
                arr[2][2]: arr[2][1]}
