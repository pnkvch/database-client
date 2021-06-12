from mainInterfaceTest import MainInterface
from tkinter import *
import unittest


class TestProject(unittest.TestCase):
    root = Tk()
    interface = MainInterface(root)

    # Before running tests remove all the .get() methods and comment out self.createMainInterface() method from tested function

    def test_00_AddTable(self):
        self.interface.entries = {
            "ID": "Integer",
            "name": "Text",
            "surname": "Text",
            "height": "Real Number"
        }

        resultDataTypes = {
            "ID": int,
            "name": str,
            "surname": str,
            "height": float,
            "tableID": 0
        }
        resultDatabase = {
            "ID": [],
            "name": [],
            "surname": [],
            "height": [],
            "tableName": "test1",
            "tableID": 0
        }

        self.interface.handleAddTable(Toplevel(self.root), "test1")
        self.assertDictEqual(resultDataTypes, self.interface.dataTypes[0])
        self.assertDictEqual(resultDatabase, self.interface.databases[0])

    def test_01_AddTableRow(self):
        self.interface.entries = {
            "ID": 1,
            "name": "Roch",
            "surname": "Przylbipiet",
            "height": 1.50
        }

        result = {
            "ID": [1],
            "name": ["Roch"],
            "surname": ["Przylbipiet"],
            "height": [1.50],
            "tableName": "test1",
            "tableID": 0
        }

        self.interface.handleAddRecord(
            Toplevel(self.root), self.interface.databases[0])
        self.assertDictEqual(result, self.interface.databases[0])

    def test_02_AddTableRow(self):
        self.interface.entries = {
            "ID": 2,
            "name": "Ziemniaczyslaw",
            "surname": "Bulwiasty",
            "height": 1.91
        }

        result = {
            "ID": [1, 2],
            "name": ["Roch", "Ziemniaczyslaw"],
            "surname": ["Przylbipiet", "Bulwiasty"],
            "height": [1.50, 1.91],
            "tableName": "test1",
            "tableID": 0
        }

        self.interface.handleAddRecord(
            Toplevel(self.root), self.interface.databases[0])
        self.assertDictEqual(result, self.interface.databases[0])

    def test_03_AddIncorrectTableRow(self):
        self.interface.entries = {
            "ID": "cztery",
            "name": "bla",
            "surname": "bla",
            "height": -90
        }

        inputWindow = Toplevel(self.root)
        self.interface.handleAddRecord(
            inputWindow, self.interface.databases[0])
        result = inputWindow.children["!label5"].cget("text")
        expected = "cztery is not the correct type"
        self.assertEqual(result, expected)

    def test_04_AddIncorrectTableRow(self):
        self.interface.entries = {
            "ID": 3.14,
            "name": "pi",
            "surname": "ludolfina",
            "height": 314e-2
        }

        inputWindow = Toplevel(self.root)
        self.interface.handleAddRecord(
            inputWindow, self.interface.databases[0])

        result = inputWindow.children["!label5"].cget("text")
        expected = "3.14 is not the correct type"
        self.assertEqual(result, expected)

    def test_05_AttemptToDeleteTableRow(self):
        entry = 0

        inputWindow = Toplevel(self.root)
        self.interface.verifyDeleteRow(
            inputWindow, entry, self.interface.databases[0])

        inputWindow.children["!toplevel"].children['!button2'].invoke()

        result = {
            "ID": [1, 2],
            "name": ["Roch", "Ziemniaczyslaw"],
            "surname": ["Przylbipiet", "Bulwiasty"],
            "height": [1.50, 1.91],
            "tableName": "test1",
            "tableID": 0
        }

        self.assertDictEqual(result, self.interface.databases[0])

    def test_06_DeleteTableRow(self):
        entry = 0

        inputWindow = Toplevel(self.root)
        self.interface.verifyDeleteRow(
            inputWindow, entry, self.interface.databases[0])

        inputWindow.children["!toplevel"].children['!button'].invoke()

        result = {
            "ID": [2],
            "name": ["Ziemniaczyslaw"],
            "surname": ["Bulwiasty"],
            "height": [1.91],
            "tableName": "test1",
            "tableID": 0
        }

        self.assertDictEqual(result, self.interface.databases[0])

    def test_07_AddSecondTable(self):
        self.interface.entries = {
            "reserved": "Text",
            "color": "Integer",
        }

        resultDataTypes = {
            "reserved": str,
            "color": int,
            "tableID": 1
        }

        resultDatabase = {
            "reserved": [],
            "color": [],
            "tableName": "test2",
            "tableID": 1
        }

        self.interface.handleAddTable(Toplevel(self.root), "test2")
        self.assertDictEqual(resultDataTypes, self.interface.dataTypes[1])
        self.assertDictEqual(resultDatabase, self.interface.databases[1])

    def test_08_AddTableRow(self):
        self.interface.entries = {
            "reserved": "",
            "color": 1337,
        }

        result = {
            "reserved": [""],
            "color": [1337],
            "tableName": "test2",
            "tableID": 1
        }

        self.interface.handleAddRecord(
            Toplevel(self.root), self.interface.databases[1])
        self.assertDictEqual(result, self.interface.databases[1])

    def test_09_AddIncorrectTableRow(self):
        self.interface.entries = {
            "reserved": "bla",
            "color": "1939b",
        }

        inputWindow = Toplevel(self.root)
        self.interface.handleAddRecord(
            inputWindow, self.interface.databases[1])

        result = inputWindow.children["!label3"].cget("text")
        expected = "1939b is not the correct type"
        self.assertEqual(result, expected)

    def test_10_DeleteTable(self):
        entry = 0

        inputWindow = Toplevel(self.root)
        self.interface.verifyDeleteTable(
            inputWindow, entry)

        inputWindow.children["!toplevel"].children['!button2'].invoke()

        result = len(self.interface.databases)
        expected = 2

        self.assertEqual(result, expected)

    def test_11_DeleteTable(self):
        entry = 0

        inputWindow = Toplevel(self.root)
        self.interface.verifyDeleteTable(
            inputWindow, entry)

        inputWindow.children["!toplevel"].children['!button'].invoke()

        result = len(self.interface.databases)
        expected = 1

        self.assertEqual(result, expected)

    def test_12_AddTableWithIncorrectName(self):
        self.interface.entries = {
            "ID": "Integer",
            "login": "text"
        }

        self.interface.handleAddTable(Toplevel(self.root), "")
        result = len(self.interface.databases)
        expected = 1

        self.assertEqual(result, expected)

    def test_13_AddTableWithNoName(self):
        self.interface.entries = {
            "ID": "Integer",
            "login": "text"
        }

        self.interface.handleAddTable(Toplevel(self.root))
        result = len(self.interface.databases)
        expected = 1

        self.assertEqual(result, expected)

    def test_14_AddTableWithNoColumnName(self):
        self.interface.entries = {
            "": "Integer"
        }

        self.interface.handleAddTable(Toplevel(self.root), "test")
        result = len(self.interface.databases)
        expected = 1

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
