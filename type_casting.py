# String
x = "hello"
print(type(x))

print("-------------------------")

y = 10
print(type(y))

print("-------------------------")

z = 3.14
print(type(z))

print("-------------------------")

a = 5j
print(type(a)) # 복소수

# 집합 자료형 : list, tuple, dict
# list : 순서가 있는 데이터 집합 - 배열
b = [1,2,3,'apple',True]
print(b[3])
print(type(b))

# tuple : 순서가 있는 자료형
c = ('grape' , 'banana', 'apple')
print(c)
print(type(c))

# dic(딕셔너리) : 키와 값의 쌍으로 이뤄진 데이터 그룹 - 자바스크립트의 객체와 유사
d = {"name" : "jy " ,"age " :  20}
print(d['name'])
print(type(d))

# 개행 문자열
e = """파이썬은 1991년에 귀도 반 로섬에 의해 만들어진 인터프리터 프로그래밍 언어이다. 
직관적이고 쉬운 문법과 다양하고 풍부한 라이브러리들을 바탕으로 한 강력한 생태계를 가지고 있어
 프로그래밍 교육, 인공지능, 데이터 분석 및 빅데이터, 백엔드, 프론트엔드, 웹 스크래핑 등 다양한 분야에서 사용되며, 이에 힘입어 2024 TIOBE 인덱스 기준 프로그래밍 언어 순위 1위이기도 하다."""
print(e)

