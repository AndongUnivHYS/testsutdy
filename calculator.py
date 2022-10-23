#사칙연산 계산기 만들기


def main():
    #사칙연산에 사용할 두 수
    a = 0
    b = 0

    


    while True:
        a = int(input("a의 숫자를 지정해주세요."))
        b = int(input("b의 숫자를 지정해주세요."))
        operation = input("사칙연산을 선택하세요. (1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈)")
    
        if operation == '0':
            print("덧셈 시작합니다.")
            print(a+b)

        elif operation == '1':
            print("뺄셈 시작합니다.")
            print(a-b)

        elif operation == "2":
            print("곱셈 시작합니다.")
            print(a*b)

        else:
            print("나눗셈 시작합니다.")
            print(a/b)
        

if __name__ == "__main__":
    main()
