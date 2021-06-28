import unittest
import pathlib
import openpyxl


class make_new_workbook_nameTest(unittest.TestCase):
    def test_no_extension(self):
        from mkevixl2.excel_handler import make_new_workbook_name

        self.assertEqual(make_new_workbook_name("test"), "test.xlsx")

    def test_extension(self):
        from mkevixl2.excel_handler import make_new_workbook_name

        self.assertEqual(make_new_workbook_name("test.xlsx"), "test.xlsx")

    def test_wrong_extension(self):
        from mkevixl2.excel_handler import make_new_workbook_name

        self.assertEqual(make_new_workbook_name("test.txt"), "test.xlsx")


class AddWorkSheetTest(unittest.TestCase):
    def test_makefile_mode1(self):
        filename = "AddWorkSheetTest_1.xlsx"
        file = pathlib.Path(filename)
        sheetnames = ("add1", "add2", "add3")

        from mkevixl2.excel_handler import make_file

        make_file(filename, sheetnames)
        self.assertTrue(file.exists())
