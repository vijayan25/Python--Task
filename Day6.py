## ----------- Task 1: Encapsulation (User Class) --------------

class User:
    def __init__(self):
        self.__user_name = None   # private
        self.__pwd = None         # private

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name   # hide password

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)


# Testing
u = User()
u.set_user("john", "1234")
u.register()
u.login()

## -------------- Task 2: Inheritance (User → Student, Faculty) ------------

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):   # multilevel
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Testing
s = Student()
s.register()       # parent method
s.login()
s.student_greet()  # child method

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()

## ---------- Task 3: Method Overriding --------------

class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):   # override
        print("Welcome Student")


class Faculty(User):
    def greet(self):   # override
        print("Welcome Faculty")


# Testing
s = Student()
f = Faculty()

s.greet()
f.greet()

## --------------- Task 4: Method Chaining --------------

class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Testing
user = User()
user.login().greet().register()

## --------------- Task 5: Combined Real-Time Mini System ------------

class User:
    users_count = 0   # class variable

    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1

    def login(self):
        print(f"{self.__name} logged in")
        return self

    def register(self):
        print(f"{self.__name} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class Student(User):
    def greet(self):   # overriding
        print("Welcome Student")
        return self


class Faculty(User):
    def greet(self):   # overriding
        print("Welcome Faculty")
        return self


# Testing
s1 = Student("Vijay", "258")
f1 = Faculty("Sandy", "135")

s1.login().greet().register()
f1.login().greet().register()

print("Total users:", User.users_count)