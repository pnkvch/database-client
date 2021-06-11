from tkinter import *
from tkinter import ttk


class MainInterface:
    def __init__(self, root) -> None:
        self.root = root
        self.entries = {}
        self.databases = [
            {
                "ID": [23, 5, 25, 2, 9],
                "name": ["Artur", "Pavel", "Vlad", "Stot", "wfw"],
                "age": [22, 31, 54, 44, 10],
                "tableID": 0,
                "tableName": "table Name"
            }
        ]
        self.dataToInsert = []
        self.dataTypes = [
            {
                "ID": int,
                "name": str,
                "age": int,
                "tableID": 0
            }
        ]
        self.availableTypes = {
            "Integer": int,
            "Real Number": float,
            "Text": str
        }

    def createEntries(self, inputWindow, database):
        for index, (key) in enumerate(database.keys()):
            if "tableID" in key or "tableName" in key:
                continue
            Label(inputWindow, text=key).grid(row=index, column=0)
            entry = Entry(inputWindow)
            entry.grid(row=index, column=1)
            self.entries[key] = entry

    def handleAddRecord(self, inputWindow, database):
        for (key, value) in self.entries.items():
            if "tableID" in key or "tableName" in key:
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
            if "tableID" in key or "tableName" in key:
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
            if "tableID" in key or "tableName" in key:
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
        entry = Entry(inputWindow)
        entry.grid(row=2, column=1)

        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.handleDeleteRecord(inputWindow, entry, database))
        inputBtn.grid(row=len(database.items()) + 1, column=0)

    def addEntryBox(self, inputWindow, addRowBtn, submitBtn):
        nextRow = len(self.entries) + 1

        entry = Entry(inputWindow)
        entry.grid(row=nextRow, column=0)
        variable = StringVar(inputWindow)
        textTypes = list(self.availableTypes.keys())
        variable.set(textTypes[0])
        dropdown = OptionMenu(
            inputWindow, variable, *textTypes)
        dropdown.grid(row=nextRow, column=1, padx=15)
        addRowBtn.grid(row=nextRow + 3, column=0)
        submitBtn.grid(row=nextRow + 3, column=1, padx=15)
        self.entries[entry] = variable

    def handleAddTable(self, inputWindow, tableName):
        for item in self.entries.keys():
            if not item.get():
                Label(inputWindow, text="Name of column cannot be empty!").grid(
                    row=len(self.entries) + 5, column=0, columnspan=2, pady=10, padx=10)
                return

        result = {key.get(): self.availableTypes[value.get()] for
                  key, value in self.entries.items()}
        ids = [item["tableID"] for item in self.databases]
        if not ids:
            result["tableID"] = 0
        else:
            result["tableID"] = max(ids) + 1
        self.dataTypes.append(result)
        database = {}
        for key, value in result.items():
            if key in "tableID":
                database[key] = value
                continue
            database[key] = []
        database["tableName"] = tableName.get()
        self.databases.append(database)

        self.entries = {}
        inputWindow.destroy()
        self.createMainInterface()

    def addTable(self):
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter column name and select it's type:").grid(
            row=0, column=0, columnspan=2, pady=10, padx=10)

        Label(inputWindow, text="Enter table name:").grid(
            row=1, column=0, columnspan=2, pady=10, padx=10)

        tableName = Entry(inputWindow)
        tableName.grid(row=1, column=1)

        submitBtn = Button(inputWindow, text='Submit Data',
                           command=lambda: self.handleAddTable(inputWindow, tableName))
        addRowBtn = Button(inputWindow, text='Add Column',
                           command=lambda: self.addEntryBox(inputWindow, addRowBtn, submitBtn))
        addRowBtn.grid(row=len(self.entries) + 2,
                       column=0, columnspan=2, pady=10)

    def handleDeleteTable(self, inputWindow, entry):
        try:
            tableIndex = int(entry.get())
        except ValueError:
            Label(inputWindow, text=f"{entry.get()} is not integer").grid(
                row=4, column=0)
            return

        self.databases.pop(tableIndex)
        self.dataTypes.pop(tableIndex)
        inputWindow.destroy()
        self.createMainInterface()

    def removeTable(self):
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter the index of a table to delete:").grid(
            row=1, column=0)
        entry = Entry(inputWindow)
        entry.grid(row=2, column=1)

        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.handleDeleteTable(inputWindow, entry))
        inputBtn.grid(row=3, column=0)

    def createMainInterface(self):
        self.root.title("Database Client")
        for widget in self.root.winfo_children():
            widget.destroy()
        Label(self.root, text='Database Client', font='Helvetica 28 bold').grid(
            row=0, column=0, sticky="nsew", pady=10)

        if len(self.databases) == 0:
            Label(self.root, text='No available tables', font='Helvetica 14 bold').grid(
                row=1, column=0, pady=10)
            Button(self.root, text='Add Table', font='Helvetica 14',
                   command=self.addTable).grid(row=2, column=0)

        for i in range(len(self.databases)):
            items = list(self.databases[i].keys())
            items.pop(len(items) - 1)
            items.pop(len(items) - 1)
            cols = tuple(items)

            listBox = ttk.Treeview(
                self.root, columns=cols, show='headings', selectmode='browse')
            for col in cols:
                listBox.heading(col, text=col)
            listBox.grid(row=i + 1, column=0)

            for (key, values) in self.databases[i].items():
                if "tableID" in key or "tableName" in key:
                    continue
                self.dataToInsert.append(values)
            self.dataToInsert = list(zip(*self.dataToInsert))

            for data in self.dataToInsert:
                listBox.insert("", "end", values=(data))
            self.dataToInsert = []
            rowButtonsFrame = Frame(self.root)
            tableName = Label(
                rowButtonsFrame, text=self.databases[i]["tableName"], font='Helvetica 14 bold')
            addRowButton = Button(rowButtonsFrame, text='Add Row', font='Helvetica 14',
                                  command=lambda index=i: self.addRowToTable(self.databases[index]))
            removeRowButton = Button(rowButtonsFrame, text='Remove Row', font='Helvetica 14',
                                     command=lambda index=i: self.removeRowToTable(self.databases[index]))
            rowButtonsFrame.grid(row=i + 1, column=len(self.databases[i]) - 1)
            tableName.grid(row=0, column=0)
            addRowButton.grid(row=1, column=0)
            removeRowButton.grid(row=2, column=0)

            tableButtonsFrame = Frame(self.root)
            addTableButton = Button(tableButtonsFrame, text='Add Table', font='Helvetica 14',
                                    command=self.addTable)
            removeTableButton = Button(tableButtonsFrame, text='Remove Table', font='Helvetica 14',
                                       command=self.removeTable)
            tableButtonsFrame.grid(row=len(self.databases) + 1, column=0, columnspan=max(
                [len(item) for item in self.databases]) - 1)
            addTableButton.grid(row=0, column=0, pady=10)
            removeTableButton.grid(row=0, column=1, pady=10)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
