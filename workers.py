from xmlrpc.client import boolean
import json
from tkinter import *

root = Tk()
root.title("Employees database")


list_of_employees = {}


class employee:
    def __init__(self, name, ID, department, title, wage_h, hours_week):
        self.name = name
        self.ID = ID
        self.department = department
        self.title = title
        self.wage_h = wage_h
        self.hours_week = hours_week
        list_of_employees[self.ID] = self


    #wyplata brutto za tydzien pracy
    def pay_brutto(self, wage_h, hours_week):
        extra_hours = hours_week - 35
        if extra_hours < 0:
            extra_hours = 0
        return (wage_h * hours_week + (1.5 * wage_h * extra_hours))


    #wplata na plan emerytalny co tydzien
    def rent_weekly(self):
        pay = self.pay_brutto(self.wage_h, self.hours_week)
        return (pay * 0.03)

    def __str__(self) -> str:
        return f'Name: {self.name}; ID: {self.ID}; Department: {self.department}; Title: {self.title}'




class worker (employee):
    def __init__(self, name, ID, department, title, wage_h, hours_week, is_day_shift):
        super().__init__(name, ID, department, title, wage_h, hours_week)
        if type(is_day_shift) != bool:
            print("Please enter whether the shift is during day: 'True' or 'False'")
        else:
            self.is_day_shift = is_day_shift
        list_of_employees[self.ID] =  self


    def __str__(self) -> str:
        return f'Name: {self.name}; ID: {self.ID}; Department: {self.department}; Title: {self.title}; IsOnDayShift: {self.is_day_shift}'




employee1 = employee("Alex", 1, "Logistics", "Manager", 15, 40)
employee2 = worker('Jacob', 15, 'Security', 'Officer', 10, 30, True)
employee3 = employee("Bob", 3, "Analysis", "Intern", 3, 35)





#1. Znalezienie pracownika
def findEmployee(number):
    print(list_of_employees.get(number))
    print('\n')

#2. Znalezienie pracownika wdg departmentu
def lookByDepartment(name_of_department):
    for number in list_of_employees:
        if list_of_employees.get(number).department == name_of_department:
            print('Name: ' + list_of_employees.get(number).name)
            print('ID: ' + str(list_of_employees.get(number).ID))
            print('Title: ' + list_of_employees.get(number).title + '\n')
            print('\n')

#3. Dodanie nowego pracownika - zakladam ze pracownik juz istnieje i tylko dodaje go na liste
#nie tworze nowego obiektu
def addNewEmployee(new_employee: employee):
    list_of_employees.update({new_employee.ID: new_employee})
    print('\n')

#4. Zmiana cech pracownika
def changeEmployee(number):
    list_of_employees.get(number).title = input("Enter new title: \n")
    print('\n')

#5. Usuniecie pracownika z listy
def removeEmployee(number):
    list_of_employees.pop(number)
    print('\n')

#6. Wyswietlanie slownika
def showAllEmployees():
    print("LIST OF EMPLOYEES\n")
    for employee in list_of_employees:
        print('Name: ' + list_of_employees.get(employee).name)
        print('ID: ' + str(list_of_employees.get(employee).ID))
        print('Department: ' + list_of_employees.get(employee).department)
        print('Title: ' + list_of_employees.get(employee).title)
        print('Wage per hour: ' + str(list_of_employees.get(employee).wage_h))
        print('Hours weekly: ' + str(list_of_employees.get(employee).hours_week) + '\n')
        print('\n')


#7. Wyjscie z programu
#if leave = True:
#    exit()

#TASK 1
#findEmployee(1)
#findEmployee(2)
#findEmployee(3)


#TASK 2
#lookByDepartment('Logistics')
#lookByDepartment('Security')
#lookByDepartment('Analysis')


#TASK 4
#findEmployee(1)
#changeEmployee(1)
#findEmployee(1)


#TASK 5
#showAllEmployees()
#removeEmployee(3)
#showAllEmployees()


