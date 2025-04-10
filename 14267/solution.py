'''
회사 문화 1 - 골드 4(https://www.acmicpc.net/problem/14267)
위에서부터 아래로 내리칭찬하는 문제임.
직속상사가 무조건 자기보다 무조건 번호가 낮으므로, 그냥 0번 인덱스부터 한 번만 순회하면 됨..
처음에 이 조건을 못 봐서 어렵게 하다가 계속 틀림 ㅠㅠ
'''
# import sys
# sys.stdin = open('input.txt')


N, M = map(int, input().split())   # N, M: 직원 수, 칭찬 횟수
seniors = list(map(int, input().split()))   # 직속 상사 정보
compliments = [list(map(int, input().split())) for _ in range(M)]   # 칭찬 정보

# 칭찬 정보 저장
answer = [0 for _ in range(N)]
for i, w in compliments:
    answer[i-1] += w

# 내리칭찬 시작 (사장 상사는 없으므로 1번 인덱스부터 시작)
for i in range(1, N):
    senior = seniors[i] - 1
    answer[i] += answer[senior]

# 정답 출력
for c in answer:
    print(c, end=' ')