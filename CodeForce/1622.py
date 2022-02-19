def construct_sides(side):
    is_rectangle = 'NO'
    if sum(side) % 2 == 0:
        is_rectangle = 'YES'
    return is_rectangle


if __name__ == '__main__':
    test_case_num = int(input())
    result = []
    for case in range(test_case_num):
        sides = [int(num) for num in input().split()]
        result.append(construct_sides(sides))
    print(*result, sep = "\n")
