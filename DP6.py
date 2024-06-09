a_1 = 1
q = int(input())


for i in range(q):
  k = int(input())
  data = [a_1] * (k +1)    
  for j in range(3,k+1):
    data[j] = data[j - 1] + data[j - 2]
  print(data[k])


