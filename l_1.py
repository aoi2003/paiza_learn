h,w = map(int,input().split())
y,x = map(int,input().split())
grid = []

move_x = [1,0,-1,0]
move_y = [0,1,0,-1]


for i in range(h):
  data = ['.'] * w
  grid.append(data)

grid[y][x] = '*'

for i in range(4):
  new_x = x + move_x[i]
  new_y = y + move_y[i]
  if w > new_x >= 0 and h > new_y >= 0:
    grid[new_y][new_x] = '*'

for i in range(h):
    print(''.join(grid[i]))