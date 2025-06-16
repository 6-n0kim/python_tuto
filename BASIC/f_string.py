# f 키워드를 사용한 문자열 포멧팅

# + 키워드
a = 'junyoung'
b = 'jane'
print(a+ "은 " + b + "의 친구입니다.")

# % 키워드
print("%s은 %s의 친구입니다" %(a,b))

# f-string
print(f"{a}은 {b}의 친구입니다")
print(fr"{a}은 {b}의 친구입니다") # r: raw string

# 문자열 조작
z = "junyoung"
print(f"{z.upper()}")
print(f"{z[:5]}")
