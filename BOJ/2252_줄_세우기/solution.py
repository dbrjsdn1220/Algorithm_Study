"""
줄 세우기 - 골드 3 (https://www.acmicpc.net/problem/2252)
꼭 완벽한 키 순서대로 서지 않아도 됨. 특정 학생 앞에 특정 학생이 서야한다는 것만 지켜지면 됨.
-> 답이 여러개일 수 있음.

A < B 형태로 주어지니까 B 학생의 차수를 +1,
우선순위 0을 출력하면서 해당 학생 뒤에 서는 학생의 차수 -1
(위상정렬)

처음에는 0 not in indegree해서 계속 indegree을 순회해서 느렸음. (1,796ms)
-> 그냥 학생 수만큼 출력하면 멈추게 바꿈. (1,500ms)
-> deque 넣고 차수가 0인 애들만 처리해서 계속 반복 확인하지 않도록 함. (244ms)
"""
from collections import deque
import sys
input = sys.stdin.readline


# N, M: 학생 수, 비교 수
N, M = map(int, input().split())
compare = [list(map(int, input().split())) for _ in range(M)]

indegree = [-1] + [0 for _ in range(N)]   # 차수
graph = [[] for _ in range(N+1)]   # 그래프

# 차수, 그래프 연산
for short, tall in compare:
    indegree[tall] += 1
    graph[short].append(tall)

# 차수가 0인 애들 저장
que = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        que.append(i)

# 차수가 0인 애들 출력
while que:
    student = que.popleft()
    print(student, end=' ')

    # 현재 학생 뒤에 서는 학생들 차수 -1, 0이 되면 que에 추가
    for i in graph[student]:
        indegree[i] -= 1
        if indegree[i] == 0:
            que.append(i)
