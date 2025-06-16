# 파이썬에서는 주로 for in문을 사용
my_list = ["a" , "b", "c", "d" , "e", "f" , "g"]

for x in my_list:
    if x == "c":
        # break - 조건에 맞으면 중단
        # continue - 조건에 맞는 부분을 건너뜀
        pass
    # print(x)

# range() : 숫자의 범위 생성 
for k in range(10):
    # print(k)
    pass

for y in range(3,10,2):
    # print(y)
    pass
# 구구단
for i in range(2,10):
    print(f"-----------{i}단-----------")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    pass
