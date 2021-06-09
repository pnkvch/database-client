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
            }
        ]

    def handleAddRecord(self, inputWindow, database):
        for (key, value) in self.entries.items():
            if "tableID" in key:
                continue
            database[key].append(value.get())
        inputWindow.destroy()
        self.entries = {}
        self.createMainInterface()

    def handleDeleteRecord(self, inputWindow, entry, database):
        for key in database.keys():
            if "tableID" in key:
                continue
            database[key].pop(int(entry.get()))
        inputWindow.destroy()
        self.createMainInterface()

    def addRowToTable(self, database):
        inputWindow = Toplevel(self.root)

        for index, (key) in enumerate(database.keys()):
            if "tableID" in key:
                continue
            Label(inputWindow, text=key).grid(row=index, column=0)
            entry = Entry(inputWindow, bd=5)
            entry.grid(row=index, column=1)
            self.entries[key] = entry

        inputBtn = Button(inputWindow, text='Submit Data',
                          command=lambda: self.handleAddRecord(inputWindow, database))
        inputBtn.grid(row=len(database.items()) + 1, column=0)

    def removeRowToTable(self, database):
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Row ID").grid(row=1, column=0)
        entry = Entry(inputWindow, bd=5)
        entry.grid(row=2, column=1)

        inputBtn = Button(inputWindow, text='Submit Data',
                          command=lambda: self.handleDeleteRecord(inputWindow, entry, database))
        inputBtn.grid(row=len(database.items()) + 1, column=0)

    def createMainInterface(self):
        self.root.title("Database Client")
        Label(self.root, text='Database Client', font='Helvetica 28 bold').grid(
            row=0, column=0, columnspan=3, sticky="nsew", pady=10)

        if len(self.databases) == 0:
            Label(self.root, text='No available tables', font='Helvetica 14 bold').grid(
                row=1, column=1, sticky="nsew", pady=10)

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
