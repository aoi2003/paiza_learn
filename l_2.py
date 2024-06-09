from collections import deque

# 盤面のサイズ（H, W）とスタート位置（y, x）を入力から読み取る
H, W = map(int, input().split())
y, x = map(int, input().split())

# キューを初期化し、スタート位置をキューに追加する
q = deque()
q.append((y, x))

# 移動回数を管理するための配列 l を初期化する
# 各マスへの最短移動回数を記録し、初期値は-1（未訪問）とする
l = [[-1] * W for _ in range(H)]
l[y][x] = 0

# 盤面の状態を表す配列 mp を初期化する
# 初期値は"."（未到達）とし、到達可能なマスを"*"で表す
mp = [["."] * W for _ in range(H)]
mp[y][x] = "*"

# キューが空になるまで探索を続ける
while q:
    # キューから現在のマス（ny, nx）を取り出す
    ny, nx = q.popleft()
    
    # 現在のマスへの移動回数が3回以上の場合、探索を終了する
    if l[ny][nx] == 3:
        continue
    
    # 現在のマスから上下左右の4方向に移動する
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        # 移動先のマスが盤面の範囲内にあるかどうかを確認する
        if 0 <= ny + dy < H and 0 <= nx + dx < W:
            # 移動先のマスが未訪問の場合、探索を続ける
            if l[ny + dy][nx + dx] == -1:
                # 移動先のマスへの移動回数を現在のマスの移動回数 + 1で更新する
                l[ny + dy][nx + dx] = l[ny][nx] + 1
                # 移動先のマスを"*"で表す
                mp[ny + dy][nx + dx] = "*"
                # 移動先のマスをキューに追加する
                q.append((ny + dy, nx + dx))

# 最終的な盤面の状態を出力する
for i in range(H):
    print(*mp[i], sep="")