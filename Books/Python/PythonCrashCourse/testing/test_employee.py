import pytest
from employee import Employee

'''def test_give_custom_raise():
    emp = Employee('John', 'Doe', 60000)
    emp.give_custom_raise(7000)
    assert emp.annual_salary == 67000'''

# Using fixture to create an Employee instance
@pytest.fixture
def emp():
    return Employee('Jane', 'Smith', 80000)
def test_give_raise(emp):
    emp.give_raise()
    assert emp.annual_salary == 85000
def test_give_custom_raise_with_fixture(emp):
    emp.give_custom_raise(10000)
    assert emp.annual_salary == 90000
    