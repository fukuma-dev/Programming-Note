n = int(input())
s = input()
if n%2 != 0:
  print('No')
else:
  if s[:int(n/2)] == s[int(n/2):]:
    print('Yes')
  else:
    print('No')
