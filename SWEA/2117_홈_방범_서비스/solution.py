"""
해당 문제를 그리디로 풀려면 어떻게 해야 하나?
특정 위치가 최적의 해인지 구하는 것은 매우 복작하고 불가능에 가까워 보임.
또한, 특정 위치만 확인하는 것은 원하는 값을 도출하기 어렵다는 것을 의미하기도 함.
필자의 생각에는 (집 * 지불 금액)을 구해서 서비스 가능한 최대 영역을 설정하는 것이 중요해 보임.
제공할 수 있는 가장 큰 서비스 영역을 "최적의 해"라고 한다면,
제공 가능한 가장 큰 서비스 영역부터 낮은 영역까지 확인하며 완전 탐색하는 것은
그리디 알고리즘 방식의 일종이라 할 수 있는가?
-> 필자는 그렇다고 생각하므로 이 로직으로 알고리즘을 풀어보려 함.
-> 큰 범위부터 내려가면서 탐색하다 특정 범위에서 제공이 가능해진다면, 해당 범위에서 가장 많은 집을 제공해주는 부분이 정답.
"""
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 도시 크기, M: 하나의 집이 지불 가능한 금액
    N, M = map(int, input().split())
    # city: 도시 정보(1: 집)
    city = [list(map(int, input().split())) for _ in range(N)]
    # house_count: 도시에 있는 집의 개수
    total_house = sum([city[i].count(1) for i in range(N)])

    # 가능한 최대 영역의 크기 구하기 (K)
    K = 1
    while True:
        temp = K**2 + (K-1)**2
        if temp > total_house * M:
            K -= 1
            break
        K += 1

    # 서비스 가능한 집의 최대 개수 구하기
    # 만약 큰 범위에서 제공 가능한 경우가 나오면 해당
    answer = 0
    # 가능한 가장 큰 범위부터 시작
    for k in range(K, 0, -1):
        operate_fee = k**2 + (k-1)**2

        # i, j는 시작 좌표를 정하기 위함.
        for i in range(N):
            for j in range(N):
                house_count = 0
                y = 0

                # 서비스 영역에 집이 몇 개인지 확인
                for area in range(k-1, -1, -1):
                    # i에서 확인할 j 범위 선택
                    begin = j - area if j - area >= 0 else 0
                    finish = j + area if j + area < N else N-1
                    # 범위에 집 개수 새기
                    if y == 0:
                        house_count += city[i][begin:finish+1].count(1)
                    else:
                        if i-y >= 0:
                            house_count += city[i-y][begin:finish+1].count(1)
                        if i+y < N:
                            house_count += city[i+y][begin:finish+1].count(1)
                    y += 1

                if house_count * M >= operate_fee:
                    answer = max(house_count, answer)

        # 해당 서비스 영역 완탐 후, 결과가 나왔다면 종료
        if answer != 0:
            break

    print(f"#{tc} {answer}")
