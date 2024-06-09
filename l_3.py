from collections import deque

def bfs(H, W, start_y, start_x, N):
    """
    盤面上の特定の位置からN回以内に到達できるマスを求める関数
    """
    # キューを初期化し、スタート位置をキューに追加する
    q = deque([(start_y, start_x)])

    # 移動回数を管理するための配列 l を初期化する
    # 各マスへの最短移動回数を記録し、初期値は-1（未訪問）とする
    l = [[-1] * W for _ in range(H)]
    l[start_y][start_x] = 0

    # 盤面の状態を表す配列 mp を初期化する
    # 初期値は"."（未到達）とし、到達可能なマスを"*"で表す
    mp = [["."] * W for _ in range(H)]
    mp[start_y][start_x] = "*"

    # 移動方向を表す配列
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # キューが空になるまで探索を続ける
    while q:
        # キューから現在のマス（y, x）を取り出す
        y, x = q.popleft()

        # 現在のマスへの移動回数がN回以上の場合、探索を終了する
        if l[y][x] == N:
            continue

        # 現在のマスから上下左右の4方向に移動する
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # 移動先のマスが盤面の範囲内にあるかどうかを確認する
            if 0 <= ny < H and 0 <= nx < W:
                # 移動先のマスが未訪問の場合、探索を続ける
                if l[ny][nx] == -1:
                    # 移動先のマスへの移動回数を現在のマスの移動回数 + 1で更新する
                    l[ny][nx] = l[y][x] + 1
                    # 移動先のマスを"*"で表す
                    mp[ny][nx] = "*"
                    # 移動先のマスをキューに追加する
                    q.append((ny, nx))

    return mp

def print_board(board):
    """
    盤面の状態を出力する関数
    """
    for row in board:
        print("".join(row))

# 盤面のサイズ（H, W）、移動回数（N）、スタート位置（y, x）を入力から読み取る
H, W, N = map(int, input().split())
start_y, start_x = map(int, input().split())

# 幅優先探索を実行し、最終的な盤面の状態を取得する
final_board = bfs(H, W, start_y, start_x, N)

# 最終的な盤面の状態を出力する
print_board(final_board)