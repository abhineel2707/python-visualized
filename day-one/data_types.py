import sys

married = False
print("married", married, type(married), sys.getsizeof(married))

salary = 1_00_000.00
print("salary", salary, type(salary), sys.getsizeof(salary))

complex_data = 2 + 3j
print("complex", complex_data, type(complex_data), sys.getsizeof(complex_data))

void = None
print("void", void, type(void), sys.getsizeof(void))

age = 111111111111111111111.11
print("int_data", age, type(age), sys.getsizeof(age))

name = "Abhineel"
print("name", name, type(name), sys.getsizeof(name))
