"""
https://www.acmicpc.net/problem/1005
목표 건물부터 부모를 찾아 계속 올라가면서 더하고 비교하는 방식은 시간초과로 실패
-> 같은 건물을 중복으로 계속 확인하기 때문이다

이를 해결하려면, 첫 건물부터 순서대로 건물 건설 최대 시간을 저장
DP로 문제를 해결해서 중복 검사를 줄여야 함.
앞에서부터 지을 수 있는 건물의 건설 소요 시간을 저장하고,
이를 이용해 다음 건물의 건설 소요 시간을 저장함.

건설된 건물을 확인하는 finished 리스트가 있었는데, 그냥 build_time 하나로만 줄임.
-> 메모리 줄이려고 했는데, 실제로는 0.3%만 줄어들음 ㅋㅋ
-> 실행속도는 매번 달라지겠지만 실행속도 10% 줄어들음. 왜일까?
-> finished를 True로 추가적으로 바꿀 필요 없이 build_time만 바꾸면 되니까, 연산 횟수가 1번 줄어서 그런 듯.
"""
import sys
sys.stdin = open('input.txt', 'r')


def build_dp():
    # 초기 건물 짓기
    init = [i for i in range(1, N+1) if not prior[i]]
    for i in init:
        build_time[i] = D[i]

    # W번 건물이 지어질 때까지 다른 건물 짓기
    while build_time[W] == -1:
        # 건물 순회
        for i in range(1, N+1):
            # 이미 지은 건물은 확인 X
            if build_time[i] != -1:
                continue

            check = True   # 해당 건물을 지을 수 있는지 확인
            time = 0   # 해당 건물 건설 총 시간 저장
            for j in prior[i]:
                # 못 짓는 경우
                if build_time[j] == -1:
                    check = False
                    break
                # 필요로 하는 건물 시간 + 현재 건물 시간 더해서 최고 값 저장
                time = max(build_time[j] + D[i], time)

            # 지을 수 있다면 저장
            if check:
                build_time[i] = time


T = int(input())
for tc in range(1, T+1):
    # N: 건물 개수, K: 규칙 개수
    # D: 건물 건설 시간
    # XY: 건설 규칙
    # W: 이기기 위해 지어야 할 건물
    N, K = map(int, input().split())
    D = [None] + list(map(int, input().split()))
    XY = [list(map(int, input().split())) for i in range(K)]
    W = int(input())

    prior = [[] for _ in range(N + 1)]   # 필요한 선행 건물 저장
    # build_time: 건물 별 총 소요 시간 for DP
    build_time = [-1 for _ in range(N + 1)]   # -1이면 아직 지어지지 않은 건물임.

    # 선행 건물 저장
    for X, Y in XY:
        prior[Y].append(X)

    # dp로 건물 건설 소요시간 구하기
    build_dp()

    print(build_time[W])
