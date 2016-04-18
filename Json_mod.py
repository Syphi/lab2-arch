import json


class JsonMethod:

    @staticmethod
    def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment):
            with open('ser.json', 'r') as f:
                Operation_History = json.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment)
            with open('ser.json', 'w') as f:
                json.dump(Operation_History, f)
            return crud
        return wrapper