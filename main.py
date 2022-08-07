import tkinter as tk
from tkinter import ttk
from model import Employee
# extra import
from tkinter import messagebox

DATA = {}

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

MOCK_DATA = {1: ["John", "IT", "Senior Developer", "1500", "40"],
             5: ["Dave", "Logistics", "Manager", "3000", "35"],
             3: ["Max", "PR", "idk", "2000", "40"]}


class EmployeeManager(tk.Tk):
    __SELECTED_RECORD_ID = -1

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
                                     command=self.register_employee)
        self.btnUpdate = tk.Button(self, text='Update', font={FONT_NAME, FONT_REGULAR_SIZE},
                                   command=self.update_employee)
        self.btnDelete = tk.Button(self, text='Delete', font={FONT_NAME, FONT_REGULAR_SIZE},
                                   command=self.delete_employee)
        self.btnClear = tk.Button(self, text='Clear', font={FONT_NAME, FONT_REGULAR_SIZE}, command=self.clear_all)
        self.btnReload = tk.Button(self, text='Reload', font={FONT_NAME, FONT_REGULAR_SIZE}, command=self.reload_all)
        # extra button
        self.btnMockData = tk.Button(self, text='Load mock data', font={FONT_NAME, FONT_REGULAR_SIZE},
                                     command=self.load_data)

        # Table definition
        columns = ["#1", "#2", "#3", "#4", "#5", "#6"]
        self.tableEmployees = ttk.Treeview(self, show="headings", height=300, columns=columns)
        self.tableEmployees.heading('#1', text="Id", anchor='center')
        self.tableEmployees.column('#1', width=106, anchor='center', stretch=False)
        self.tableEmployees.heading('#2', text="Name", anchor='center')
        self.tableEmployees.column('#2', width=106, anchor='center', stretch=False)
        self.tableEmployees.heading('#3', text="Department", anchor='center')
        self.tableEmployees.column('#3', width=106, anchor='center', stretch=False)
        self.tableEmployees.heading('#4', text="Title", anchor='center')
        self.tableEmployees.column('#4', width=106, anchor='center', stretch=False)
        self.tableEmployees.heading('#5', text="Wage", anchor='center')
        self.tableEmployees.column('#5', width=106, anchor='center', stretch=False)
        self.tableEmployees.heading('#6', text="Working hours", anchor='center')
        self.tableEmployees.column('#6', width=106, anchor='center', stretch=False)

        # Scroll bars definition
        self.tableEmployees.bind("<<TreeviewSelect>>", self.selection)

        # Lbls placement
        self.lblTitle.place(x=TITLE_MARGIN, y=30, height=47, width=300)
        self.lblId.place(x=LEFT_MARGIN, y=75, height=LABEL_HEIGHT, width=45)
        self.lblName.place(x=LEFT_MARGIN, y=102, height=LABEL_HEIGHT, width=65)
        self.lblDepartment.place(x=LEFT_MARGIN, y=129, height=LABEL_HEIGHT, width=99)
        self.lblJobTitle.place(x=LEFT_MARGIN, y=156, height=LABEL_HEIGHT, width=99)
        self.lblWage.place(x=LEFT_MARGIN, y=183, height=LABEL_HEIGHT, width=99)
        self.lblWorkingHours.place(x=LEFT_MARGIN, y=220, height=LABEL_HEIGHT, width=200)

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
        self.btnUpdate.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 1 + COMPONENT_MARGIN * 10), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)
        self.btnDelete.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 2 + COMPONENT_MARGIN * 20), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)
        self.btnClear.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 3 + COMPONENT_MARGIN * 30), y=285, height=BUTTON_HEIGHT,
                            width=BUTTON_WIDTH)
        self.btnReload.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 4 + COMPONENT_MARGIN * 40), y=285, height=BUTTON_HEIGHT,
                             width=BUTTON_WIDTH)
        # extra button
        self.btnMockData.place(x=(WIDE_MARGIN + BUTTON_HEIGHT * 5 + COMPONENT_MARGIN * 50), y=285, height=BUTTON_HEIGHT,
                               width=BUTTON_WIDTH * 1.7)

    def selection(self, event):
        self.clear_all()
        item = []
        for selection in self.tableEmployees.selection():
            item = self.tableEmployees.item(selection)
        if len(item) != 0:
            id, name, department, title, wage, working_hours = item["values"][0:7]
            self.textFiledId.insert(0, id)
            self.textFiledName.insert(0, name)
            self.textFiledDepartment.insert(0, department)
            self.textFiledTitle.insert(0, title)
            self.textFiledWage.insert(0, wage)
            self.textFiledWorkingHours.insert(0, working_hours)
            self.__SELECTED_RECORD_ID = id
            return id
        return -1

    def is_selected(self):
        if self.__SELECTED_RECORD_ID == -1:
            messagebox.showinfo("Employee manager", "Please select the record in the table")
        return self.__SELECTED_RECORD_ID != -1

    def register_employee(self):
        empl = Employee(str(self.textFiledName.get()), int(self.textFiledId.get()), str(self.textFiledDepartment.get()),
                        str(self.textFiledTitle.get()), str(self.textFiledWage.get()),
                        str(self.textFiledWorkingHours.get()))
        if DATA.keys().__contains__(empl.id):
            messagebox.showwarning("Employee manager", "This ID is already taken!")
            # print("Id taken")
        else:
            DATA.update({empl.id: [empl.name, empl.department, empl.title, empl.wage_h, empl.hours_week]})
            # print(DATA)
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            for item in DATA:
                self.tableEmployees.insert('', tk.END, values=(
                    item, DATA[item][0], DATA[item][1], DATA[item][2], DATA[item][3], DATA[item][4]))

    def update_employee(self):
        if not self.is_selected():
            return
        if DATA.keys().__contains__(int(self.__SELECTED_RECORD_ID)):
            DATA.update({int(self.__SELECTED_RECORD_ID): [str(self.textFiledName.get()),
                                                          str(self.textFiledDepartment.get()),
                                                          str(self.textFiledTitle.get()),
                                                          float(self.textFiledWage.get()),
                                                          int(self.textFiledWorkingHours.get())]})
            self.reload_table()
        else:
            messagebox.showwarning("Employee manager", "Cannot update employee - there is no employee with that ID!")

    def reload_table(self):
        self.tableEmployees.delete(*self.tableEmployees.get_children())
        for emp in DATA:
            self.tableEmployees.insert('', tk.END, values=(
                emp, DATA[emp][0], DATA[emp][1], DATA[emp][2], DATA[emp][3], DATA[emp][4]))

    def delete_employee(self):
        if not self.is_selected():
            return
        if DATA.keys().__contains__(int(self.__SELECTED_RECORD_ID)):
            del DATA[int(self.__SELECTED_RECORD_ID)]
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            for item in DATA:
                self.tableEmployees.insert('', tk.END, values=(
                    item, DATA[item][0], DATA[item][1], DATA[item][2], DATA[item][3], DATA[item][4]))
        else:
            messagebox.showwarning("Employee manager", 'Cannot delete employee - there is no employee with that ID!')
            # print('Cannot delete employee - there is no employee with that ID!')
        # print(DATA)

    def clear_all(self):
        self.textFiledId.delete(0, tk.END)
        self.textFiledName.delete(0, tk.END)
        self.textFiledDepartment.delete(0, tk.END)
        self.textFiledTitle.delete(0, tk.END)
        self.textFiledWage.delete(0, tk.END)
        self.textFiledWorkingHours.delete(0, tk.END)
        # print('reloadAll method invoked')

    def reload_all(self):
        pass

    def load_data(self):
        if DATA.keys().__contains__(1 or 5 or 3):
            messagebox.showwarning("Employee manager", "This ID is already taken!")
        else:
            DATA.update(MOCK_DATA)
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            for item in DATA:
                self.tableEmployees.insert('', tk.END, values=(
                    item, DATA[item][0], DATA[item][1], DATA[item][2], float(DATA[item][3]), int(DATA[item][4])))
        # print("loadData method invoked")
        # print(DATA)


if __name__ == "__main__":
    app = EmployeeManager()
    emp = Employee()
    print(emp)
    app.mainloop()
