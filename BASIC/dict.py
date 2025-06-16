# 자료형: 리스트[], 튜플(), 딕셔너리{key : value}, 셋트{}

# 3. 딕셔너리
# 중복 허용 x
# 변경 가능
# 키와 값이 쌍으로 구성

a = {
    "name" : "homegogo",
    "age" : 20,
    "address" : "Ilsan",
    # "address": "Seoul", # 중복키가 있을경우 마지막 키값만 적용
    "gu" : ["bupyeung","namgu" , "jungu"]
}

# print(a)
# print(type(a))

# 길이
# print(len(a))

# 요소의 접근
# print(a["name"])

# 생성자로 생성
b = dict(name="ho" , age = 30)
# print(b)

# 키 값으로 접근(get)
# print(a.get("age"))

# 키 값만 출력
# print(a.keys())

# 요소의 변경
a["age"] = 30
a.update({'name' : "jaen"})
# print(a)

# 요소의 추가
a["color"] = ['red', "green" , "blue"]
a.update({'number' : [1,2,3]})
# print(a)

# 요소의 제거
# a.pop("age")

d = {
    "name" : "homegogo",
    "age" : 20,
    "address" : "Ilsan",
    # "address": "Seoul", # 중복키가 있을경우 마지막 키값만 적용
    "gu" : ["bupyeung","namgu" , "jungu"]
}

# keys 를 출력
for x in d.keys():
    # print(x)
    pass

for x in d.values():
    # print(x)
    pass

# print(d.items())

for k , v in d.items():
    print(k , v)
    print(type(k) , type(v)) # 반복문으로 추출된 데이터는 원시 타입을 갖는다.
    pass

# 딕셔너리 내부의 딕셔너리

famliy = {
    "first" : {
        "a" : "hoem",
        "b" : "jane",
    }
    ,
    "second" : {
        "c" : "qld",
        "d" : "kan"
    }
}