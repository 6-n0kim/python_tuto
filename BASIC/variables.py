# 변수는 키워드 없이 사용
# 파이썬은 세미콜론 마침표를 사용하지 않는다.

# x = 10
# print(x)
# print(type(x)) # 타입확인


# y = "jy"
# print(y)
# print(type(y))

# type casting : 타입의 명시적 변환
# a = "3" #String
# b = int(a) #int

# print(b)
# print(type(b))

# print(str(3))
# print(int(3))
# print(float(3))


# # 변수 이름 규칙
# # 1. 숫자로 시작하는 이름 사용 불가
# # 2. 특수문자는 _만 사용 가능
# # 3. 예약어 사용 불가: if, function, for, while, ....
# # 4. 대소문자 구분
# # 5. 중복 단어 연결은 언더바(스네이크 케이스): my_name

# 변수를 여러개 선언
name, age, adr = "juny" , 20, "seoul"
# print(name,age,adr)

# List 구조분해 할당
fruits = ['apple' , 'banana' , 'orange']
a,b,c= fruits
# print(a,b,c)
# print(fruits)

# 변수의 연결
# print("name : " + name + ", age : " + str(age))

# 함수로 문자열 읽기
def my_function():
    x = "jy"
    print("my name is : " + x + " my age is : " +str(age))

my_function()