#TASK3
#showAllEmployees()
#print('-------')
#removeEmployee(3)
#showAllEmployees()
#print('-------')
#addNewEmployee(employee3)
#showAllEmployees()
#print('-------')


#TASK6
#showAllEmployees()

#Program
"""
leave = False
while leave == False:
    print('What would you like to do?\n')
    print("To find an employee by his ID type '1'\n")
    print("To find an employee by department type '2'\n")
    print("To find add new employee type '3'\n")
    print("To change sth about an employee type '4'\n")
    print("To fire an employee type '5'\n")
    print("To see list of all employees type '6'\n")
    print("To exit program type '7'\n")

    x = int(input("Please enter a number from 1 to 7\n"))
    print('\n')

    if x == 1:
        number = int(input("Type ID of employee\n"))
        findEmployee(number)
    elif x == 2:
        department = input("Type name of department")
        lookByDepartment(department)
    elif x == 3:
        number = int(input("Type ID of employee\n"))
        addNewEmployee(number)
    elif x == 4:
        number = int(input("Type ID of employee\n"))
        changeEmployee(number)
    elif x == 5:
        number = int(input("Type ID of employee\n"))
        removeEmployee(number)
    elif x == 6:
        showAllEmployees()
    elif x == 7:
        exit()
    else:
        print("Please choose number from 1 to 7\n")


    print("Conitune?\n")
    ans = input("Type 'yes' or 'no'\n")
    if ans == 'no':
        leave = True
    print('\n')
"""

#Program z gui
leave = False
while leave == False:

    isClicked = False

    main_field = Text(root, height=10, width = 100)
    main_field.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


    main_field.insert(END, "What would you like to do?\n")


    #dla innych guzikow
    def button_add():
        pass

    #do wyjscia z programu
    def leave_program():
        exit()

    #zeby zostac w programie
    def stay():
        isClicked = True
        pass


    def ending():
        main_field.insert(END, "Do you want to continue?\n")
        button1.grid_forget()
        button2.grid_forget()
        button3.grid_forget()
        button4.grid_forget()
        button5.grid_forget()
        button6.grid_forget()
        button7.grid_forget()
        stay_button = Button(root, text = 'Yes', padx=30, pady=10, command= stay)
        stay_button.grid(row=5, column=1)
        exit_button = Button(root, text = 'No', padx=30, pady=10, command=leave_program)
        exit_button.grid(row=5, column=3)
        if isClicked == True:
            stay_button.grid_forget()


    def button_6():
        main_field.delete('1.0', END)
        for employee in list_of_employees:
            main_field.insert(END, 'Name: ' + list_of_employees.get(employee).name + '; ')
            main_field.insert(END, 'ID: ' + str(list_of_employees.get(employee).ID) + '; ')
            main_field.insert(END, 'Department: ' + list_of_employees.get(employee).department + '; ')
            main_field.insert(END, 'Title: ' + list_of_employees.get(employee).title + ';\n')
        ending()

    #Przyciski
    button1 = Button(root, text = '1', padx=30, pady=10, command=button_add)
    button2 = Button(root, text = '2', padx=30, pady=10, command=button_add)
    button3 = Button(root, text = '3', padx=30, pady=10, command=button_add)
    button4 = Button(root, text = '4', padx=30, pady=10, command=button_add)
    button5 = Button(root, text = '5', padx=30, pady=10, command=button_add)
    button6 = Button(root, text = 'Display all employees', padx=30, pady=10, command=button_6)
    button7 = Button(root, text = 'Exit program', padx=30, pady=10, command=leave_program)

    button1.grid(row=5, column=1)
    button2.grid(row=5, column=2)
    button3.grid(row=5, column=3)
    button4.grid(row=6, column=1)
    button5.grid(row=6, column=2)
    button6.grid(row=6, column=3)
    button7.grid(row=7, column=2)







    #Zapisywanie do pliku


#    with open("pracownicy.txt", 'w') as f:
#        for key, value in list_of_employees.items():
#            f.write('%s:%s\n' % (key, value))

    root.mainloop()