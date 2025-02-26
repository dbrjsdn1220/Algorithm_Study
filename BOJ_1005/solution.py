import sys
sys.stdin = open('input.txt', 'r')

"""
목표 건물부터 부모를 찾아 계속 올라가면서 더하는 방식은 시간초과
-> 같은 건물을 중복으로 확인하기 때문이다
이를 해결하려면, 첫 건물부터 순서대로 건물 건설 최대 시간을 저장
DP로 문제를 해결해서 중복 검사를 줄여야 함
"""

def dp():
    for i in range(1, N+1):
        


T = int(input())
for tc in range(1, T+1):
    # N: 건물 개수, K: 규칙 개수
    # D: 건물 건설 시간
    # XY: 건설 규칙
    # W: 이기기 위해 지어야 할 건물
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for i in range(K)]
    W = int(input())

    prior = [[] for _ in range(N + 1)]   # 필요한 선행 건물 저장
    max_time = [[0] for _ in range(N + 1)]
    answer = 0   # 이기는데 걸린 총 시간

    # 선행 건물 저장
    for X, Y in XY:
        prior[Y].append(X)

    print(prior)
    # dp()
    print(answer)
