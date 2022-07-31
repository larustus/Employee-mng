import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

FONT_NAME = "Helvetica"
FONT_HEADER_SIZE = 14
FONT_REGULAR_SIZE = 10

LEFT_MARGIN = 40
TITLE_MARGIN = LEFT_MARGIN * 6
WIDE_MARGIN = LEFT_MARGIN * 4
COMPONENT_MARGIN = 5
TABLE_WIDTH = 640
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 25
TEXT_FIELD_HEIGHT = 21
LABEL_HEIGHT = 23

MOCK_DATA = [[1, "John", "IT", "1500", "40", "Senior Developer"]]


class EmployeeManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Manager")
        self.geometry("750x650+350+170")

        # Lbls definition
        self.lblTitle = tk.Label(self, text="Employee Manager App (c)", font=(FONT_NAME, FONT_HEADER_SIZE))
        self.lblId = tk.Label(self, text="Id: ", font=(FONT_NAME, FONT_REGULAR_SIZE))
        self.lblName = tk.Label(self, text="Name: ", font=(FONT_NAME, FONT_REGULAR_SIZE))
        self.lblDepartment = tk.Label(self, text="Department: ", font=(FONT_NAME, FONT_REGULAR_SIZE))
        self.lblJobTitle = tk.Label(self, text="Title: ", font=(FONT_NAME, FONT_REGULAR_SIZE))
        self.lblWage = tk.Label(self, text="Wage: ", font=(FONT_NAME, FONT_REGULAR_SIZE))
        self.lblWorkingHours = tk.Label(self, text="Working hours: ", font=(FONT_NAME, FONT_REGULAR_SIZE))

        # TextFields definition
        self.textFiledId = tk.Entry(self)
        self.textFiledName = tk.Entry(self)
        self.textFiledDepartment = tk.Entry(self)
        self.textFiledTitle = tk.Entry(self)
        self.textFiledWage = tk.Entry(self)
        self.textFiledWorkingHours = tk.Entry(self)

        # Buttons definition
        self.btnRegister = tk.Button(self, text="Register", font={FONT_NAME, FONT_REGULAR_SIZE},
                                     command=self.registerEmployee)
        self.btnUpdate = tk.Button(self, text='Update', font={FONT_NAME, FONT_REGULAR_SIZE},
                                   command=self.updateEmployee)
        self.btnDelete = tk.Button(self, text='Delete', font={FONT_NAME, FONT_REGULAR_SIZE},
                                   command=self.deleteEmployee)
        self.btnClear = tk.Button(self, text='Clear', font={FONT_NAME, FONT_REGULAR_SIZE}, command=self.clearAll)
        self.btnReload = tk.Button(self, text='Reload', font={FONT_NAME, FONT_REGULAR_SIZE}, command=self.reloadAll)

        # Table definition
        columns = ["#1", "#2", "#3", "#4", "#5", "#6"]
        self.tableEmployees = ttk.Treeview(self, show="headings", height=5, columns=columns)
        self.tableEmployees.heading('#1', text="Id", anchor='center')
        self.tableEmployees.column('#1', width=10, anchor='center', stretch=False)
        self.tableEmployees.heading('#2', text="Name", anchor='center')
        self.tableEmployees.column('#2', width=10, anchor='center', stretch=False)
        self.tableEmployees.heading('#3', text="Department", anchor='center')
        self.tableEmployees.column('#3', width=10, anchor='center', stretch=False)
        self.tableEmployees.heading('#4', text="Wage", anchor='center')
        self.tableEmployees.column('#4', width=10, anchor='center', stretch=False)
        self.tableEmployees.heading('#5', text="Working hours", anchor='center')
        self.tableEmployees.column('#5', width=10, anchor='center', stretch=False)
        self.tableEmployees.heading('#6', text="Title", anchor='center')
        self.tableEmployees.column('#6', width=10, anchor='center', stretch=False)

        # Scroll bars definition

        # Lbls placement
        self.lblTitle.place(x=TITLE_MARGIN, y=30, height=47, width=300)
        self.lblId.place(x=LEFT_MARGIN, y=75, height=LABEL_HEIGHT, width=45)
        self.lblName.place(x=LEFT_MARGIN, y=102, height=LABEL_HEIGHT, width=65)
        self.lblDepartment.place(x=LEFT_MARGIN, y=129, height=LABEL_HEIGHT, width=99)
        self.lblJobTitle.place(x=LEFT_MARGIN, y=156, height=LABEL_HEIGHT, width=99)
        self.lblWage.place(x=LEFT_MARGIN, y=183, height=LABEL_HEIGHT, width=99)
        self.lblWorkingHours.place(x=LEFT_MARGIN, y=220, height=LABEL_HEIGHT, width=99)

        # TextFields placement
        self.textFiledId.place(x=LEFT_MARGIN * 5, y=72, height=TEXT_FIELD_HEIGHT,
                               width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledName.place(x=LEFT_MARGIN * 5, y=100, height=TEXT_FIELD_HEIGHT,
                                 width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledDepartment.place(x=LEFT_MARGIN * 5, y=127, height=TEXT_FIELD_HEIGHT,
                                       width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledTitle.place(x=LEFT_MARGIN * 5, y=154, height=TEXT_FIELD_HEIGHT,
                                  width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledWage.place(x=LEFT_MARGIN * 5, y=181, height=TEXT_FIELD_HEIGHT,
                                 width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledWorkingHours.place(x=LEFT_MARGIN * 5, y=218, height=TEXT_FIELD_HEIGHT,
                                         width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))

        # Table placement
        self.tableEmployees.place(x=LEFT_MARGIN, y=340, height=200, width=TABLE_WIDTH)

        # Buttons placement
        self.btnRegister.place(x=WIDE_MARGIN, y=285, height=BUTTON_HEIGHT, width=BUTTON_WIDTH)
        self.btnUpdate.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 1 + COMPONENT_MARGIN * 1), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)
        self.btnDelete.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 2 + COMPONENT_MARGIN * 2), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)
        self.btnClear.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 3 + COMPONENT_MARGIN * 3), y=285, height=BUTTON_HEIGHT,
                            width=BUTTON_WIDTH)
        self.btnReload.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 4 + COMPONENT_MARGIN * 4), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)


    def registerEmployee(self):
      print('registerEmployee method invoked')
      pass


    def updateEmployee(self):
      print('updateEmployee method invoked')
      pass


    def deleteEmployee(self):
      print('deleteEmployee method invoked')
      pass


    def clearAll(self):
      print('clearAll method invoked')
      pass


    def reloadAll(self):
      print('reloadAll method invoked')
      pass

if __name__ == "__main__":
    app = EmployeeManager()
    app.mainloop()
