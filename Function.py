def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 500)

commision, balance = withdraw_night(balance, 300)

print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commision, balance))

# 기본값
print()

# def proflie(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

# proflie("유재석", 20, "파이썬")

# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("김태호")

# 가변인자
print()

def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile2("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile2("김태호", 25, "Kotlin", "Swift")