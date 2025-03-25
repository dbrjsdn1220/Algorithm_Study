"""
뱀과 사다리 게임 - 골드 5(https://www.acmicpc.net/problem/16928)
사다라랑 뱀 정보를 dict에 저장하고, 1-6 칸 움직였을 때 가장 멀리가는 값으로 이동
-> 생각해보니 탈 수 있는 사다리 뒤에 도착지까지 바로 가는 사다리가 있다면, 그걸 타야함.
-> 너무 오래걸려서 최소 횟수 저장해서 가지치기 해야할 듯
"""
import sys
sys.stdin = open('input.txt')


def game_start(player, count):
    stack = [(player, count)]

    while stack:
        cnt_player, cnt_count = stack.pop()

        if cnt_player >= 100:
            minmap[100] = min(minmap[100], cnt_count)
            continue

        for i in range(1, 7):
            moveto = cnt_player + i if cnt_player + i <= 100 else 100

            if ladders.get(moveto):
                moveto = ladders.get(moveto)
            elif snakes.get(moveto):
                moveto = snakes.get(moveto)

            if minmap[moveto] > cnt_count+1:
                minmap[moveto] = cnt_count+1
                stack.append((moveto, cnt_count+1))


# N, M: 사다리의 수, 뱀의 수
N, M = map(int, input().split())

ladders = {k: v for k, v in [map(int, input().split()) for _ in range(N)]}
snakes = {k: v for k, v in [map(int, input().split()) for _ in range(M)]}

minmap = [100] * 101   # 최소 횟수 저장
game_start(1, 0)

print(minmap[100])