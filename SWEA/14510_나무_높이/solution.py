"""
모든 나무에서 얼마나 더 자라야 하는지 구하자.
2의 경우 1+1로 대체가 가능함으로, 자라야 하는 길이가 홀수인 나무의 개수를 구함.
-> 그렇다면 개수만큼 홀수 일을 무조건 진행해야 함.

홀수 나무 개수를 구하고 빼주면, 모든 나무의 필요한 길이는 2의 배수가 됨.
앞에서 홀수인 나무 개수를 이미 연산했기 때문에 추가로 더 진행된 홀수 날만 연산해야 함.
-> 모든 나무 필요 길이 = 진행된 짝수 날 * 2 + 추가 진행된 홀수 날이 됨.
"""
# import sys
# sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    top_tree = max(trees)
    day = 0

    # 키워야 하는 나무 길이
    need_height = [top_tree - trees[i] for i in range(N) if top_tree != trees[i]]
    # need_height = need_odd + need_two 임
    need_odd = sum(need % 2 for need in need_height)
    need_two = sum(need // 2 for need in need_height)

    # 이미 다 자란 상태면
    if not need_height:
        print(f"#{tc} {0}")
        continue

    # 무조건 필요한 홀수 날에 맞게 day 연산
    if need_odd > 0:
        day += need_odd * 2 - 1

    while True:
        odd_day = (day+1) // 2
        even_day = day // 2

        if even_day + (odd_day - need_odd) // 2 >= need_two:
            break

        day += 1

    print(f"#{tc} {day}")