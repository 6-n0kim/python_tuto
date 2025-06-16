# 자료형: 리스트[], 튜플(), 딕셔너리{key : value}, 셋트{}

# 2. tuple
# 값을 변경할 수 없다.
# 중복데이터를 허용한다
# 순서를 가지고있다
# 데이터는 괄호를 사용한다.
# 모든 타입을 요소로 지정할 수 있다

a =("사과" , "복숭아" , "사과" , 1 ,True)
b =("apple")
c ="grape" , "banana"

# print(a[0])
# print(b)
# print(c)

# a[0] = "포도" 요소 변경시 오류

# print(type(a))
# print(type(b))
# print(type(c))

# 튜플 길이
# print(len(a))

# 생성자로 튜플 생성
b = tuple(("사과" , "배", "딸기"))

# 튜플 슬라이싱
# print(a[1:3])

# 반복문 읽기
for x in a:
    # print(x)
    pass

# if 문으로 존재 여부 확인
if "사과" in a:
    # print(True)
    pass

# 요소의 변경
b = list(a)
b[0] = "포도"

c = tuple(b)
# print(c)

# 요소의 추가
b.append("라임")
c = tuple(b)
print(c)

# 튜플 자체에 요소 추가
a += ("라임" , "레몬")
print(a)

# 구조분해 할당
(a1,a2,a3,a4,a5,a6,a7) = a
# print(a5)

# 요소의 범위
# print(range(len(a)))

for i in range(len(a)):
    print(a[i])
    pass

# 튜플 복사하여 붙이기
print(a * 2)