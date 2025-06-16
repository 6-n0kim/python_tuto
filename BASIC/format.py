# 문자열 포매팅
age = 20
message = "제 이름은 준영이고, 나이는 {}살 입니다."
a = message.format(age)
# print(a)

full_text = "저는 {name}이고, 나이는 {age}살 입니다."
b = full_text.format(name = "준영" , age = 20)
# print(b)

# 자리수 지정 포매팅
# 변수 앞으로 5자리까지 확보하는 정렬
c = "저는 {:>5}마리의 강아지를 키우고 있습니다."
print(c.format(5))
print(c.format(50))
print(c.format(500))
print(c.format(5000))
print(c.format(50000))

# 천단위 콤마 표시
q = "저는 {:,}원을 주식으로 날렸습니다"
print(q.format(1000000000))
