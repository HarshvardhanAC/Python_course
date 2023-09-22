def fibonacci(n):
    result= fibonacci(n-1) + fibonacci(n-2)
    print(result)
    
fibonacci(5)