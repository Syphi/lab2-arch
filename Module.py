import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['DEFAULT']['FileType'] == 'pickle' :
    from Pickle_mod import PickleMethod
    Methods = PickleMethod()
elif config['DEFAULT']['FileType'] == 'json' :
    from Json_mod import JsonMethod
    Methods = JsonMethod()
elif config['DEFAULT']['FileType'] == 'yaml' :
    from Yaml_mod import YamlMethod
    Methods = YamlMethod()


class create_method:

    @staticmethod
    @Methods.serial_method
    def create(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        create operation in our list
        :return:

        """
        op_id = 0
        operation = {'sign': sign,
                     'summary': summary,
                     'dd': dd, 'mm': mm, 'yy': yy,
                     'comment': comment}
        Operation_History.append(operation)


class edit_method:

    @staticmethod
    @Methods.serial_method
    def edit_sign(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit sign in need operation
        :return:

        """
        summary = 0
        dd = 0
        mm = 0
        yy = 0
        comment = ''
        Operation_History[op_id-1]['sign'] = sign

    @staticmethod
    @Methods.serial_method
    def edit_summary(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit summary in need operation
        :return:

        """
        sign = 0
        dd = 0
        mm = 0
        yy = 0
        comment = ''
        Operation_History[op_id-1]['summary'] = summary

    @staticmethod
    @Methods.serial_method
    def edit_dd(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit day in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        comment = ''
        Operation_History[op_id-1]['dd'] = dd

    @staticmethod
    @Methods.serial_method
    def edit_mm(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit month in need operation
        :return:

        """
        summary = 0
        sign = 0
        dd = 0
        yy = 0
        comment = ''
        Operation_History[op_id-1]['mm'] = mm

    @staticmethod
    @Methods.serial_method
    def edit_yy(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit year in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        dd = 0
        comment = ''
        Operation_History[op_id-1]['yy'] = yy

    @staticmethod
    @Methods.serial_method
    def edit_comment(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit comment in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        dd = 0
        Operation_History[op_id-1]['comment'] = comment


class delete:

    @staticmethod
    @Methods.serial_method
    def delete_operation(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        delete need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        dd = 0
        comment = ''
        Operation_History.pop(op_id-1)

class Geter:

    @staticmethod
    @Methods.serial_method
    def get_dict(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        dd = 0
        comment = ''
        op_id = 0
        return Operation_History
