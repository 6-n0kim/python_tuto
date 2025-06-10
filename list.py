# 자료형: 리스트[], 튜플(), 딕셔너리{key : value}, 셋트{}

# 1 list
a = ["사과", "배", "딸기", "포도","사과","포도", "체리" ,"수박"]
# print(a) 중복허용 ['사과', '배', '딸기', '포도', '사과', '포도', '체리', '수박']

# 슬라이싱
# print(a[:3])
# print(a[3:])
# print(a[-1])
# print(a[::2])

# 마지막 요소 추가
a.append("라임")
# print(a)

# 특정 위치에 요소 추가
a.insert(2, "라임")
# print(a)

# 파라미터에 지정된 요소 삭제
a.remove("라임")
# print(a) # 중복될 경우 앞에 있는 요소 하나만 삭제

# 마지막 요소만 삭제
a.pop()
# print(a)

# 리스트 비우기
a.clear()
# print(a)

b = ["사과", "배", "딸기", "포도","사과","포도", "체리" ,"수박"]

# 반복문으로 읽기
for x in b:
    # print(x)
    pass

b.sort()
# print(b)

# 역정렬
b.sort(reverse=True)
# print(b)

# 복사
c = b.copy() # list(b) 도 가능
c[0] = "라임"
# print(c)

# 리스트 합치기
d = ["list1" , "list2"]
e = b+d
print(e)