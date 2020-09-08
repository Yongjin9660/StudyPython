# Dictionary
# Key : Value
cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)     # True
print(5 in cabinet)     # False

cabinet2 = {"A-3":"유재석", "B-100":"박명수"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 추가
print(cabinet2)
cabinet2["C-20"] = "조세호"
print(cabinet2)

# 삭제
del cabinet2["A-3"]
print(cabinet2)

# Key 출력
print(cabinet2.keys())

# value 출력
print(cabinet2.values())

# key-value 쌍으로 출력
print(cabinet2.items())

# 모두 삭제
cabinet2.clear()
print(cabinet2)