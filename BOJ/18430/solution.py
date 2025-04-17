'''
무기 공학 - 골드 4(https://www.acmicpc.net/problem/18430)
제일 큰 크기가 5*5가 되므로 완전탐색해도 시간제한 충분함.

'''
import sys
sys.stdin = open('input.txt')


# 부메랑을 만들 수 있는지 없는지 확인
def available(y, x, parts):
    for part in parts:
        ny, nx = y + part[0], x + part[1]
        if not (0 <= ny < N and 0 <= nx < M and not visited[ny][nx]):
            return False
    return True


# dfs
def dfs(y, x, total):
    global answer

    if x == M:
        y += 1
        x = 0
    if y == N:
        answer = max(answer, total)
        return

    if not visited[y][x]:
        for boomerang in boomerangs:
            strength = 0
            if available(y, x, boomerang):
                strength += K[y][x] * 2
                visited[y][x] = True
                for part in boomerang:
                    ny, nx = y + part[0], x + part[1]
                    strength += K[ny][nx]
                    visited[ny][nx] = True

                dfs(y, x+1, total+strength)

                # 방문 처리 취소하고 다음 진행
                visited[y][x] = False
                for part in boomerang:
                    ny, nx = y + part[0], x + part[1]
                    visited[ny][nx] = False

    dfs(y, x+1, total)   # 선택 안하고 넘어가기



N, M = map(int, input().split())   # 세로, 가로 크기
K = [list(map(int, input().split())) for _ in range(N)]   # 강도 정보
visited = [[False] * M for _ in range(N)]   # 방문 정보

# 부메랑의 4가지 방향 (날개가 위치한 방향)
boomerangs = [
    ((0, -1), (1, 0)),      # 좌상 방향
    ((0, 1), (1, 0)),       # 우상 방향
    ((0, -1), (-1, 0)),     # 좌하 방향
    ((0, 1), (-1, 0))       # 우하 방향
]

answer = 0
dfs(0, 0, 0)

print(answer)