Lists = [1,2,3,4,5]
print(Lists) # [1, 2, 3, 4, 5]

for List in Lists:
    print(List)
"""
1
2
3
4
5
"""

print(*Lists) # 1 2 3 4 5

for i in range(len(Lists)):
    print(Lists[i])
"""
1
2
3
4
5
"""
