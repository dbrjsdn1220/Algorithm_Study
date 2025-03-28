"""
루미의 28번째 생일 - 골드 2(https://www.acmicpc.net/problem/33667)
윤년 구해서 그냥 하면 되는 거 아닌가? 왜 골드2나 되는거지?
"""
import sys
sys.stdin = open('input.txt')


def check_leap_year(year):
    if year % 4 == 0 and year % 400 != 100 or year % 400 != 200 or year % 400 != 300:
        return True
    else:
        return False


def change_as_unit(time, to_unit):
    compare = 86400   # 1일을 초로 환산
    if to_unit == 'Month':
        if time[1] == 2:   # 2월인데 윤년 아니면 28일, 이면 29일
            compare = 2419200 if leap_year is False else 2505600
        else:   # 4, 6, 9 ,11월이면 30일, 아니면(2월 제외) 31일
            compare = 2592000 if time[1] in [4, 6, 9, 11] else 2678400

    elif to_unit == 'Year':   # 윤년 아니면 365일, 이면 366일
        compare = 31536000 if leap_year is False else 31622400

    day = 0 if to_unit == 'Day' else time[2] - 1
    if to_unit == 'Year':
        for i in range(1, 12):
            if i == time[1]:
                break
            elif time[1] == 2:   # 2월인데 윤년 아니면 28일, 이면 29일
                day += 28 if leap_year is False else 29
            else:   # 4, 6, 9 ,11월이면 30일, 아니면(2월 제외) 31일
                day += 30 if time[1] in [4, 6, 9, 11] else 31

    seconds = time[5] + ((time[4]-1) * 60) + ((time[3]-1) * 3600)
    seconds += (time[2]-1) * 86400

    return seconds / compare


T = int(input())
for tc in range(1, T+1):
    birth_time = list(map(int, input().split()))
    now_time = list(map(int, input().split()))
    unit = input()

