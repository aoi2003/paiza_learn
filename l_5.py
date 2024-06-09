n = map(int,input().split())
data = list(map(int,input().split()))
q = input()
data2 = list(map(int,input().split()))

for i in data2:
  print(data[i-1])