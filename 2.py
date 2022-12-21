value = input('Enter number: ')


def fibo(n):
    data = []
    a, b = 0, 1
    for _ in range(n):
        data.append(a)
        a, b = b, a + b
    return data


try:
    number = int(value)
    print(', '.join(str(x) for x in fibo(number)))
except ValueError:
    print('input is number !!')


# วิธีที่ 2
value = input('Enter number: ')


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end='')
        if i != n-1:
            print(', ', end='')
        a, b = b, a + b
    print()


try:
    fibo(int(value))
except ValueError:
    print('input is number !!')
