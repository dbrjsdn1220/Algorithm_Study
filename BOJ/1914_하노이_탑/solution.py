import sys
sys.stdin = open('input.txt', 'r')


def hanoi_tower(n, start, end, left):
    # n이 1이면 바로 이동
    if n == 1:
        print(start, end)
        return
    hanoi_tower(n - 1, start, left, end)
    print(start, end)
    hanoi_tower(n - 1, left, end, start)

# N: 원판의 개수
N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi_tower(N, 1, 3, 2)