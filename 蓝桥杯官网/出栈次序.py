def fib(n, m):
    if n == 0:  # 当只有等候区没有汽车时返回1
        return 1
    if m == 0:  # 当检测区没有汽车时，汽车入栈
        return fib(n-1, 1)
    if m > 0:  # 当检测区有汽车时，分为汽车入栈和汽车出栈
        return fib(n-1, m+1)+fib(n, m-1)
    return 0

print(fib(16,0))
