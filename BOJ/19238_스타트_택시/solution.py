from collections import deque
# import sys
# sys.stdin = open('input.txt')

"""
가장 가까운 승객을 태우러 가야하므로, 택시와 승객의 거리를 구해야 함.

시간 초과로 실패 ㅠㅠ
시간 초과를 해결하기 위해 DFS -> BFS
visited를 순회하면서 확인이 아니라 True False로 확인 가능하게 바꿈
승객 정보 접근할 때 딕셔너리로 해서 조금이라도 빠르게
승객 하나씩 최단거리를 재는게 아니라 한 번에 모든 승객하도록
난 거리가 같은 경우 먼저 입력된 승객을 태우는 줄 알았는데 그게 아니라 행, 열 기준으로 태우는 거라 틀렸음.
승객을 태우고 난 뒤에도 못 가는 경우가 있는데, 이를 고려 못했었음. 수정완.
"""

# 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def get_distance(start, destination):
    # 택시 위치에서 모든 승객까지의 최단 거리를 구하는 BFS
    queue = deque([(start[0], start[1], 0)])   # (y, x, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    min_distance = N ** 2

    while queue:
        y, x, d = queue.popleft()

        # 최소 거리보다 멀리 있는 승객은 탐색할 필요 없음
        if d > min_distance:
            break

        # 도착지가 없다면 -> 승객 위치 구하기
        if not destination:
            # 현재 위치가 승객의 출발지라면 후보에 추가
            if (y, x) in passenger:
                targets.append([y, x, d])
                min_distance = d
                continue  # 같은 거리의 다른 승객을 더 찾기 위해 탐색 지속

        # 도착지가 있는 경우 -> 승객 목적기 거리 구하기
        else:
            if (y, x) == destination:
                return d

        # 이동 가능하면 BFS 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and A[ny][nx] != 1:
                visited[ny][nx] = True
                queue.append((ny, nx, d + 1))


# N: 활동 영역의 크기, M: 승객 수, F(fuel): 초기 연료량
N, M, F = map(int, input().split())
# A(area): 활동 영역 정보
A = [list(map(int, input().split())) for _ in range(N)]
# T(taxi): 택시 위치
T = list(int(i) - 1 for i in input().split())
# P(passenger): 승객 정보
# 그런데 인덱스 값을 맞추기 위해 -1 해주기
P = [list(int(i) - 1 for i in input().split()) for _ in range(M)]


passenger = {}
for i in range(M):
    sy, sx, ey, ex = P[i]
    A[sy][sx] = 2
    passenger[(sy, sx)] = (i, ey, ex)   # i: 우선순위 겸 인덱스

# 승객 태우러 가자~
for _ in range(M):
    targets = []
    get_distance(T, [])
    targets.sort(key=lambda x: (x[0], x[1]))  # 행, 열 순으로 정렬

    # 승객만큼 반복 전에 태울 승객이 없다면
    if not targets:
        F = -1
        break

    target_y, target_x, target_d = targets[0]
    value = passenger.get((target_y, target_x))

    if target_d <= F:
        F -= target_d
        T = [target_y, target_x]
        passenger.pop((target_y, target_x))

        target_d = get_distance(T, (value[1], value[2]))
        if target_d is not None:
            if target_d <= F:
                F += target_d
                T = [value[1], value[2]]
                continue
    F = -1
    break

print(F)
