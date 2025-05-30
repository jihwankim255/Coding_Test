import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

'''
10, 20, 10, 30, 20, 50 . . .. .. . ..

10
20
30
50


10 50 10 20 30
dp = []
감이아ㅏㄴ와 어떻게 풀지?
증가를해야한다
완전탐색을 하지않고?
결정되는게잇나?

10  20 x
     x x

x    20 x
      x x

'''