# compound interest calculator : Compound interest calculator는 원금(principal)과 이자가 누적되어 이자에 이자가 붙는 방식으로 계산되는 복리(Compound Interest)를 계산하는 도구입니다. 복리 계산은 다음과 같은 수식을 사용합니다:


# [ A = P * (1 + r / n)^t ]


# ( A )는 최종 금액 (원금 + 이자)
# ( P )는 초기 원금 (Principal)
# ( r )는 연이율 (Annual interest rate, 소수로 표현)
# ( n )는 연간 복리 계산 횟수 (Compounding frequency per year): 100분율 이므로 100
# ( t )는 시간 (연 단위, Time in years)


# 변수 초기화
principal = 0 # 초기 원금
rate = 0 # 연이율
time = 0 # 시간

# 원금 입력
while True: # 무한 루프
    principal = input("초기 원금을 입력해주세요 : ")


# AttributeError
    # 숫자 입력 여부 파악
    try:
        principal = float(principal) # 숫자로 변환 - 숫자형 문자만 변환됨
    except ValueError: # 숫자형 문자가 아닌 경우
        print(f"{principal}은 숫자가 아닙니다. 숫자를 입력해 주세요.")
        continue # principal 입력 받기로 돌아감

    # 원금이 0보다 큰지 확인
    if principal <= 0:
        print("원금은 0보다 커야합니다.")
    else:
        break

# 연이율 입력
while True:
    rate = input("연이율을 입력해주세요 : ")

    try:
        rate = float(rate) / 100 # 백분율 변환
    except ValueError: # 숫자형 문자가 아닌 경우
        print(f"{rate}은 숫자가 아닙니다. 숫자를 입력해 주세요.")
        continue

    if rate <= 0:
        print("연이율은 0보다 커야합니다.")
    else:
        break

# 기간 입력
while True:
    time = input("기간을 입력해주세요 : ")

    try:
        time = float(time)
    except ValueError: # 숫자형 문자가 아닌 경우
        print(f"{time}은 숫자가 아닙니다. 숫자를 입력해 주세요.")
        continue

    if time <= 0:
        print("기간은 0보다 커야합니다.")
    else:
        break

print(f"원금 : {principal}")
print(f"연이율 : {rate}")
print(f"기간 : {time}")

total = principal * ((1 + rate) ** time)

print(total)

