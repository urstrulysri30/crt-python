try:
    lit = list(map(int, input().split()))
    for i in lit:
        print(i)
except ValueError:
    print('enter correct')
