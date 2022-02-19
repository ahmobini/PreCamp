def game(num):
    str_number = str(num)
    number_list = [int(str_number[0]), int(str_number[1])]
    return max(number_list) - min(number_list)


if __name__ == '__main__':
    number = int(input())
    print(game(number))
