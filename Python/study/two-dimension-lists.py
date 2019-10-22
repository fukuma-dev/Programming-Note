# 二次元リスト

Lists = [[1,2,3],[4,5,6]]
print(Lists) # [[1, 2, 3], [4, 5, 6]]

for List in Lists:
    print(List)
"""
[1, 2, 3]
[4, 5, 6]
"""

for Row in Lists:
    for Col in Row:
        print(Col)
"""
1
2
3
4
5
6
"""

for i in range(len(Lists)):
    for j in range(len(Lists[i])):
        print(Lists[i][j])
"""
1
2
3
4
5
6
"""
