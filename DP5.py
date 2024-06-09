k = int(input())
a_1 = 1
a_2 = 1
data = [a_1] * (k +1)

for i in range(3,k):
  data[i] = data[i - 1] + data[i - 2]

print(data[k])


