# 문자열 조작을 위해 만들어진 메서드
# isalpha() : 문자열이 모두 알파벳인지 확인
a = 'abc'
b = "ABC"
c = "a b c"
d = "abc123"

# print(a.isalpha())
# print(b.isalpha())
# print(c.isalpha())
# print(d.isalpha())

# isnumeric() : 문자열이 모두 숫자인지 확인
e = 123
f = "123"
g = "12 3"

# print(e.isnumeric()) 인트형은 에러 발생
print(f.isnumeric())
print(g.isnumeric())