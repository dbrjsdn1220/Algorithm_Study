"""
DP로 접근, 타일의 종류가 길이 1에서는 1종류, 2는 2종류, 3은 1종류
-> 1: 2X1 타일 세로로 1개
-> 2: 2X1 타일 가로로 2개, 2X2 타일 1개
-> 3: 2X3 타일 1개

그렇다면 우리는 어떻게 접근해야할까.
이미 만들어진 조합에서 타일의 종류를 모두 넣으면 새로운 조합이 됨.
예를 들어, 길이 8의 타일이라면
-> 길이 7타일의 모든 조합에 길이 1인 타일의 종류를 넣으면 됨.
-> 길이 6타일의 모든 조합에 길이 2인 타일의 종류를 넣으면 됨.
-> 길이 5타일의 모든 조합에 길이 3인 타일의 종류를 넣으면 되.
-> 길이가 4인 종류의 타일은 없으므로 끝
"""
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # N: 타일 크기
    N = int(input())

    answer = [None, 1, 3, 6]
    for i in range(4, N+1):
        answer.append(answer[i-1] + answer[i-2]*2 + answer[i-3])

    print(f"#{tc} {answer[N]}")

