import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


t = int(sys.stdin.readline())
for _ in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    combi = [[] for _ in range(len(n)**2)]
    gcd_list = []
    # for i in range(1, len(n)-1):  n[1]부터 조합 만드려다가 실패
    #     for j in range(len(n)):
    #         combi.append([n[j], n[j+i]])
    # print(combi)
    # for i in range(len(combi)):
    #   gcd_list.append(gcd(combi[i]))
    # gcd_list=set(gcd_list)
    # print(gcd_list)
