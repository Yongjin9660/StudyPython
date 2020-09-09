
# File_Open
#--------------------------------
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()


# File_Append
#--------------------------------
# score_file = open("./File/score.txt", "a", encoding = "utf8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()


# File Read
#--------------------------------
# score_file = open("./File/score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file.close()


#File Read OneLine 1
#--------------------------------
# score_file = open("./File/score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")

# score_file.close()


#File Read OneLine 2
#--------------------------------
score_file = open("./File/score.txt", "r", encoding = "utf8")
lines = score_file.readlines()      #list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()