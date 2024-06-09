x,d = map(int,input().split())
q = int(input())
x, d, k = map(int, input().split())

a = [x] * (k + 1)

for i in range(2, k + 1):
    a[i] = a[i - 1] + d

print(a[k])


x,d = map(int,input().split())
q = int(input())


for i in range(q):
    k = int(input())
    a = [x] * (k + 1)
    for j in range(2, k + 1):
        a[j] = a[j - 1] + d
    print(a[k])
    print(k)