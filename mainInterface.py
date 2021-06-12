from tkinter import *
from tkinter import ttk


class MainInterface:
    def __init__(self, root):
        self.root = root
        self.entries = {}
        self.warningLabels = []
        self.databases = []
        self.dataToInsert = []
        self.dataTypes = []
        self.availableTypes = {
            "Integer": int,
            "Real Number": float,
            "Text": str
        }

    def createEntries(self, inputWindow, database):
        """
            This funciton creates entries in a window to add row values to insert into a table.
        """
        for index, (key) in enumerate(database.keys()):
            if "tableID" in key or "tableName" in key:
                continue
            Label(inputWindow, text=key).grid(row=index, column=0, padx=5)
            entry = Entry(inputWindow)
            entry.grid(row=index, column=1, padx=5)
            self.entries[key] = entry

    def handleAddRecord(self, inputWindow, database):
        """
            This function adds rows to a selected database from self.database and also verifies if the type is correct.
        """
        for (key, value) in self.entries.items():
            if "tableID" in key or "tableName" in key:
                continue
            types = next(
                x for x in self.dataTypes if x["tableID"] == database["tableID"])
            try:
                types[key](value)
            except ValueError:
                self.entries = {}
                self.createEntries(inputWindow, database)
                Label(inputWindow, text=f"{value} is not the correct type").grid(
                    row=len(database.items()) + 2, column=0)
                return
        for (key, value) in self.entries.items():
            if "tableID" in key or "tableName" in key:
                continue
            result = types[key](value)
            database[key].append(result)
        inputWindow.destroy()
        self.entries = {}
        # self.createMainInterface()

    def handleDeleteRecord(self, inputWindow, entry, database):
        """
            This function deletes row using an index from a selected database from self.database and also verifies if the index is exists.
        """
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

    def verifyDeleteRow(self, inputWindow, entry, database):
        """
            This function verifies if the user intended to delete the row.
        """
        verificationWindow = Toplevel(inputWindow)
        Label(verificationWindow, text=f"Do you want to row with index {entry.get()}?").grid(
            row=0, column=0)

        yesBtn = Button(verificationWindow, text="Yes",
                        command=lambda: (self.handleDeleteRecord(inputWindow, entry, database), verificationWindow.destroy()))
        yesBtn.grid(row=1, column=0)
        noBtn = Button(verificationWindow, text="No",
                       command=verificationWindow.destroy)
        noBtn.grid(row=1, column=1)

    def addTableRow(self, database):
        """
            This function adds a row to a selected table from self.databases.
        """
        inputWindow = Toplevel(self.root)
        self.createEntries(inputWindow, database)
        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.handleAddRecord(inputWindow, database))
        inputBtn.grid(row=len(database.items()) + 1,
                      column=0, columnspan=2, pady=10)

    def deleteTableRow(self, database):
        """
            This function creates window to enter row index and on button click verifies if user intended to delete a row.
        """
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter the index of a row to delete:").grid(
            row=1, column=0, padx=15, pady=10)
        entry = Entry(inputWindow)
        entry.grid(row=1, column=1, padx=15, pady=10)

        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.verifyDeleteRow(inputWindow, entry, database))
        inputBtn.grid(row=len(database.items()), column=0,
                      columnspan=2, padx=15, pady=5)

    def addEntryBox(self, inputWindow, addRowBtn, submitBtn):
        """
            This function creates window to enter row index and on button click verifies if user intended to delete a row.
        """
        nextRow = len(self.entries) + 3

        for item in self.warningLabels:
            item.destroy()

        entry = Entry(inputWindow)
        entry.grid(row=nextRow, column=0, padx=15)
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
        """
            This function adds table to a database from self.database and also verifies if every entry is populated.
        """
        if not tableName.strip():
            label = Label(inputWindow, text="Name of table cannot be empty!")
            label.grid(
                row=len(self.entries) + 6, column=0, columnspan=2, pady=10, padx=10)
            self.warningLabels.append(label)
            return
        for item in self.entries.keys():
            if not item.strip():
                label = Label(
                    inputWindow, text="Name of column cannot be empty!")
                label.grid(
                    row=len(self.entries) + 6, column=0, columnspan=2, pady=10, padx=10)
                self.warningLabels.append(label)
                return

        result = {key: self.availableTypes[value] for
                  key, value in self.entries.items()}
        ids = [item["tableID"] for item in self.databases]
        if not ids:
            result["tableID"] = 0
        else:
            result["tableID"] = max(ids) + 1
        self.dataTypes.append(result)
        database = {}
        for key, value in result.items():
            if "tableID" in key:
                database[key] = value
                continue
            database[key] = []
        database["tableName"] = tableName
        self.databases.append(database)

        self.entries = {}
        inputWindow.destroy()
        # self.createMainInterface()

    def addTable(self):
        """
            This function gives user entries to create table. Table can be of an unlimited size.
        """
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter table name:").grid(
            row=0, column=0, columnspan=2)

        tableName = Entry(inputWindow)
        tableName.grid(row=1, column=0, columnspan=2)

        Label(inputWindow, text="Enter column name and select it's type:").grid(
            row=2, column=0, columnspan=2, pady=10, padx=10)

        submitBtn = Button(inputWindow, text="Submit Data",
                           command=lambda: self.handleAddTable(inputWindow, tableName))
        addRowBtn = Button(inputWindow, text="Add Column",
                           command=lambda: self.addEntryBox(inputWindow, addRowBtn, submitBtn))
        addRowBtn.grid(row=len(self.entries) + 3,
                       column=0, columnspan=2, pady=10)
        self.addEntryBox(inputWindow, addRowBtn, submitBtn)

    def handleDeleteTable(self, inputWindow, entry):
        """
            This function deletes a table from database and also deletes it's data types. It also verifies in index is a nnumber and the table with this index exists.
        """
        try:
            tableIndex = int(entry.get())
        except ValueError:
            Label(inputWindow, text=f"{entry.get()} is not integer").grid(
                row=4, column=0)
            return
        if tableIndex >= len(self.databases):
            Label(inputWindow, text=f"{entry.get()} doesn't exist").grid(
                row=4, column=0)
            return
        self.databases.pop(tableIndex)
        self.dataTypes.pop(tableIndex)
        inputWindow.destroy()
        self.createMainInterface()

    def verifyDeleteTable(self, inputWindow, entry):
        """
            This function verifies if the user intended to delete the table.
        """
        verificationWindow = Toplevel(inputWindow)
        Label(verificationWindow, text=f"Do you want to delete table with index {entry.get()}?").grid(
            row=0, column=0)

        yesBtn = Button(verificationWindow, text="Yes",
                        command=lambda: (self.handleDeleteTable(inputWindow, entry), verificationWindow.destroy()))
        yesBtn.grid(row=1, column=0)
        noBtn = Button(verificationWindow, text="No",
                       command=verificationWindow.destroy)
        noBtn.grid(row=1, column=1)

    def deleteTable(self):
        """
            This function creates window to enter table index and on button click verifies if user intended to delete a table.
        """
        inputWindow = Toplevel(self.root)

        Label(inputWindow, text="Enter the index of a table to delete:").grid(
            row=1, column=0,  padx=15, pady=10)
        entry = Entry(inputWindow)
        entry.grid(row=2, column=1)

        inputBtn = Button(inputWindow, text="Submit Data",
                          command=lambda: self.verifyDeleteTable(inputWindow, entry))
        inputBtn.grid(row=2, column=0)

    def createMainInterface(self):
        """
            This is the main funciton of a program. It creates main view with TreeView and appends data to it. It adds buttons to manipulate tables and rows.
        """
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
                                  command=lambda index=i: self.addTableRow(self.databases[index]))
            removeRowButton = Button(rowButtonsFrame, text='Remove Row', font='Helvetica 14',
                                     command=lambda index=i: self.deleteTableRow(self.databases[index]))
            rowButtonsFrame.grid(row=i + 1, column=len(self.databases[i]) - 1)
            tableName.grid(row=0, column=0)
            addRowButton.grid(row=1, column=0)
            removeRowButton.grid(row=2, column=0)

            tableButtonsFrame = Frame(self.root)
            addTableButton = Button(tableButtonsFrame, text='Add Table', font='Helvetica 14',
                                    command=self.addTable)
            removeTableButton = Button(tableButtonsFrame, text='Remove Table', font='Helvetica 14',
                                       command=self.deleteTable)
            tableButtonsFrame.grid(row=len(self.databases) + 1, column=0, columnspan=max(
                [len(item) for item in self.databases]) - 1)
            addTableButton.grid(row=0, column=0, pady=10)
            removeTableButton.grid(row=0, column=1, pady=10)
        self.root.bind("<Escape>", lambda event: self.root.destroy())
