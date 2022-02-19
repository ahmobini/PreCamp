def minority(binary_str):
    length = len(binary_str)
    if length < 3:
        return 0
    zeros_count = binary_str.count('0')
    ones_count = binary_str.count('1')
    if zeros_count == ones_count:
        return 0
    elif zeros_count < length // 2:
        return zeros_count
    return ones_count


if __name__ == '__main__':
    test_case_num = int(input())
    result = []
    for case in range(test_case_num):
        binary_str = input()
        result.append(minority(binary_str))
    print(*result, sep='\n')
