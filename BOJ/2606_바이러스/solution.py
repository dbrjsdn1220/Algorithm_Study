"""
단순하게 연결되어 네트워크를 무방향 그래프로 구성 (인접 리스트)
1번 정점과 연결된 컴퓨터를 찾기 위해 DFS
"""
import sys
sys.stdin = open('input.txt')


# idx와 연결되어 있는 정점 구하기
def dfs(idx):
    answer.append(idx)

    for i in graph[idx]:
        if i not in answer:
            dfs(i)


# N: 컴퓨터 수
# M: 연결된 컴퓨터 쌍의 수
# network: 연결된 컴퓨터 네트워크 정보
N = int(input())
M = int(input())
network = [list(map(int, input().split())) for _ in range(M)]

# 무방향 그래프 만들기
graph = [[None]] + [[] for _ in range(1, N+1)]
for conn in network:
    graph[conn[0]].append(conn[1])
    graph[conn[1]].append(conn[0])

answer = []
dfs(1)

print(len(answer)-1)
