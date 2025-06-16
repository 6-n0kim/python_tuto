from words import hangman_words


hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),}

# for line in hangman_art[6]:
#     print(line)

# 한글 입력 체크 함수

# 행맨 그리기 함수
def display_hangman(wrong_guesses):
    print("*************")
    print(wrong_guesses)
    for line in hangman_art[wrong_guesses]:
        print(line)

    print("*************")

# 행맨 힌트 출력 함수

# 정답 출력 함수

# 메인 함수
def main():
    is_run = True
    wrong_guesses = 0
    answer = "dog"
    guess_letters = set()
    
    while is_run:
        display_hangman(wrong_guesses)

        guess = input("문자를 입력하세요 : ").lower()

        guess_letters.add(guess)

    if guess in answer:
      for i in range(len(answer)):
        if answer[i] == guess:
          print(answer[i], end="")
    else:
      wrong_guesses += 1

# 프로그램 시작
if __name__ == "__main__":
    main()