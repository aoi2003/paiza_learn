
x,d_1,d_2,k = map(int,input().split())



for i in range(k):
    a = [x] * (k + 1)
    for j in range(2, k + 1):
        if j % 2 == 0:
          a[j] = a[j - 1] + d_2
        else:
          a[j] = a[j - 1] + d_1
          
    
print(a[j])