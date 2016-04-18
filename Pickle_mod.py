import pickle


class PickleMethod:

     @staticmethod
     def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment, data):
            with open('ser.pickle', 'rb') as f:
                Operation_History = pickle.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
            with open('ser.pickle', 'wb') as f:
                pickle.dump(Operation_History, f)
            return crud
        return wrapper

