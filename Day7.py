## ---------------- Task 1: Use super() properly ------------------


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


## ------------ Task 2: Apply Abstraction ---------------

from abc import ABC, abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

# update classes:

class Student(User, AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User, AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"


class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"Temp Faculty: {self.name}, Salary: {self.salary}, Duration: {self.duration}"
    
## ------------ Task 3: Sorting using key ----------------

# create data FIRST
students = [Student("Araind", 1, "CSE", 60000),
    Student("Akshaya", 2, "ECE", 40000),
    Student("Vijay", 3, "IT", 80000)]
faculty_list = [  Faculty("Raj", 101, 35000),
    Faculty("Sumi", 102, 28000),
    TempFaculty("Ananya", 103, 30000, "6 months")]

students.sort(key=lambda x: x.fees)
faculty_list.sort(key=lambda x: x.salary)

## ------------- Task 4: Use map() --------------

names = list(map(lambda s: s.name, students))

## -------------- Task 5: Use filter() --------------

high_fee_students = list(filter(lambda s: int(s.fees) > 50000, students))
high_salary_faculty = list(filter(lambda f: int(f.salary) > 30000, faculty_list))

## ------------- Task 6: Use reduce() ---------------

from functools import reduce

total_fees = reduce(lambda acc, s: acc + int(s.fees), students, 0)
total_salary = reduce(lambda acc, f: acc + int(f.salary), faculty_list, 0)

## ------------- Task 7: Higher Order Function ---------------

def process_users(users, func):
    return list(map(func, users))

## ---------- Final Mini System (Complete Implementation) -----------------

from abc import ABC, abstractmethod
from functools import reduce

# Abstract Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Base Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Student Class
class Student(User, AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, Dept: {self.dept}, Fees: {self.fees}"


# Faculty Class
class Faculty(User, AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, Salary: {self.salary}"


# Temp Faculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"Temp Faculty: {self.name}, Salary: {self.salary}, Duration: {self.duration}"


# Sample Data
students = [
    Student("Aravind", 1, "CSE", 60000),
    Student("Akshaya", 2, "ECE", 40000),
    Student("Vijay", 3, "IT", 80000)
]

faculty_list = [
    Faculty("Raj", 101, 35000),
    Faculty("Sumi", 102, 28000),
    TempFaculty("Ananya", 103, 30000, "6 months")
]


# Print Details
print("\n--- All Details ---")
for s in students:
    print(s.get_details())

for f in faculty_list:
    print(f.get_details())


# Sorting
students.sort(key=lambda x: x.fees)
faculty_list.sort(key=lambda x: x.salary)


# Map
names = list(map(lambda s: s.name, students))
print("\nStudent Names:", names)


# Filter
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))


print("\nHigh Fee Students:")
for s in high_fee_students:
    print(s.get_details())

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.get_details())


# Reduce
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)


# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


result = process_users(students, lambda s: s.name.upper())
print("\nProcessed Names:", result)