import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 작업 신청서 개수
    N = int(input())
    # SE: [시작 시간, 종료 시간]
    SE = [list(map(int, input().split())) for _ in range(N)]
    SE.sort(key=lambda x: x[1])

    end = 0
    answer = 0
    for s, e in SE:
        if s >= end:
            answer += 1
            end = e

    print(f"#{tc} {answer}")


