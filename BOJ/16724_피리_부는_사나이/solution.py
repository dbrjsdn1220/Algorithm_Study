"""
피리 부는 사나이 - 골드 3 (https://www.acmicpc.net/problem/16724)
피리 소리가 나면 특정 방향으로 계속 움직임.
모든 구역을 들어가서 DFS 쓰되, 한 번 들어가면 특정 방향을 따라 모두 visited에 저장.
그럼 다음부터는 이번에 방문한 곳이 아니라 이전에 방문한 곳을 만나면 안전구역이 필요없음.
이번에 방문한 곳을 다시 방문했다면, 다른 안전구역으로 연결되는 길이 없으므로 안전구역 +1

원래는 이번에만 방문한 곳인지 확인하기 위해 다른 visited를 만들어 계속 초기화 했는데 시간초과 남.
그래서 DFS로 들어갈 때마다 zone변수를 +1하고 zone을 visited에 저장해서 고유하게 만듬.
"""
import sys
sys.stdin = open('input.txt')


def move(y, x, num):
    while visited[y][x] == 0:
        visited[y][x] = num
        next_dir = direction.get(map_data[y][x])
        y, x = y + next_dir[0], x + next_dir[1]

    # 이번에만 방문했던 구역이라면
    if visited[y][x] == num:
        global safe_zone
        safe_zone += 1


# N, M: 행, 열
N, M = map(int, input().split())
map_data = [list(input()) for _ in range(N)]
direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1),
}
visited = [[0] * M for _ in range(N)]

safe_zone = 0
zone = 0   # 몇 번째 구역 진입인지 확인
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            zone += 1
            move(i, j, zone)

print(safe_zone)