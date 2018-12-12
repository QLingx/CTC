
def step(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 4
    return step(N-1) + step(N-2) + step(N-3)

def step_iter(N):
    res = [0,1,2,4]
    if N > 3:
        for i in range(4,N+1):
            tmp = i % 4
            res[tmp] = res[(i-1)%4] + res[(i-2)%4]+res[(i-3)%4]
    return res[N % 4]

if __name__ == '__main__':
    n = step_iter(4)
    print(n)
    n = step_iter(5)
    print(n)
    n = step_iter(6)
    print(n)
    n = step_iter(7)
    print(n)
