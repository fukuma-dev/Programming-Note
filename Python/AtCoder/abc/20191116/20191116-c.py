# pi = 8450**0.5
# print('{:.10f}'.format(pi))
import itertools

Row = int(input())
X = []
Y = []
SUM = []
NX = []
NY = []

for i in range(Row):
  x, y = input().split()
  X.append(int(x))
  Y.append(int(y))

per = list(itertools.permutations(range(Row)))
print(per)

for p in per:
  print('start')
  for num in p:
    print(num)
    NX = X[num]
    NY = Y[num]

      # SUMX = (int(X[i]) - int(X[i+1]))**2
      # SUMY = (int(Y[i]) - int(Y[i+1]))**2
      # SUM.append((SUMX + SUMY)**0.5)
  # SUM.append(((int(X[i]) - int(X[i+1]))**2 + (int(Y[i]) - int(Y[i+1]))**2)**0.5)

# print(NX, NY)
