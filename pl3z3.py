def fib(n = 1, m = 1, d = 5):
    if d == 1:
        return m
    else:
        return fib(m, n+m, d - 1)
    
fib()
pass
    