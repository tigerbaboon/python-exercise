value_A = input('Enter number A: ')
value_B = input('Enter number B: ')

try:
    a = int(value_A)
    b = int(value_B)
    res = ''
    for i in range(a+b):
        if res[-1:] == 'B' or res[-1:] == '':
            if a == 0 or b == 0:
                if a == 0 and b != 0:
                    b = b - 1
                    res = res + 'B'
                elif b == 0 and a != 0:
                    a = a - 1
                    res = res + 'A'
                elif a == 0 and b == 0:
                    break
            else:
                if a > b:
                    if (res[-2:] == 'AA'):
                        print('error')
                        break
                    else:
                        a = a - 2
                        res = res + 'AA'
                elif b > a:
                    if (res[-2:] == 'BB'):
                        print('error')
                        break
                    else:
                        b = b - 2
                        res = res + 'BB'
                elif b == a:
                    a = a - 1
                    b = b - 1
                    res = res + 'AB'
        elif res[-1:] == 'A':
            if a == 0 or b == 0:
                if a == 0 and b != 0:
                    b = b - 1
                    res = res + 'B'
                elif b == 0 and a != 0:
                    a = a - 1
                    res = res + 'A'
                elif a == 0 and b == 0:
                    break
            else:
                if b > a:
                    if (res[-2:] == 'BB'):
                        print('error')
                        break
                    else:
                        b = b - 2
                        res = res + 'BB'
                elif a > b:
                    if (res[-2:] == 'AA'):
                        print('error')
                        break
                    else:
                        a = a - 2
                        res = res + 'AA'
                elif b == a:
                    a = a - 1
                    b = b - 1
                    res = res + 'BA'
    print(res)

except ValueError:
    print('error')
