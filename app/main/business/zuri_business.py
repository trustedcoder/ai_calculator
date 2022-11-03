
class AppBusiness:
    @staticmethod
    def cal_arithmetic(data):
        if data['operation_type'] == 'addition':
            result = data['x'] + data['y']
        elif data['operation_type'] == 'subtraction':
            result = data['x'] - data['y']
        else:
            result = data['x'] * data['y']
        response = {
            'slackUsername': 'trustedcoder',
            'result': result,
            'operation_type': data['operation_type']
        }
        return response, 200
