import pytest

from classes import *


def test_create_manager():
    simple_employee = Employee("John", "Smith", "other@mail.com")
    simple_manager = Manager("John", "Smith", "test@test.pl", 14000, [simple_employee])
    assert simple_manager.get_money() == 14000


def test_create_manager_wrong_list():
    with pytest.raises(OnlyEmployeesListException):
        simple_employee = Employee("John", "Smith", "other@mail.com")
        simple_manager = Manager("John", "Smith", "test@test.pl", 14000, [simple_employee, 1])
        assert simple_manager.get_money() == 14000


def test_create_employee():
    simple_employee = Employee("John", "Smith", "test@mail.com")
    assert simple_employee.get_name() == "John"
    assert simple_employee.get_surname() == "Smith"
    assert simple_employee.get_email() == "test@mail.com"


def test_create_employee_wrong_email():
    with pytest.raises(WrongEmailException):
        simple_employee = Employee("John", "Smith", "cat")
        assert simple_employee.get_name() == "John"
        assert simple_employee.get_surname() == "Smith"
        assert simple_employee.get_email() == "test@mail.com"
