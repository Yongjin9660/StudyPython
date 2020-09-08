s = '나는 소년'
print(s)

s2 = "큰 따옴표"
print(s2)

s3 = """
나는 소년이고,
파이썬은 쉽다.
"""
print(s3)

# Function
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])     # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])    # 처음부터 6 직전까지
print("뒤 7 자리 : " + jumin[7:]) # 7 부터 끝까지 

print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])

ex = "Python is Amazing"
print(ex.lower())           # 소문자로
print(ex.upper())           # 대문자로
print(ex[0].isupper())
print(len(ex))
print(ex.replace("Python", "Java"))

index = ex.index("n")
print("First Index : "+ str(index))

index = ex.index("n", index + 1)
print("Second Index : " + str(index))

print(ex.find("Java"))

print("Count : " + str(ex.count("n")))

# String Format
# 방법 1
print()
print("나는 %d 살입니다." %20)
print("나는 %s을 좋아합니다." %"파이썬")
print("Apple은 %c로 시작합니다." %"A")

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))

#방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

#방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아합니다.")

########
print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\Yongjin\\PythonWorkspace")

# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한글자삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# 생성된 비밀번호 : nav51!

url = "http://naver.com"
url = url.replace("http://", "")        # 규칙 1
index = url.find(".com")
url = url[:index]
print(url)
print(url[:3] + str(len(url)) + str(url.count("e")) + "!")