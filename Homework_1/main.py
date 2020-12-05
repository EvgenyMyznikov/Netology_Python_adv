from Homework_1.application.db.people import get_employees
from Homework_1.application.salary import calculate_salary
from datetime import date

now = date.today()
if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(now)
