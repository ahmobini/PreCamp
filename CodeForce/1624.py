def make_ap(sequence):
    sequence.sort()
    return 'YES' if sequence[1] % sequence[0] == 0 else 'NO'


if __name__ == '__main__':
    test_case_num = int(input())
    result = []
    for i in range(test_case_num):
        sequence = [int(i) for i in input().split()]
        result.append(make_ap(sequence))
    print(*result, sep='\n')
