"""
최단 거리를 구하기 위해 다익스트라 사용
"""
import heapq
# import sys
# sys.stdin = open('input.txt')


def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])  # 최소힙은 배열의 첫 번째 값을 기준으로 배열을 정렬.
    distance = [float('inf')] * (N+1) # DP에 활용할 memoization 테이블 생성
    distance[start] = 0  # 자기 자신으로 가는 사이클은 없으므로.

    while heap:
        node, weight = heapq.heappop(heap)

        if weight > distance[node]:  # 비용 최적화 전부터 큰 비용일 경우 고려할 필요 없음.
            continue

        for n, w in graph[node]:  # 최소 비용을 가진 노드를 그리디하게 방문한 경우 연결된 간선 모두 확인
            total = weight + w
            if distance[n] > total:  # 여러 경로를 방문해 합쳐진 가중치 W가 더 비용이 적다면
                distance[n] = total  # 업데이트
                heapq.heappush(heap, (n, total))  # 최소 비용을 가진 노드와 합쳐진 가중치 추가

    return distance


T = int(input())
for tc in range(1, T+1):
    # N: 마지막 지점, E: 도로 개수
    N, E = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(E)]
    graph = [[] for _ in range(N+1)]

    # s: 시작, e: 끝, w: 거리
    for s, e, w in roads:
        graph[s].append((e, w))

    result = dijkstra(0)
    print(f"#{tc} {result[-1]}")
