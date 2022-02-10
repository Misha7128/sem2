def summ(n1, n2):
    n1 = str(n1).split('.')
    n2 = str(n2).split('.')
    ans = []
    if len(n1[0]) < len(n2[0]):
        n1[0] = '0' * abs(len(n1[0]) - len(n2[0])) + n1[0]
    elif len(n1[0]) > len(n2[0]):
        n2[0] = '0' * abs(len(n1[0]) - len(n2[0])) + n2[0]
    if len(n1[1]) < len(n2[1]):
        n1[1] += '0' * abs(len(n1[1]) - len(n2[1]))
    elif len(n1[1]) > len(n2[1]):
        n2[1] += '0' * abs(len(n2[1]) - len(n1[1]))
    x = 0
    for i in range(len(n1[1]) - 1, -1, -1):
        elem = (int(n1[1][i]) + int(n2[1][i])) % 3
        ans.insert(0, str(elem + x))
        x = (int(n1[1][i]) + int(n2[1][i])) // 3
    ans = '.' + ''.join(ans)
    for i in range(len(n1[0]) - 1, -1, -1):
        elem = (int(n1[0][i]) + int(n2[0][i])) % 3
        ans = str(elem + x) + ans
        x = (int(n1[0][i]) + int(n2[0][i])) // 3
    return float(ans)


def rasn(n1, n2):
    sign = ''
    if n1 < n2:
        sign = '-'
        n1, n2 = n2, n1
    n1 = str(n1).split('.')
    n2 = str(n2).split('.')
    if len(n1[0]) < len(n2[0]):
        n1[0] = '0' * abs(len(n1[0]) - len(n2[0])) + n1[0]
    elif len(n1[0]) > len(n2[0]):
        n2[0] = '0' * abs(len(n1[0]) - len(n2[0])) + n2[0]
    if len(n1[1]) < len(n2[1]):
        n1[1] += '0' * abs(len(n1[1]) - len(n2[1]))
    elif len(n1[1]) > len(n2[1]):
        n2[1] += '0' * abs(len(n2[1]) - len(n1[1]))
    x = 0
    ans = ''
    for i in range(len(n1[1]) - 1, -1, -1):
        if int(n1[1][i]) > int(n2[1][i]):
            ans = str(int(n1[1][i]) - int(n2[1][i]) - x) + ans
            x = 0
        elif int(n1[1][i]) == int(n2[1][i]) and x == 0:
            ans = str(int(n1[1][i]) - int(n2[1][i])) + ans
        elif int(n1[1][i]) == int(n2[1][i]) and x != 0:
            ans = '2' + ans
            x = 1
        elif int(n1[1][i]) < int(n2[1][i]):
            ans = str(3 + int(n1[1][i]) - int(n2[1][i])) + ans
            x = 1
    ans = '.' + ans
    for i in range(len(n1[0]) - 1, -1, -1):
        if int(n1[0][i]) > int(n2[0][i]):
            ans = str(int(n1[0][i]) - int(n2[0][i]) - x) + ans
            x = 0
        elif int(n1[0][i]) == int(n2[0][i]) and x == 0:
            ans = str(int(n1[0][i]) - int(n2[0][i])) + ans
        elif int(n1[0][i]) == int(n2[0][i]) and x != 0:
            ans = '2' + ans
            x = 1
        elif int(n1[0][i]) < int(n2[0][i]):
            ans = str(3 + int(n1[0][i]) - int(n2[0][i])) + ans
            x = 1
    ans = sign + ans
    return float(ans)