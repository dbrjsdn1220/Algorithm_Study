"""
단순하게 빈 공간에 3개의 기둥을 세울 수 있는 모든 수를 이용한다.
각 경우마다 bfs를 사용해 바이러스를 퍼트리고,
가지 칠 때는 바이러스 수를 저장해서 퍼진 바이러스가 가장 작은 경우만 적용.
-> 전체공간 - 바이러스 수 - 기둥 개수하면 정답이 나온다.
"""
from collections import deque
import sys
sys.stdin = open('input.txt')


def infection(cnt_map):
    global virus
    que = deque(virus_pos)
    visited = [[False] * M for _ in range(N)]
    count = 0   # 지금까지 나온 바이러스 개수

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while que:
        y, x = que.popleft()
        count += 1

        # 현재 퍼진 바이러스가 지금까지 최소로 퍼진 바이러스 수보다 많다면 종료
        if count >= virus:
            return

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 방문한 적 없고 빈 공간이 경우만 진행
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] is False and cnt_map[ny][nx] == 0:
                visited[ny][nx] = True
                cnt_map[ny][nx] = 2
                que.append((ny, nx))

    virus = min(virus, count)


def build_wall():
    count_pos = len(empty_pos)

    for i in range(count_pos):
        for j in range(i+1, count_pos):
            for k in range(j+1, count_pos):
                # 벽 세운 뒤 맵
                built_map = [map[i][:] for i in range(N)]
                built_map[empty_pos[i][0]][empty_pos[i][1]] = 1
                built_map[empty_pos[j][0]][empty_pos[j][1]] = 1
                built_map[empty_pos[k][0]][empty_pos[k][1]] = 1

                infection(built_map)   # 바이러스 퍼지기 시작


# N, M: 지도 크기(세로, 가로)
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

# 바이러스와 빈 칸의 초기 위치들 저장
virus_pos = [(i, j) for i in range(N) for j in range(M) if map[i][j] == 2]
empty_pos = [(i, j) for i in range(N) for j in range(M) if map[i][j] == 0]
# 벽의 개수 구하기 (세울 벽 +3)
wall_count = sum([1 for i in range(N) for j in range(M) if map[i][j] == 1]) + 3

virus = float('inf')
build_wall()

print(N*M - virus - wall_count)
