"""
완탐을 시도하데, 이미 만들어진 안전한 영역은 넘어가도록
새로운 영역에 들어가면 +1 하고 인접한 영역을 True로 바꿔 막힐 때까지 DFS
-> 재귀호출 방식으로 하니까 RecursionError 뜸, 그래서 재귀호출 없애고 스택으로
-> 물에 잠기지 않는 경우 비의 양 = 0이지만 처음에는 1부터 탐색해서 틀렸었음.
"""
# import sys
# sys.stdin = open('input.txt')


def expand_area(y, x, h):
    expanding = [(y, x)]

    while expanding:
        cy, cx = expanding.pop()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] is False and area[ny][nx] > h:
                expanding.append((ny, nx))
                visited[ny][nx] = True


N = int(input())   # 지역 크기
area = [list(map(int, input().split()))for _ in range(N)]   # 지역 높이 정보

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for height in range(0, 100):
    safe_area = 0   # 안전한 영역의 개수
    visited = [[False] * N for _ in range(N)]  # 안전한 지역 표시

    for i in range(N):
        for j in range(N):
            if visited[i][j] is False and area[i][j] > height:
                expand_area(i, j, height)
                safe_area += 1

    answer = max(answer, safe_area)

print(answer)