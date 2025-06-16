# 합수는 def 키워드를 사용한다

def my_func(na, age):
    print("age is {1}, {0} hello".format(na,age))

# my_func("jun" , 20) # 호이스팅이 되지않는다
# my_func(na = "jun" , age = 20) # 키워드 파라미터

# arbitary arguments : 튜플로 여러 파라미터를 한번에 받는다

def arb_func(na, age, w):
    print("age is {1}, {0} hello {2}".format(na,age , w))

# arb_func("jun" , 20, "world")

# keyword arguments : 딕셔너리로 여러 파라미터를 한번에 받는다

def key_arb_func(**kwargs):
    print(kwargs)

key_arb_func(name = "hym" , age = 20 , city = "incheon")

# 콜렉션 파라미터
def coll_func(aaa):
    for x in aaa:
        print(x)

# coll_func(["korea" , "japan", "china"])
# coll_func(("korea" , "japan", "china"))

