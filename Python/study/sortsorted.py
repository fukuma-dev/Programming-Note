"""
What's the difference in sort() and sorted()

sort()はBuilt-in methods (組み込みメソッド)
sorted()はBuilt-in function (組み込み関数)
"""

x = [30, 40, 10, 20]

sortedx = sorted(x)
print(sortedx) # [10, 20, 30, 40]
print(x) # [30, 40, 10, 20]

x.sort()
print(x) # [10, 20, 30, 40]
