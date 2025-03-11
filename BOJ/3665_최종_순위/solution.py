"""
최종 순위 - 골드 1 (https://www.acmicpc.net/problem/3665)
선행 관계를 따지는 것이므로 위상정렬로 접근해 봄.
-> 위상정렬로 접근했다가 그냥 우선순위를 바꾸는 식으로 함.

------------------------------------------
작년 순위: 1 5 3 2 4
바뀐 쌍: [4 3]
------------------------------------------
단순하게 2개의 위치를 바꾸면 1 5 4 2 3가 되는데 이에 경우 바뀐 쌍으로 [4 2] [2 3] 도 주어져야만 함.
따라서, "2와 4 사이의 모든 숫자"에 대해 바뀐 값을 제공 받아야 함.
즉, 정상적인 데이터를 제공 받는다면!
주어지는 숫자의 를 +1, -1만 해주면 알아서 순서가 바뀐다.

------------------------------------------
작년 순위: 1 5 3 2 4
바뀐 쌍: [4 3] [4 2] [2 3]
------------------------------------------
정상적으로 받은 데이터이다. 바뀐 쌍에 주어지는 숫자를 A B라고 하자.
A의 우선순위 +1 B의 우선순위 -1를 하면 순위가 아래 과정을 통해 정상적으로 바뀐다.

우선순위 리스트: [1, 4, 3, 5, 2]
바뀐 쌍 / 우선순위 리스트 / 설명
[4 3] / [1, 4, 4, 4, 2] / 4의 우선순위 -1, 3의 우선순위 +1
[4 2] / [1, 5, 4, 3, 2] / 4의 우선순위 -1, 2의 우선순위 +1
[2 3] / [1, 4, 5, 3, 2] / 2의 우선순위 -1, 3의 우선순위 +1

우선순위만 사용해도 그래프 생성 가능
graph[indegree[i]].append(i)
"""
from collections import deque
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 팀의 수
    N = int(input())
    last_rank = list(map(int, input().split()))   # 작년 순위
    # M: 상대적인 등수가 바뀐 쌍의 수
    M = int(input())
    changed = [list(map(int, input().split())) for _ in range(M)]

    last_indegree = [0 for _ in range(N+1)]
    # 작년 기준 우선순위
    for i in range(N-1):
        now = last_rank[i]
        nxt = last_rank[i+1]

        last_indegree[now] += 1
        last_indegree[nxt] = last_indegree[now]
    last_indegree[nxt] += 1

    indegree = last_indegree[:]
    # 올해 우선순위로 바꾸기
    for c1, c2 in changed:
        if last_indegree[c1] > last_indegree[c2]:
            indegree[c1] -= 1
            indegree[c2] += 1
        elif last_indegree[c1] < last_indegree[c2]:
            indegree[c1] += 1
            indegree[c2] -= 1

    this_rank = [[] for _ in range(N+1)]
    # 우선순위 순서대로 그래프 만들기
    for i in range(1, N+1):
        if indegree[i] > N+1 or 1 > indegree[i]:
            print("IMPOSSIBLE")
            break

        this_rank[indegree[i]].append(i)

    # 정상적인 그래프라면 모든 위치에서 한 개씩 연결됨.
    if [] not in this_rank[1:]:
        for i in range(1, N+1):
            print(this_rank[i][0], end=' ')
        print()
    # 그렇지 않다면 순위 알아낼 수 없음.
    else:
        print("IMPOSSIBLE")
