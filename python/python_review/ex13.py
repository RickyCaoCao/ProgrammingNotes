# Exercise 13 - Fibonacci
# Use for i in range(..) than while loop

def create_fib(num=1):
    if num < 1:
        print('Error: We need positive num.')
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, num):
            fib.append(fib[i-2]+fib[i-1])
        return fib

num = int(raw_input("Enter an integer: "))
print(create_fib(num))