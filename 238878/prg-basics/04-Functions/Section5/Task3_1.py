###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import Task3 as t3

# Reads employee's data from keyboard
first_name = t3.input_string('Enter first name: ')
last_name = t3.input_string('Enter last name: ')
age = t3.input_integer('Enter age: ')
salary = t3.input_real('Input salary: ')
is_salary_hidden = t3.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name: ', first_name, " ", last_name)
print('Age: ', age)
print('Salary hidden: ', is_salary_hidden)
if not is_salary_hidden:
    print('Salary: ', salary)