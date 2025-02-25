import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start, targets):
    """택시 위치에서 모든 승객까지의 최단 거리를 구하는 BFS"""
    queue = deque([(*start, 0)])  # (y, x, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    candidates = []
    min_distance = float('inf')

    while queue:
        y, x, d = queue.popleft()

        # 최소 거리보다 멀리 있는 승객은 탐색할 필요 없음
        if d > min_distance:
            break

        # 현재 위치가 승객의 출발지라면 후보에 추가
        if (y, x) in targets:
            candidates.append((y, x, d))
            min_distance = d
            continue  # 같은 거리의 다른 승객을 더 찾기 위해 탐색 지속

        # 이동 가능하면 BFS 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and A[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx, d + 1))

    return sorted(candidates, key=lambda x: (x[0], x[1]))  # 행, 열 순으로 정렬


T = 1
for tc in range(1, T + 1):
    # 입력 처리
    N, M, F = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    taxi_y, taxi_x = map(lambda x: int(x) - 1, input().split())

    passengers = {}
    for _ in range(M):
        sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
        passengers[(sy, sx)] = (ey, ex)

    # 방향 벡터
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for _ in range(M):
        if not passengers:
            break

        # 현재 택시 위치에서 모든 승객까지의 거리 구하기
        closest_passengers = bfs((taxi_y, taxi_x), passengers.keys())

        # 태울 승객이 없는 경우 종료
        if not closest_passengers:
            F = -1
            break

        # 가장 가까운 승객 선택
        (sy, sx, dist) = closest_passengers[0]

        # 연료 부족하면 종료
        if dist > F:
            F = -1
            break

        # 연료 감소 및 택시 이동
        F -= dist
        taxi_y, taxi_x = sy, sx

        # 해당 승객의 목적지 찾기
        destination = passengers.pop((sy, sx))

        # 승객을 목적지까지 이동시키는 거리 구하기
        destination_distance = bfs((taxi_y, taxi_x), {destination})

        # 도착할 수 없는 경우 종료
        if not destination_distance:
            F = -1
            break

        # 목적지 이동 처리
        (ey, ex, dist) = destination_distance[0]
        if dist > F:
            F = -1
            break

        # 연료 충전 및 택시 이동
        F += dist
        taxi_y, taxi_x = ey, ex

    print(F)


"""
ChatGPT 최적화 코드는 시간초과 안해서 올려둠. 비교하면서 공부할 것.
import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start, targets):
    # 택시 위치에서 모든 승객까지의 최단 거리를 구하는 BFS
    queue = deque([(*start, 0)])  # (y, x, 이동 거리)
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    candidates = []
    min_distance = float('inf')

    while queue:
        y, x, d = queue.popleft()

        # 최소 거리보다 멀리 있는 승객은 탐색할 필요 없음
        if d > min_distance:
            break

        # 현재 위치가 승객의 출발지라면 후보에 추가
        if (y, x) in targets:
            candidates.append((y, x, d))
            min_distance = d
            continue  # 같은 거리의 다른 승객을 더 찾기 위해 탐색 지속

        # 이동 가능하면 BFS 탐색
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and A[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx, d + 1))

    return sorted(candidates, key=lambda x: (x[0], x[1]))  # 행, 열 순으로 정렬


T = 1
for tc in range(1, T + 1):
    # 입력 처리
    N, M, F = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    taxi_y, taxi_x = map(lambda x: int(x) - 1, input().split())

    passengers = {}
    for _ in range(M):
        sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
        passengers[(sy, sx)] = (ey, ex)

    # 방향 벡터
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for _ in range(M):
        if not passengers:
            break

        # 현재 택시 위치에서 모든 승객까지의 거리 구하기
        closest_passengers = bfs((taxi_y, taxi_x), passengers.keys())

        # 태울 승객이 없는 경우 종료
        if not closest_passengers:
            F = -1
            break

        # 가장 가까운 승객 선택
        (sy, sx, dist) = closest_passengers[0]

        # 연료 부족하면 종료
        if dist > F:
            F = -1
            break

        # 연료 감소 및 택시 이동
        F -= dist
        taxi_y, taxi_x = sy, sx

        # 해당 승객의 목적지 찾기
        destination = passengers.pop((sy, sx))

        # 승객을 목적지까지 이동시키는 거리 구하기
        destination_distance = bfs((taxi_y, taxi_x), {destination})

        # 도착할 수 없는 경우 종료
        if not destination_distance:
            F = -1
            break

        # 목적지 이동 처리
        (ey, ex, dist) = destination_distance[0]
        if dist > F:
            F = -1
            break

        # 연료 충전 및 택시 이동
        F += dist
        taxi_y, taxi_x = ey, ex

    print(F)

"""