# For loop

for i in range(1, 6):
    print("대기번호 : {0}".format(i))

s = ["a", "b", "c", "d"]

for i in s:
    print("{0}, 커피가 준비되었습니다.".format(i))

# While
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 처분되었습니다")


# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students_len = [len(i) for i in students]

print(students)
print(students_len)
