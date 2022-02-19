def find(num1, num2, num3):
    n = [i for i in range(1, 5) if i not in [num1, num2, num3]]
    print(*n)


if __name__ == '__main__':
    numbers = [int(i) for i in input().split()]
    find(*numbers)
