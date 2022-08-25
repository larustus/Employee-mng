import os
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from jproperties import Properties

from model import Employee

# Please add some doc comments
config = Properties()


def init_config():
    with open('application.properties', 'rb') as config_file:
        config.load(config_file)


init_config()

STORAGE_FILE = str(config.get("app.storage.fileName").data)
DATA = {}

FONT_NAME = str(config.get("app.ui.fontType").data)
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

MOCK_DATA = {1: ["John", "IT", "Senior Developer", 1500.0, 40],
             5: ["Dave", "Logistics", "Manager", 3000.0, 35],
             3: ["Max", "PR", "Team leader", 2000.0, 40]}


def load_from_file_():
    if os.path.getsize(STORAGE_FILE) > 0:
        temp = pickle.load(open(STORAGE_FILE, 'rb'))
        return temp
    else:
        temp = {}
        return temp


temp_data = load_from_file_()
DATA = temp_data

x = (str(config.get("app.mode.test").data))
print(x)
if x == "False":
    x = False
else:
    x = True
print(x)


class EmployeeManager(tk.Tk):
    __SELECTED_RECORD_ID = -1

    def __init__(self):
        super().__init__()
        self.textFields = []
        self.title(str(config.get("app.name").data))
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
        self.textFields.append(self.textFiledId)
        self.textFiledName = tk.Entry(self)
        self.textFields.append(self.textFiledName)
        self.textFiledDepartment = tk.Entry(self)
        self.textFields.append(self.textFiledDepartment)
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

        # Initial inputs in text fields
        def initial_input_id(e):
            self.textFiledId.delete(0, "end")

        def initial_input_name(e):
            self.textFiledName.delete(0, "end")

        def initial_input_department(e):
            self.textFiledDepartment.delete(0, "end")

        def initial_input_title(e):
            self.textFiledTitle.delete(0, "end")

        def initial_input_wage(e):
            self.textFiledWage.delete(0, "end")

        def initial_input_hours(e):
            self.textFiledWorkingHours.delete(0, "end")

        # TextFields placement
        self.textFiledId.place(x=LEFT_MARGIN * 5, y=72, height=TEXT_FIELD_HEIGHT,
                               width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledId.insert(0, "Insert number")
        self.textFiledId.bind("<FocusIn>", initial_input_id)
        # self.frame.bind("<Return>",
        #                 lambda event, a=10, b=20, c=30:
        #                 self.rand_func(a, b, c))
        self.textFiledId.bind("<FocusOut>",
                              lambda event, txf=self.textFiledId, func=self.val_tid: self.validate_text_field(txf,
                                                                                                              func,
                                                                                                              event))

        self.textFiledName.place(x=LEFT_MARGIN * 5, y=100, height=TEXT_FIELD_HEIGHT,
                                 width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledName.insert(0, "Insert name")
        self.textFiledName.bind("<FocusIn>", initial_input_name)
        self.textFiledName.bind("<FocusOut>",
                                lambda event, txf=self.textFiledName, func=self.val_name: self.validate_text_field(
                                    txf,
                                    func,
                                    event))

        self.textFiledDepartment.place(x=LEFT_MARGIN * 5, y=127, height=TEXT_FIELD_HEIGHT,
                                       width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledDepartment.insert(0, "Insert name")
        self.textFiledDepartment.bind("<FocusIn>", initial_input_department)
        self.textFiledDepartment.bind("<FocusOut>",
                                      lambda event, txf=self.textFiledDepartment,
                                             func=self.val_name: self.validate_text_field(
                                          txf,
                                          func,
                                          event))

        self.textFiledTitle.place(x=LEFT_MARGIN * 5, y=154, height=TEXT_FIELD_HEIGHT,
                                  width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledTitle.insert(0, "Insert name")
        self.textFiledTitle.bind("<FocusIn>", initial_input_title)
        self.textFiledTitle.bind("<FocusOut>",
                                 lambda event, txf=self.textFiledTitle,
                                        func=self.val_title: self.validate_text_field(
                                     txf,
                                     func,
                                     event))

        self.textFiledWage.place(x=LEFT_MARGIN * 5, y=181, height=TEXT_FIELD_HEIGHT,
                                 width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledWage.insert(0, "Insert number")
        self.textFiledWage.bind("<FocusIn>", initial_input_wage)
        self.textFiledWage.bind("<FocusOut>",
                                lambda event, txf=self.textFiledWage, func=self.val_twage: self.validate_text_field(
                                    txf,
                                    func,
                                    event))

        self.textFiledWorkingHours.place(x=LEFT_MARGIN * 5, y=218, height=TEXT_FIELD_HEIGHT,
                                         width=(TABLE_WIDTH - ((LEFT_MARGIN * 5) - LEFT_MARGIN)))
        self.textFiledWorkingHours.insert(0, "Insert number")
        self.textFiledWorkingHours.bind("<FocusIn>", initial_input_hours)
        self.textFiledWorkingHours.bind("<FocusOut>",
                                        lambda event, txf=self.textFiledWorkingHours,
                                               func=self.val_tfh: self.validate_text_field(txf,
                                                                                           func,
                                                                                           event))

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
        if x:
            self.btnMockData.place_forget()

        self.reload_table()

    def reload_table(self):
        for emp in DATA:
            self.tableEmployees.insert('', tk.END, values=(
                emp, DATA[emp][0], DATA[emp][1], DATA[emp][2], float(DATA[emp][3]), int(DATA[emp][4])))

    def val_tid(self):
        int(self.textFiledId.get())

    def val_name(self):
        if len(self.textFiledName.get()) != 0:
            self.textFiledName.config(background="white", foreground="black")
            return True
        else:
            raise ValueError("error")

    def val_twage(self):
        int(self.textFiledWage.get())

    def val_tfh(self):
        int(self.textFiledWorkingHours.get())

    def val_dep(self):
        if len(self.textFiledDepartment.get()) != 0:
            self.textFiledDepartment.config(background="white", foreground="black")
            return True
        else:
            raise ValueError("error")

    def val_title(self):
        if len(self.textFiledTitle.get()) != 0:
            self.textFiledTitle.config(background="white", foreground="black")
            return True
        else:
            raise ValueError("error")

    def validate_text_field(self, text_field, func, event):
        try:
            if func is not None:
                func()
            text_field.config(background="white", foreground="black")
            return True
        except ValueError:
            text_field.config(background="red", foreground="black")
            return False

    def selection(self, event):
        """
        Sets selection item and populates all the fields
        @:return id of selected record, otherwise if no selection, returns -1
        """
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

    # CRUD
    def register_employee(self):
        try:
            if not self.validate(None):
                raise ValueError("error")
        except ValueError:
            messagebox.showinfo("Employee manager", "Wrong inputs in form!")
        empl = Employee(str(self.textFiledName.get()), int(self.textFiledId.get()), str(self.textFiledDepartment.get()),
                        str(self.textFiledTitle.get()), str(self.textFiledWage.get()),
                        str(self.textFiledWorkingHours.get()))
        if DATA.keys().__contains__(empl.id):
            self.textFiledId.config(background="red", foreground="black")
        else:
            self.textFiledId.config(background="white", foreground="black")
            DATA.update({empl.id: [empl.name, empl.department, empl.title, empl.wage_h, empl.hours_week]})
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            self.save_to_file()

    def validate(self, event):
        # Exceptions
        id = self.validate_text_field(self.textFiledId, self.val_tid, None)
        name = self.validate_text_field(self.textFiledName, self.val_name, None)
        title = self.validate_textFieldTitle(self.textFiledId, self.val_title, None)
        department = self.validate_textFieldDepartment(self.textFiledId, self.val_dep, None)
        wage = self.validate_text_field(self.textFiledWage, self.val_twage, None)
        hours = self.validate_text_field(self.textFiledWorkingHours, self.val_tfh, None)
        return id and name and title and department and wage and hours

    def update_employee(self):
        if not self.is_selected():
            return
        if DATA.keys().__contains__(int(self.__SELECTED_RECORD_ID)):
            try:
                if not self.validate(None):
                    raise ValueError("error")
            except ValueError:
                messagebox.showinfo("Employee manager", "Wrong inputs in form!")
            previous_id = self.__SELECTED_RECORD_ID
            changed_id = int(self.textFiledId.get())
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            if previous_id == changed_id:
                self.textFiledId.config(background="white", foreground="black")
                DATA.update({int(self.__SELECTED_RECORD_ID): [str(self.textFiledName.get()),
                                                              str(self.textFiledDepartment.get()),
                                                              str(self.textFiledTitle.get()),
                                                              float(self.textFiledWage.get()),
                                                              int(self.textFiledWorkingHours.get())]})
                self.tableEmployees.delete(*self.tableEmployees.get_children())
                self.reload_table()
                self.save_to_file()
            else:
                self.textFiledId.config(background="red", foreground="black")
                messagebox.showerror("Employee manager", "Cannot change ID of an employee, use 'register' option "
                                                         "instead")
            self.__SELECTED_RECORD_ID = -1
        else:
            messagebox.showinfo("Employee manager", "Please select the record in the table")
        self.tableEmployees.delete(*self.tableEmployees.get_children())
        self.reload_table()

    def delete_employee(self):
        if not self.is_selected():
            return
        if DATA.keys().__contains__(int(self.__SELECTED_RECORD_ID)):
            del DATA[int(self.__SELECTED_RECORD_ID)]
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            self.save_to_file()
        else:
            messagebox.showinfo("Employee manager", "Please select the record in the table")

    def clear_all(self):
        self.textFiledId.delete(0, tk.END)
        self.textFiledId.config(background="white", foreground="black")
        self.textFiledName.delete(0, tk.END)
        self.textFiledName.config(background="white", foreground="black")
        self.textFiledDepartment.delete(0, tk.END)
        self.textFiledDepartment.config(background="white", foreground="black")
        self.textFiledTitle.delete(0, tk.END)
        self.textFiledTitle.config(background="white", foreground="black")
        self.textFiledWage.delete(0, tk.END)
        self.textFiledWage.config(background="white", foreground="black")
        self.textFiledWorkingHours.delete(0, tk.END)
        self.textFiledWorkingHours.config(background="white", foreground="black")

    def reload_all(self):
        reload_dict = load_from_file_()
        DATA.clear()
        DATA.update(reload_dict)
        self.tableEmployees.delete(*self.tableEmployees.get_children())
        self.reload_table()
        self.save_to_file()

    # temporary
    def load_data(self):
        list_of_keys = list(MOCK_DATA.keys())
        list_of_values = []
        for item in MOCK_DATA:
            list_of_values.append(MOCK_DATA[item])
        if DATA.keys().__contains__(1) and DATA.keys().__contains__(5) and DATA.keys().__contains__(3):
            messagebox.showwarning("Employee manager", "This ID is already taken!")

        if not DATA.keys().__contains__(1):
            DATA.update({list_of_keys[0]: list_of_values[0]})
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            self.save_to_file()
        if not DATA.keys().__contains__(5):
            DATA.update({list_of_keys[1]: list_of_values[1]})
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            self.save_to_file()
        if not DATA.keys().__contains__(3):
            DATA.update({list_of_keys[2]: list_of_values[2]})
            self.tableEmployees.delete(*self.tableEmployees.get_children())
            self.reload_table()
            self.save_to_file()

    def save_to_file(self):
        with open(STORAGE_FILE, 'wb') as convert_file:
            pickle.dump(DATA, convert_file, protocol=pickle.HIGHEST_PROTOCOL)


def exiting():
    with open(STORAGE_FILE, 'wb') as convert_file:
        pickle.dump(DATA, convert_file, protocol=pickle.HIGHEST_PROTOCOL)
    app.destroy()


if __name__ == "__main__":
    app = EmployeeManager()
    app.protocol("WM_DELETE_WINDOW", exiting)
    app.mainloop()
