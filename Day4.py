employees = []
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)
    print("Employee added successfully!")

def display_employees():
    for emp in employees:
        print(emp)

def delete_employee():
    name = input("Enter employee name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)
            print("Employee deleted!")

add_employee()
display_employees()

# Mini Project 2: Student Report Card

def report_card():
    name = input("Enter student name: ")
    
    a = int(input("Subject 1 : "))
    b = int(input("Subject 2 : "))
    c = int(input("Subject 3 : "))

    total = a + b + c
    avg = total / 3

    print("\n------ REPORT CARD ------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", avg)
    if avg >= 91:
        grade = "A+"
    elif avg >= 81:
        grade = "A"    
    elif avg >= 71:
        grade = "B+"
    elif avg >= 61:
        grade = "B"
    elif avg >= 51:    
        grade = "C"
    else:
        grade = "Fail"

    print("Grade:", grade)

report_card()

# Mini Project 3: Shopping Cart System

cart = []

def add_product():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    cart.append({"name": name, "price": price, "quantity": quantity})

def show_cart():
    total = 0
    for item in cart:
        cost = item["price"] * item["quantity"]
        total += cost
        print(item["name"], item["quantity"], cost)

    print("Total Bill:", total)

add_product()
add_product()
add_product()
show_cart()

# Mini Project 4: Login & User Validation

users = {
    "vijay": "vijay@2580",
    "pistolraj": "Raj@1707"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Login")

# Mini Project 5: Unique Visitor Counter

visitors = set()

for i in range(5):
    name = input("Enter visitor name: ")
    visitors.add(name)

print("Unique Visitors:", visitors)
print("Total Unique Visitors:", len(visitors))

# Mini Project 6: String Formatter Tool

name = input("Enter name: ")
product = input("Enter product: ")

print(f"{name} purchased {product}")

print(name.ljust(20))
print(name.rjust(20))
print(name.center(20))

# Mini Project 7: Bank Account System

account = {"name": "vijay", "balance": 1000}

def deposit(amount):
    account["balance"] += amount

def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
    else:
        print("Insufficient balance")

def check_balance():
    print("Balance:", account["balance"])

deposit(500)
withdraw(200)
check_balance()

# Mini Project 8: Voting System

votes = {
    "vijay": 0,
    "Sathish": 0,
    "rifa": 0
}

for i in range(5):
    vote = input("Vote for candidate: ")
    if vote in votes:
        votes[vote] += 1

print(votes)

winner = max(votes, key=votes.get)
print("Winner:", winner)

# Mini Project 9: Course Enrollment System

students = {}

name = input("Student name: ")
courses = input("Enter courses (comma separated): ").split(",")

students[name] = courses

print("Student Details")
print(students)

# Mini Project 10: Number Utility Tool

num = int(input("Enter number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hex:", hex(num))

print("With commas:", format(num, ","))
print("Scientific:", format(num, ".2e"))