from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date

print (date.today())

if __name__ == '__main__':
  calculate_salary()
  get_employees()
