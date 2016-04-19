from Contreller import *

class main:

    def menu(self):
        """

        interface menu
        :return:

        """
        ViewMethod().show_list()
        op = int(input("\n Enter menu number :"))
        if op == 1:
            ViewMethod().show_method()
            self.menu()
        elif op == 2:
            ViewMethod().menu_create()
            self.menu()
        elif op == 3:
            ViewMethod().menu_delete()
            self.menu()
        elif op == 4:
            ViewMethod().menu_edit()
            self.menu()
        elif op == 5:
            ViewMethod().menu_balance_plus()
            self.menu()
        elif op == 6:
            ViewMethod().menu_balance_minus()
            self.menu()
        elif op == 7:
            ViewMethod().menu_balance_all()
            self.menu()
        elif op == 8:
            exit()
        else:
            print("\n Not right number!!")
            self.menu()

p=main()
p.menu()
