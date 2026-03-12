#Task 1
print("Hello World",end=" ")
print("Welcome Python")
print("laptop","Mouse","Keyboard",sep="|")

#Task2
name="vijay"
age="24"
location="Villupuram"
print(name,age,location," - ")

#Task3-Multiline assingment
name,age,location="vijay","25","villupuram"
print("multiline assingment:-",name,age,location)

#Task4 Indexing
word="Hogwards"
print(word[0],word[2],word[7])

#Task5 Arithmetic operator
print(25 + 10)
print(50 - 20)
print(8 * 5)
print(100 / 10)
print(10 % 3)
print(2 ** 4)
print(20 // 3)
 
#Task6 BODMAS
print(3+2*5**2)

#Task7 Assingment operator
num=50
num+=25
print(num)
num=100
num/=10
print(num)

#task8 Comparision Operator
print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)


#Task9 String comparission
a="calm"
b="Calm"
print(a==b)

#Task 10  Logical Operators
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))

#Task11 Membership Operator
numbers = [10,20,30,40,50]
print(20 in numbers,60 in numbers,30 not in numbers)

#Task 12  Swap Variables
a = 10
b = 20
a,b=b,a
print(a,b)

#Task 13 Bitwise XOR
a = 6
b = 3
print(a^b)
