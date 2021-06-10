from tkinter import *
from tkinter import ttk


class MainInterface:
    def __init__(self, root) -> None:
        self.root = root
        self.entries = {}
        self.databases = [
            {
                "tableID": 0,
                "ID": [23, 5, 25, 2, 9],
                "name": ["Artur", "Pavel", "Vlad", "Stot", "wfw"],
                "age": [22, 31, 54, 44, 10]
            },
            {
                "tableID": 1,
                "ID": [23, 5, 25, 2, 9],
                "name": ["Artur", "Pavel", "Vlad", "Stot", "wfw"],
                "age": [22, 31, 54, 44, 10]
            },
            {
                "tableID": 2,
                "ID": [23, 5, 25, 2, 9],
                "name": ["Artur", "Pavel", "Vlad", "Stot", "wfw"],
                "age": [22, 31, 54, 44, 10],
                "login":["Artur", "Pavel", "Vlad", "Stot", "wfw"],
            }
        ]
        self.dataToInsert = []
        self.dataTypes = [
            {
                "tableID": 0,
                "ID": int,
                "name": str,
                "age": int
            },
            {
                "tableID": 1,
                "ID": int,
                "name": str,
                "age": int
            },
            {
                "tableID": 2,
                "ID": int,
                "name": str,
                "age": int
            }
        ]

    def createEntries(self, inputWindow, database):
        for index, (key) in enumerate(database.keys()):
            if "tableID" in key:
                continue
            Label(inputWindow, text=key).grid(row=index, column=0)
            entry = Entry(inputWindow)
            entry.grid(row=index, column=1)
            self.entries[key] = entry

    def handleAddRecord(self, inputWindow, database):
        for (key, value) in self.entries.items():
            if "tableID" in key:
                continue
            types = next(
                x for x in self.dataTypes if x["tableID"] == database["tableID"])
            try:
                types[key](value.get())
            except ValueError:
                self.entries = {}
                self.createEntries(inputWindow, database)
                Label(inputWindow, text=f"{value.get()} is not the correct type").grid(
                    row=len(database.items()) + 2, column=0)
                return
        for (key, value) in self.entries.items():
            if "tableID" in key:
                continue
            result = types[key](value.get())
            database[key].append(result)
        inputWindow.destroy()
        self.entries = {}
        self.createMainInterface()

    def handleDeleteRecord(self, inputWindow, entry, database):
        try:
            rowID = int(entry.get())
        except ValueError:
            Label(inputWindow, text=f"{entry.get()} is not integer").grid(
                row=len(database.items()) + 2, column=0)
            return
        for key in database.keys():
            if "tableID" in key:
                continue
            if rowID > len(database[key]):
                Label(inputWindow, text=f"{rowID} doesn't exist").grid(
                    row=len(database.items()) + 2, column=0)
                return
            database[key].pop(rowID)
        inputWindow.destroy()
        self.createMainInterface()

    def addRowToTable(self, database):
        inputWindow = Toplevel(self.root)
        self.createEntries(inputWindow, database)
        inputBtn = Button(inputWindow, text='Submit Data',
                          command=lambda: self.handleAddRecord(inputWindow, database))
        inputBtn.grid(row=len(database.items()) + 1, column=0)

    def removeRowToTable(self, database):
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter the index of a row to delete:").grid(
            row=1, column=0)
        entry = Entry(inputWindow, bd=5)
        entry.grid(row=2, column=1)

        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.handleDeleteRecord(inputWindow, entry, database))
        inputBtn.grid(row=len(database.items()) + 1, column=0)

    def addTable(self):
        inputWindow = Toplevel(self.root)

        inputBtn = Button(inputWindow, text='Submit Data',
                          command=lambda: self.handleAddRecord(inputWindow))
        inputBtn.grid(row=0, column=2)

    def createMainInterface(self):
        self.root.title("Database Client")
        Label(self.root, text='Database Client', font='Helvetica 28 bold').grid(
            row=0, column=0, columnspan=3, sticky="nsew", pady=10)

        if len(self.databases) == 0:
            Label(self.root, text='No available tables', font='Helvetica 14 bold').grid(
                row=1, column=1, sticky="nsew", pady=10)
            Button(self.root, text='Add Table', font='Helvetica 14',
                   command=self.addTable).grid(row=2, column=0)

        for i in range(len(self.databases)):
            items = list(self.databases[i].keys())
            items.pop(0)
            cols = tuple(items)

            listBox = ttk.Treeview(
                self.root, columns=cols, show='headings')
            for col in cols:
                listBox.heading(col, text=col)
            listBox.grid(row=i + 1, column=0, columnspan=2)

            for (key, values) in self.databases[i].items():
                if "tableID" in key:
                    continue
                self.dataToInsert.append(values)
            self.dataToInsert = list(zip(*self.dataToInsert))

            for data in self.dataToInsert:
                listBox.insert("", "end", values=(data))
            self.dataToInsert = []
            Button(self.root, text='Add Row', font='Helvetica 14',
                   command=lambda index=i: self.addRowToTable(self.databases[index])).grid(row=i + 1, column=0)
            Button(self.root, text='Remove Row', font='Helvetica 14',
                   command=lambda index=i: self.removeRowToTable(self.databases[index])).grid(row=i + 1, column=1)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
