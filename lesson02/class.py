def seven_boom(limit):
    counter = 0
    while counter <= limit:
        counter = counter + 1
        if counter % 7 == 0 or '7' in str(counter):
            print('boom')
            continue
        print(counter)


def int_to_number_name(number):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five']
    return numbers[number]


if __name__ == '__main__':
    seven_boom(100)
    print('='*25)
    print(int_to_number_name(5))
