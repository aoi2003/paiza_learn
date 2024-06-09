n,a,b = map(int,input().split())

data = [0] * (n+1)
data[0] = 1

for i in range(n+1):
  if i >= a:
    data[i] += data[i - a]
  if i >= b:
    data[i] += data[i - b]

print(data[n])

