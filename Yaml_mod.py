import yaml


class YamlMethod:



     def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment, data):
            with open('ser.yaml', 'r') as f:
                Operation_History = yaml.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
            with open('ser.yaml', 'w') as f:
                yaml.dump(Operation_History, f)
            return crud
        return wrapper
