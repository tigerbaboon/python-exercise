value = input('Enter odd number: ')

try:
    number = int(value)
    if number % 2 != 0:
        i = 0
        j = 0
        for i in range(number):
            for j in range(number):
                if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                    print('-', end='')
                else:
                    print('*', end='')
            print()
    else:
        print('input is odd number !!')
except ValueError:
    print('input is odd number !!')
