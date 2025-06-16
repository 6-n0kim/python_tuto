# 자료형: 리스트[], 튜플(), 딕셔너리{key : value}, 셋트{}

# 4. 셋트
# 인덱스로 접근할 수 없다.
# 내부 요소를 수정할 수 없다
# 중복된 요소를 포함할 수 없다 - 중복 요소가 있을 경우 오류가 나지는 않지만 데이터 표현이 되지 않는다
# 중괄호 사용

a = {"apple" , "banana", 'cherry' , True , False}
# print(a) 인덱스가 없고 순서사 바뀜
# print(a)

# True = 1, False = 0, 1 과 True가 중복되어 True 표시
b = {True,1,2,3}
# print(b)

# 길이
# print(len(a))

# 생성자
c = set(("apple" , "banana" , "cherry"))
# print(c)

for x in c:
    print(x)
    pass

# 요소의 추가
a.add("casd")

# 여러 요소를 합침
e = {"mango" , "grape" ,"apple"}
a.remove("apple") # 없는 요소 삭제시 오류
a.discard("grape") # 없는 요소 삭제시 오류 X
a.pop()

# 두 개의 셋트를 하나의 변수에 담는다
f = {"apple" , "banana"}
g = {"apple" , "banana"}

h= f.union(g)

# 셋트 비우기
f.clear()

# 차집합으로 합침
i = f.difference(g)

# 교집합
j  = f.intersection(g)

# 교집합 여부 확인
print(f.isdisjoint(g)) # 교집합이 있으면 False, 없으면 True

if a > 0:
    pass
elif a < 0:
    pass
