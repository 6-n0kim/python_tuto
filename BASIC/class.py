# class class_name:
#     def __init__(self):

class myClass:
  x = 5

p1 = myClass() # instance of the class
# print(p1.x)

# 생성자 : 클래스 생성되는 객체의 초기화를 담당하는 함수
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)
print(p2.name)
print(p2.age)


# 클래스 기능의 확장

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  # def printname(self):
  #   print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    # super() : 부모 클래스의 생성자를 호출 
    super().__init__(fname, lname) # self를 제외한 부모 클래스의 생성자를 호출
    self.graduationyear = year

  def printname(self): # 부모 클래스의 메소드를 재정의
    print(self.firstname, self.lastname, self.graduationyear)

  def welcome(self):
    # print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    print("Welcome, {}, {}, to the class of, {}".format(self.firstname, self.lastname, self.graduationyear))

x = Student("Mike", "Olsen", 2021)
x.printname()
# print(x.graduationyear)
x.welcome()

