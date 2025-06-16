# 문자열 조작을 위해 만들어진 메서드
# isalpha() : 문자열이 모두 알파벳인지 확인
a = 'abc'
b = "ABC"
c = "a b c"
d = "abc123"

# print(a.isalpha()) T
# print(b.isalpha()) T
# print(c.isalpha()) F
# print(d.isalpha()) F

# isnumeric() : 문자열이 모두 숫자인지 확인
e = 123
f = "123"
g = "12 3"

# print(e.isnumeric()) 인트형은 에러 발생
# print(f.isnumeric()) T
# print(g.isnumeric()) F

# isalnum() : 문자열이 숫자 또는 알파벳인지 확인
h = "123"
i = "abc"
j = "123abc"
k = "123 abc"

# print(h.isalnum()) T
# print(i.isalnum()) T
# print(j.isalnum()) T
# print(k.isalnum()) F

# join() : 문자열을 연결하여 새로운 문자열 반환
my_list = ["aa-bb-cc" , "dd-ee-ff" , "gg-hh-ii"]
rs = "/".join(my_list) 
# print(rs) aa-bb-cc/dd-ee-ff/gg-hh-ii

my_tuple= ('aa','bb','cc')
rs_tup = "-".join(my_tuple)
# print(rs_tup) aa-bb-cc

# startswith() / endswith() : 문자열이 특정 문자로 시작/ 마지막 하는지 확인
m = "Hello, it's me"
m1 = m.startswith("H")
# print(m1) T
m2 = m.endswith("me")
# print(m2) T