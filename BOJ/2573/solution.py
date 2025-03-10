"""
빙산 - 골드 4 (https://www.acmicpc.net/problem/2573)
빙산의 위치를 모두 구해서 리스트로 저장.
각 빙산 주변의 바다(0) 개수를 세고 저장. 저장된 값을 각 빙산에서 빼기(-) 연산.
0이 된 빙산이 있으면 해당 빙산 주변 4칸의 바다 수 +1
후에 남은 빙산 하나만 가져와 인접한 빙산의 개수 구하기 (DFS) // 개선 필요
인접한 빙산의 개수가 전체 빙산의 수보다 적으면 2개 이상이 되었다 판단.
"""
import sys
sys.stdin = open('input.txt')

# 방향 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# N, M: 세로, 가로
N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

# 빙산 좌표 구하기
iceberg_pos = [(i, j) for i in range(N) for j in range(M) if sea[i][j] > 0]


check = False   # 빙산이 1개라도 다 녹은 경우 True로 바꿔서 빙산 개수 셀거임.
year = 0

