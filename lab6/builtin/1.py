import functools as ft
def multNums():
    num_list=map(int, input().split())
    res=ft.reduce(lambda a, b: a*b, num_list)
    print(res)

    