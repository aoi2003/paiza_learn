x,d_1,d_2 = map(int,input().split())
q = int(input())

for i in range(q):
  k = int(input())
  for j in range(2,k):
    a = [x] * (k + 1)
    if j % 2 == 0:
      a[j] = a[j - 1] + d_2
    else:
      a[j] = a[j - 1] + d_1
  print(a[j])