# 잔액보기 : 함수
# 1번 입력시 : 잔액을 출력한다.


# 입금함수 : 함수
# 2번 입력시 : 입금할 금액 입력을 받는다.
# 입금할 금액이 0보다 작거나 문자일 경우 예외처리를 한다.


# 출금함수 : 함수
# 3번 입력시 : 출금할 금액 입력을 받는다.
# 출금할 금액이 0보다 작거나 문자일 경우 예외처리를 한다.
# 출금할 금액이 잔액보다 클 경우 예외처리를 한다.


# 종료: 함수
# 4번 입력시 : 프로그램을 종료한다.

# 잔액확인 함수
def show_balance(balance):
    print(f"현재 잔액은 {balance}원 입니다.")

# 입금 함수
def deposit():
    while True:
        amount = input("입금할 금액을 입력해주세요")

        try:
            amount = int(amount)
        except ValueError:
            print("숫자를 입력해주세요")
            continue

        if amount <= 0 :
            print("0보다 큰 수를 입력해 주세요")
            return 0
        else:
            return amount
        
    

# 출금 함수
def withdraw(balance):
    while True:
        amount = input("출금할 금액을 입력해주세요")

        try:
            amount = int(amount)
        except ValueError:
            print("숫자를 입력해주세요")
            continue

        if amount > balance :
            print("잔액이 부족합니다")
            return 0
        else:
            return amount
    


def main():
    is_run = True
    balance = 0
    while is_run:
        print("1. 잔액보기")
        print("2. 입금하기")
        print("3. 출금하기")
        print("4. 종료")

        choice = input("원하는 작업을 1 ~ 4 중에 선택해 주세요")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":            
            balance -= withdraw(balance)
        elif choice == "4":
            is_run = False
            print("프로그램을 종료합니다")
        else:
            print("1~4번중 골라주세요")
            continue

if __name__ == "__main__": # 프로그램이 시작될 때 처음으로 실행되는 영역
    main()