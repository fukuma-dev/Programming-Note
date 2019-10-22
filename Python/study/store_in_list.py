"""
Store integer in List
"""

List = list(map(int, input().split()))
print(List)

# or
List = [int(i) for i in input().split()]
print(List)
