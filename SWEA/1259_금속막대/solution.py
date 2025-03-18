"""
금속막대 - D5(https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18NaZqIt8CFAZN)
그리디로 하면 될 거 같은디?
그냥 막대 하나씩 비교하면서 앞에 연결되는지 뒤에 연결되는지 확인하고 연결
"""
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 막대 개수
    N = int(input())
    sticks = list(map(int, input().split()))
    sticks = [sticks[i:i+2] for i in range(0, N*2, 2)]
    sticks.sort(key=lambda x: -x[1])

    # 금속 막대 연결
    connected = [sticks.pop()]
    while sticks:
        check = False

        # 모든 금속 막대
        for i in range(len(sticks)-1, -1, -1):
            if sticks[i][0] == connected[-1][-1]:
                connected[-1] = connected[-1] + sticks.pop(i)
                check = True
            elif sticks[i][1] == connected[-1][0]:
                connected[-1] = sticks.pop(i) + connected[-1]
                check = True

        # 연결되지 못하는 완전 독립된 막대라면 새로 추가
        if check is False:
            connected.append(sticks.pop())

    # 연결된 막대 길이 순 정렬
    connected.sort(key=len)
    answer = connected[-1]   # 가장 긴 거

    print(f"#{tc}", end=' ')
    for i in answer:
        print(i, end=' ')
    print()
