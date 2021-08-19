# 조건문 이용
import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]
    if order == "push":
        stack.append(word[1])
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            top = stack.pop()
            print(top)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# 함수 이용
# import sys


# def push(x):
#     stack.append(x)


# def pop():
#     if len(stack) == 0:
#         print(-1)
#     else:
#         top = stack.pop()
#         print(top)


# def size():
#     print(len(stack))


# def empty():
#     if len(stack) == 0:
#         print(1)
#     else:
#         print(0)


# def top():
#     if len(stack) == 0:
#         print(-1)
#     else:
#         print(stack[-1])


# N = int(sys.stdin.readline())
# stack = []
# for _ in range(N):
#     word = sys.stdin.readline().split()
#     order = word[0]
#     if order == "push":
#         push(word[1])
#     elif order == "pop":
#         pop()
#     elif order == "size":
#         size()
#     elif order == "empty":
#         empty()
#     elif order == "top":
#         top()
