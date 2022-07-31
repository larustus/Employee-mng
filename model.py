class Employee:
    STANDARD_HRS = 35
    RETIREMENT = 0.03
    OVERTIME = 1.5

    def __init__(self, name="NULL", id="NULL", department="NULL", title="NULL", wage_h=0.00, hours_week=0):
        self.name = name
        self.id = id
        self.department = department
        self.title = title
        self.wage_h = float(wage_h)
        self.hours_week = int(hours_week)
        self.__wage_weekly = self.wage_weekly()

    def wage_weekly(self):
        return (self.hours_week - self.STANDARD_HRS) * (self.wage_h * self.OVERTIME) + self.hours_week * self.wage_h \
            if int(self.hours_week) > int(self.STANDARD_HRS) \
            else self.hours_week * self.wage_h

    def retirement_amount(self):
        return self.RETIREMENT * self.__wage_weekly

    def __str__(self) -> str:
        return f"Employee {self.name} {self.id}"


class Worker(Employee):
    def __init__(self, is_day_shift, name="NULL", id="NULL", department="NULL", title="NULL", wage_h=0.00,
                 hours_week=0):
        super().__init__(name, id, department, title, wage_h, hours_week)
        self.is_day_shift = is_day_shift

    def __str__(self) -> str:
        return f"Worker {self.name} {self.id}"
