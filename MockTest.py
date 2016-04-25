from unittest import mock
from View import *
from Contreller import *
from Module import *
import argparse

#op_id, sign, summary, dd, mm, yy, comment, Operation_History
test = create_method()

test.create = mock.MagicMock()
test.create.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test = edit_method()

test.edit_sign = mock.MagicMock()
test.edit_sign.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.edit_summary = mock.MagicMock()
test.edit_summary.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.edit_dd = mock.MagicMock()
test.edit_dd.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.edit_mm = mock.MagicMock()
test.edit_mm.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.edit_yy = mock.MagicMock()
test.edit_yy.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.edit_comment = mock.MagicMock()
test.edit_comment.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test = delete()

test.delete_operation = mock.MagicMock()
test.delete_operation.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test = Geter()

test.get_dict = mock.MagicMock()
test.get_dict.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test = database()

test.edit_all = mock.MagicMock()
test.edit_all.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.create = mock.MagicMock()
test.create.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test.delete = mock.MagicMock()
test.delete.assert_call_once_with(0, 0, 0, 0, 0, 0, 0, {})

test = ViewMethod()

test.balance_plus = mock.MagicMock()
test.balance_plus.assert_call_once_with()
result = ViewMethod().balance_plus()
assert result == 235
print(result)

test.balance_minus = mock.MagicMock()
test.balance_minus.assert_call_once_with()
result = ViewMethod().balance_minus()
assert result == 1500
print(result)

test.balance_difference = mock.MagicMock()
test.balance_difference.assert_call_once_with()
result = ViewMethod().balance_difference()
assert result == -1265
print(result)

test.show_method = mock.MagicMock()
test.show_method()

test.show_list = mock.MagicMock()
test.show_list()

test.menu_create = mock.MagicMock()
test.menu_create()

test.menu_delete = mock.MagicMock()
test.menu_delete()

test.menu_edit = mock.MagicMock()
test.menu_edit()

test.menu_balance_plus = mock.MagicMock()
test.menu_balance_plus()

test.menu_balance_minus = mock.MagicMock()
test.menu_balance_minus()

test.menu_balance_all = mock.MagicMock()
test.menu_balance_all()

test.message = mock.MagicMock()
test.message.assert_call_once_with("Hello")

test = Console()

namespace = argparse.Namespace(add=0, delete=0, show =0, update=0, positive=0, negative=0, result=0)
#test.create_parser

test.parser_analyze = mock.MagicMock()
test.parser_analyze(namespace, {})

test = main()

test.menu = mock.MagicMock()
test.menu()
