"""
로봇 청소기 - 골드 5(https://www.acmicpc.net/problem/14503)
1. 4방향이 청소되어 있으면 후진 -> 벽 만나면 청소 종료
2. 막히지 않았다면 반시계로 90도 회전 후 이동
-> 뒤로 이동할 때 머리방향 돌려서 틀렸었음 ㅠ
"""
import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())   # 방 크기(세로, 가로)
cleaner = tuple(map(int, input().split()))   # 로봇 청소기 위치, 방향
map_info = [list(map(int, input().split())) for _ in range(N)]   # 방 정보(0: 미청소, 1: 벽, 2: 청소)
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 위, 오, 아, 왼

map_info[cleaner[0]][cleaner[1]] = 2
stack = [cleaner]
count = 1

while stack:
    y, x, d = stack.pop()

    # 반시계로 회전하며 이동 시도
    for i in range(1, 5):
        nd = (d - i + 4) % 4
        ny, nx = y + direction[nd][0], x + direction[nd][1]

        if map_info[ny][nx] == 0:
            map_info[ny][nx] = 2
            stack.append((ny, nx, nd))
            count += 1
            break

    # 어느 방향으로도 이동하지 못한 경우 (뒤로 이동)
    if not stack:
        nd = (d + 2) % 4
        ny, nx = y + direction[nd][0], x + direction[nd][1]

        if map_info[ny][nx] == 2:   # 벽이 아니라면
            stack.append((ny, nx, d))

print(count)