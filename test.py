from mainInterface import MainInterface
from tkinter import *
import unittest


class TestProject(unittest.TestCase):
    root = Tk()
    interface = MainInterface(root)

    # Before running tests remove all the .get() methods and comment out self.createMainInterface() method from tested function

    def test_0_AddTable(self):
        self.interface.entries = {
            "ID": "Integer",
            "name": "Text",
            "surname": "Text",
            "height": "Real Number"
        }

        result = {
            "ID": int,
            "name": str,
            "surname": str,
            "height": float,
            "tableID": 0
        }

        self.interface.handleAddTable(Toplevel(self.root), "test1")
        self.assertDictEqual(result, self.interface.dataTypes[0])

    def test_1_AddRowToATable(self):
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

    def test_2_AddRowToATable(self):
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

    def test_3_AddIncorrectRowToATable(self):
        self.interface.entries = {
            "ID": "cztery",
            "name": "bla",
            "surname": "bla",
            "height": -90
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


if __name__ == '__main__':
    unittest.main()
