import sys
sys.stdin = open('input.txt')

"""
가장 가까운 승객을 태우러 가야하므로, 택시와 승객의 거리 구하기.
"""


def shortest_path(y, x, destination, count):
    global distance

    if [y, x] == destination:
        distance = passenger_distance[-1],


T = 1
for tc in range(1, T+1):
    # N: 활동 영역의 크기, M: 승객 수, F(fuel): 초기 연료량
    N, M, F = map(int, input().split())
    # A(area): 활동 영역
    A = [list(map(int, input().split())) for _ in range(N)]
    # S(start): 택시 시작 위치
    S = list(map(int, input().split()))
    # P(passenger): 승객 정보
    P = [list(map(int, input().split())) for _ in range(M)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    distance = N**2

    while P:
        # 승객 거리 저장할 거임.
        passenger_distance = []
        for p in P:
            # 승객의 위치 넣어서 최단거리 구하기
            shortest_path(*S, p[0:2], 0)
