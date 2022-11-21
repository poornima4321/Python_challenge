# Variables in Python
first_name = 'Poornima'
last_name = 'Santhan'
country = 'United Kingdom '
city = 'London'
age = 250
is_married = True
skills = ['MySql', 'Scala', 'Oracle', 'power BI', 'Python']
person_info = {'firstname': 'Poornims',
               'lastname': 'Santhan',
               'country': 'United Kingdom ',
               'city': 'London'
               }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Poornima', 'Santhan', 'London', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Checking Data types and Casting

# Different python data types
# Let's declare variables with various data types

first_name = 'Poornima'  # str
last_name = 'Santhan'  # str
country = 'United Kingdom'  # str
city = 'London'  # str
age = 250  # int, it is not my real age, don't worry about it

# Printing out types
print(type('Poornima'))  # str
print(type(first_name))  # str
print(type(10))  # int
print(type(3.14))  # float
print(type(1 + 1j))  # complex
print(type(True))  # bool
print(type([1, 2, 3, 4]))  # list
print(type({'name': 'Poornima', 'age': 250, 'is_married': 250}))  # dict
print(type((1, 2)))  # tuple
print(type(zip([1, 2], [3, 4])))  # set

# int to float
num_int = 10
print('num_int', num_int)  # 10
num_float = float(num_int)
print('num_float:', num_float)  # 10.0

# float to int
gravity = 9.81
print(int(gravity))  # 9

# int to str
num_int = 10
print(num_int)  # 10
num_str = str(num_int)
print(num_str)  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(float(num_str)))  # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Poornima'
print(first_name)  # 'Poornima'
first_name_to_list = list(first_name)
print(first_name_to_list)  # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

