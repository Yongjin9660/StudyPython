print("Python", "Java", "JavaScript", sep =" vs ")

print("Python", "Java", "JavaScript", sep =",", end="?")
print(" 같은 줄에 출력")

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(3), str(score).rjust(4), sep=":")

# 은행 대기표
# 001, 002, 003, ...
print()
for num in range(1, 6):
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")     # 문자열 형태로
# print("입력하신 값은 "+ answer + "입니다.")


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일  땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000))
print("{0:+,}".format(-100000000))

# 3자리마다 콤마찍기, 부호 붙이기, 자릿수 확보
# 빈자리는 ^ 로 채우기
print("{0:^<+30,}".format(100000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시(소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))