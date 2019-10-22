# https://atcoder.jp/contests/abc044/tasks/abc044_a

N, K, X, Y = (int(input()) for i in [0] * 4)

print(X * K + Y * (N - K) if N > K else X * N)

# or

print(N * X - (X - Y) * max(N - K, 0))
