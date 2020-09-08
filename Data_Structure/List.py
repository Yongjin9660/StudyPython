# List []
subway = [10, 20, 30]
print(subway)

subway=["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))

# 하하 씨가 다음 정류장에서 탐
subway.append("하하")
print(subway)

# 정형돈 씨가 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
num_list = [5,7,6,2,1,8,6,2]
num_list.sort()
print(num_list)

# 역정렬
num_list.reverse()
print(num_list)

# 다양한 자료형 함께 사용
max_list = ["조세호", 20, True]
print(max_list)

# 리스트 확장
num_list.extend(max_list)
print(num_list)
