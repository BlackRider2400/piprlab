

class WrongEmailException(Exception):
    def __init__(self):
        self.message = "Email error."


class OnlyEmployeesListException(Exception):
    def __init__(self):
        self.message = "You can only put Employee in your list."


class Employee:

    def __init__(self, name, surname, email):
        self._name = name
        self._surname = surname
        if "@" in email and "." in email:
            self._email = email
        else:
            raise WrongEmailException

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_email(self):
        return self._email

    def set_name(self, name):
        self._name = name

    def set_surname(self, surname):
        self._surname = surname

    def set_email(self, email):
        if "@" in email and "." in email:
            self._email = email
        else:
            raise WrongEmailException

#programista: jezyk, pensja miesieczna
#manager: lista pracownikow, pensja miesieczna
#pracownik techniczny: stawka godzinowa, ilosc godzin w miesiacu


class C2BEmployee(Employee):

    def __init__(self, name, surname, email, money):
        super().__init__(name, surname, email)
        if money >= 0:
            self._money = money
        else:
            raise ValueError

    def get_money(self):
        return self._money

    def set_money(self, money):
        if money >= 0:
            self._money = money
        else:
            raise ValueError


class Programmer(C2BEmployee):

    def __init__(self, name, surname, email, money, language):
        super().__init__(name, surname, email, money)
        self._language = language

    def get_language(self):
        return self._language

    def set_language(self, language):
        self._language = language


class Manager(C2BEmployee):

    def __init__(self, name, surname, email, money, employees):
        super().__init__(name, surname, email, money)
        self._employees = []
        for i in employees:
            if type(i) == Employee:
                self._employees.append(i)
            else:
                raise OnlyEmployeesListException

    def get_employees(self):
        return self._employees

    def set_employees(self, employees):
        self._employees = []
        for i in employees:
            if type(i) == Employee:
                self._employees.append(i)
            else:
                raise OnlyEmployeesListException

    def delete_employee(self, employee):
        if type(employee) != Employee:
            raise ValueError

        self._employees.remove(employee)

    def add_employee(self, employee):
        if type(employee) != Employee:
            raise ValueError

        self._employees.append(employee)
