from Module import *
import configparser
import sys
import argparse

class database():

    @staticmethod
    def edit_all(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        """

        edit our operation
        :return:

        """
        edit_method().edit_sign(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
        edit_method().edit_summary(op_id, sign, summary, dd, mm, yy, comment , Operation_History)
        edit_method().edit_dd(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
        edit_method().edit_mm(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
        edit_method().edit_yy(op_id, sign, summary, dd, mm, yy, comment, Operation_History)
        edit_method().edit_comment(op_id, sign, summary, dd, mm, yy, comment, Operation_History)

    @staticmethod
    def create(op_id, sign1, summary2, dd3, mm4, yy5, comment6, Operation_History):
        create_method().create(op_id,sign1, summary2, dd3, mm4, yy5, comment6, Operation_History)

    @staticmethod
    def delete(op_id, sign, summary, dd, mm, yy, comment, Operation_History):
        delete().delete_operation(op_id, sign, summary, dd, mm, yy, comment, Operation_History)

class ViewMethod:

    def __init__(self):
        self.geter = Geter()
        self.Operation_History = self.geter.get_dict(0, 0, 0, 0, 0, 0, 0, {})

    def balance_plus(self):
        """
        show our income
        :return: our income of all our operation

        """
        plus = 0
        i = 0
        for i in range(len(self.Operation_History)):
            if self.Operation_History[i]['sign'] == '+':
                plus += int(self.Operation_History[i]['summary'])
        return plus

    def balance_minus(self):
        """

        show our expenses
        :return: all our expenses

        """
        minus = 0
        for i in range(len(self.Operation_History)):
            if self.Operation_History[i]['sign'] == '-':
                minus += int(self.Operation_History[i]['summary'])
        return minus

    def balance_difference(self):
        """

        :return: different between our income and expenses

        """
        return self.balance_plus() - self.balance_minus()


    def show_method(self):
        """

        show to us all our operation
        :return:

        """
        i = 0
        while i < len(self.Operation_History):
            print(" Id you'r operation :"+str((i+1)))
            print(" Sign you'r operation :"+self.Operation_History[i]['sign'])
            Sum = " Summary you'r operation :"
            print(Sum+str(self.Operation_History[i]['summary']))
            print(" Day you'r operation :"+str(self.Operation_History[i]['dd']))
            print(" Mounth you'r operation :"+str(self.Operation_History[i]['mm']))
            print(" Year you'r operation :"+str(self.Operation_History[i]['yy']))
            Com = " Comment to you'r operation :"
            print(Com+self.Operation_History[i]['comment']+"\n")
            i += 1

    @staticmethod
    def show_list():
        """

        show to us main menu
        :return:
        """
        shows = ' 1: Show'
        cr_pp = '\n 2:Create Operation'
        d_op = '\n 3:Delete Operation'
        e_op = '\n 4:Edit Operation'
        print(shows, cr_pp, d_op, e_op)
        p_b = " 5:Positive Balance"
        n_b = "\n 6:Negative Balance"
        s_b = "\n 7:Summary Balance"
        e = "\n 8:Exit"
        print(p_b + n_b + s_b + e)

    def menu_create(self):
            """

            create operation menu
            :return:

            """
            sign1 = input("\n Enter you'r sign :")
            summary2 = input(" Enter summary of you'r operation :")
            dd3 = input(" Enter day :")
            mm4 = input(" Enter month :")
            yy5 = input(" Enter year :")
            comment6 = input(" Enter comment of you'r operation :")
            op_id = 0
            Operation_History = {}
            database().create(op_id,sign1, summary2, dd3, mm4, yy5, comment6, Operation_History)
            self.show_method()

    def menu_delete(self):
            """

            delete operation menu
            :return:

            """
            self.show_method()
            op_id = int(input("\n Enter number of operation what you want to delete :"))
            database().delete(op_id, 0, 0, 0, 0, 0, 0, {})
            self.show_method()

    def menu_edit(self):
            """

            edit operation menu
            :return:

            """
            self.show_method()
            op_ch = " Enter number of operation what you want to change:"
            op_id = int(input(op_ch))
            sign1 = input(" Enter you'r new sign :")
            summary2 = int(input(" Enter summary of you'r  new operation :"))
            dd3 = int(input(" Enter new day :"))
            mm4 = int(input(" Enter new month :"))
            yy5 = int(input(" Enter new year :"))
            comment6 = input(" Enter new comment of you'r operation :")
            database().edit_all(op_id, sign1, summary2, dd3, mm4, yy5, comment6, {})
            self.show_method()

    def menu_balance_plus(self):
            """

            income of all operation menu
            :return:

            """
            op_balance = self.balance_plus()
            print("You'r income =" + str(op_balance))

    def menu_balance_minus(self):
            """

            expenses of all operation menu
            :return:

            """
            op_balance = self.balance_minus()
            print("You'r expenses =" + str(op_balance))

    def menu_balance_all(self):
            """

            balance of all operation menu
            :return:

            """
            op_balance = self.balance_difference()
            print("You'r balance = " + str(op_balance))

    @staticmethod
    def message(mess):
        """
            show message for user
            :return:
        """
        print(mess)


class Console(ViewMethod):

    def __init__(self):
        self.geter = Geter()
        self.Operation_History = self.geter.get_dict(0, 0, 0, 0, 0, 0, 0, {})
        self.database = database()
        parser = self.create_parser()
        namespace = parser.parse_args(sys.argv[1:])
        self.parser_analyze(namespace, sys.argv[1:])

    def create_parser(self):
        """
        Creating parser
        :return:
        """
        parser = argparse.ArgumentParser(
            prog='lab3',
            description='''Lab 3 incoming calculate''',
            epilog='''(c) Ralko D., Shmiryov A. 2016 KPI'''
        )

        parser.add_argument('-a', '--add', nargs='+',
                            help='Adding new operation in format "Sign" "Summary" "Day" "Mounth" "Year" "Comment"')
        parser.add_argument('-d', '--delete', help='Deleting operation in format "Id"')
        parser.add_argument('-s', '--show', action='store_const', const=True, default=False,
                            help='Showing all operations')
        parser.add_argument('-u', '--update', nargs='+', help='Updating operation')
        parser.add_argument('-p', '--positive',action='store_const', const=True, default=False,
                            help='Showing positive balance')
        parser.add_argument('-n', '--negative',action='store_const', const=True, default=False,
                            help='Showing negative balance')
        parser.add_argument('-r', '--result',action='store_const', const=True, default=False,
                            help='Show you summary balance')

        return parser

    def parser_analyze(self, namespace, params):
        """
        Analyzing keys
        :param namespace:
        :param params:
        :return:
        """
        if '-s' in params or '--show' in params:
            self.show_method()
        if '-a' in params or '--add' in params:
            self.new_operation(namespace)
        if '-d' in params or '--delete' in params:
            self.del_operation(namespace)
        if '-u' in params or '--update' in params:
            self.upd_opetarion(namespace)
        if '-p' in params or '--positive' in params:
            self.menu_balance_plus()
        if '-n' in params or '--negative' in params:
            self.menu_balance_minus()
        if '-r' in params or '--result' in params:
            self.menu_balance_all()

    def new_operation(self, namespace):
        """
            Adding new product to file
            :param namespace:
            :return:
            """
        if len(namespace.add) < 6:
            self.message('Wrong number of arguments')
            return
        self.database.create(0,namespace.add[0], namespace.add[1], namespace.add[2], namespace.add[3], namespace.add[4],
                             namespace.add[5], {})

    def del_operation(self, namespace):
        """
        Deleting product from file
        :param namespace:
        :return:
        """
        id = int(namespace.delete)
        from DataBase import Operation_History
        self.database.delete(id, 0, 0, 0, 0, 0, 0, Operation_History)
        self.message('Deleted.')


    def upd_opetarion(self, namespace):
        """
        Updating product in file
        :param namespace:
        :return:
        """
        if len(namespace.update) < 7:
            self.message('Wrong number of arguments')
            return
        id = int(namespace.update[0])
        sign = namespace.update[1]
        summary = namespace.update[2]
        day = namespace.update[3]
        mounth = namespace.update[4]
        year = namespace.update[5]
        comment = namespace.update[6]
        from DataBase import Operation_History
        self.database.edit_all(id, sign, summary, day, mounth, year, comment, Operation_History)
        self.message('Updated.')
