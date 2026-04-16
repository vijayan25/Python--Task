import mysql.connector
from functools import reduce

# DB CONNECTION
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="expense_db"
    )

class User:
    def __init__(self, name):
        self.__name = name  # encapsulation

    def save(self):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (self.__name,))
        db.commit()
        print("✅ User added successfully!")


class Expense(User):   
    def __init__(self, user_id, amount, category, description, date):
        super().__init__("temp")
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = date

    def save(self):
        db = connect_db()
        cursor = db.cursor()
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(query, (
            self.__user_id,
            self.__amount,
            self.__category,
            self.__description,
            self.__date
        ))
        db.commit()
        print("💸 Expense added successfully!")


def add_user():
    name = input("Enter user name: ")
    user = User(name)
    user.save()


def add_expense():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\n👤 Users:")
    for u in users:
        print(u)

    user_id = int(input("\nEnter user ID: "))
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")
    date = input("Date (YYYY-MM-DD): ")

    exp = Expense(user_id, amount, category, description, date)
    exp.save()


def view_expenses():
    db = connect_db()
    cursor = db.cursor()

    query = """
    SELECT users.name, expenses.amount, expenses.category, expenses.date
    FROM expenses
    JOIN users ON users.user_id = expenses.user_id
    """

    cursor.execute(query)

    print("\n📊 All Expenses:")
    for row in cursor.fetchall():
        print(row)


def filter_expenses():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT category, amount, date FROM expenses")
    data = cursor.fetchall()

    choice = input("Filter by category: ")

    filtered = [row for row in data if row[0] == choice]

    print("\n🔍 Filter Result:")
    for f in filtered:
        print(f)


def total_expense():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT amount FROM expenses")
    data = cursor.fetchall()

    amounts = list(map(lambda x: x[0], data))

    total = reduce(lambda a, b: a + b, amounts, 0)

    print("\n💰 Total Expense:", total)


def category_wise():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT category, amount FROM expenses")
    data = cursor.fetchall()

    result = {}

    for c, a in data:
        result[c] = result.get(c, 0) + a

    print("\n📊 Category-wise Spending:")
    for k, v in result.items():
        print(k, ":", v)


def highest_expense():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT amount FROM expenses")
    data = cursor.fetchall()

    amounts = [x[0] for x in data]

    highest = reduce(lambda a, b: a if a > b else b, amounts)

    print("\n🔥 Highest Expense:", highest)


def monthly_report():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT date, amount FROM expenses")
    data = cursor.fetchall()

    report = {}

    for d, a in data:
        month = str(d)[:7]
        report[month] = report.get(month, 0) + a

    print("\n📅 Monthly Report:")
    for m, v in report.items():
        print(m, ":", v)


def smart_insight():
    db = connect_db()
    cursor = db.cursor()

    cursor.execute("SELECT category, amount FROM expenses")
    data = cursor.fetchall()

    result = {}

    for c, a in data:
        result[c] = result.get(c, 0) + a

    max_cat = max(result, key=result.get)

    print("\n🧠 Smart Insight:")
    print("You are spending too much on", max_cat)


while True:
    print("\n===== MENU =====")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Filter Expenses")
    print("5. Total Expense")
    print("6. Category-wise Spending")
    print("7. Highest Expense")
    print("8. Monthly Report")
    print("9. Smart Insight")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_user()
    elif choice == 2:
        add_expense()
    elif choice == 3:
        view_expenses()
    elif choice == 4:
        filter_expenses()
    elif choice == 5:
        total_expense()
    elif choice == 6:
        category_wise()
    elif choice == 7:
        highest_expense()
    elif choice == 8:
        monthly_report()
    elif choice == 9:
        smart_insight()
    elif choice == 0:
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice")