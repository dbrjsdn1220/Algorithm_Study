"""
단어 수학 - 골드 4(https://www.acmicpc.net/problem/1339)
가장 큰 단위와 개수를 고려해서 그리디하게 풀면 될 듯?
처음에는 알파벳 별로 개수를 세고 정렬하고 10000의 자리에 알파벳 개수 같으면 전체 개수랑 비교하고(생략) 별 짓 다했는데,
그냥 자리별로 숫자 세서 우선순위 높이고 거기 맞게 숫자 부여하면 되는 거였음 ㅠ
"""
import sys
sys.stdin = open('input.txt')


# N: 단어의 개수
N = int(input())
# 단어 입력 받고 길이 순으로 정렬 & 단어 배열 뒤집기(pop 할거임)
words = [list(input()) for _ in range(N)]
[words[i].reverse() for i in range(N)]

alphabet_prior = dict()   # 알파벳 우선순위 저장

# 알파벳이 해당 자리수에 등장하면 해당 자리수 값 + 1
# 예를 들어 AAB, ACD가 있다면 A는 100의 자리 2번, 10의 자리 1번이다.
# 따라서 key 'A'는 210이 된다. 이걸로 어떤 숫자가 높은 숫자를 가져야하는지 알 수 있다.
for word in words:
    multiplicand = 10

    for i in range(len(word)):
        if alphabet_prior.get(word[i]) is None:
            alphabet_prior[word[i]] = multiplicand ** i
        else:
            alphabet_prior[word[i]] += multiplicand ** i

# value(우선순위) 내림차순 기준으로 key(알파벳) 정렬
sorted_prior = dict(sorted(alphabet_prior.items(), key=lambda x: -x[1]))

# 알파벳에 숫자 할당
number = 9
alphabet_num = dict()
for char in sorted_prior.keys():
    alphabet_num[char] = number
    number -= 1

# 더하자
answer = 0
for word in words:
    multiplicand = 1
    for char in word:
        answer += alphabet_num.get(char) * multiplicand
        multiplicand *= 10

print(answer)